
import sqlite3
import os

from abc import ABCMeta

from .log import Logger
from .models import AddressBook


DB_NAME = "addressbook.db"
TABLE_NAME = "ADDRESS_BOOK"


class BaseDAO(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        db_name = kwargs.get('db_name')
        logger_name = kwargs.get('logger_name')
        logger_filename = kwargs.get('logger_filename')

        db_name = db_name if db_name else 'base.db'
        logger_name = logger_name if logger_name else 'DAO'
        logger_filename = logger_filename if logger_filename else 'DAO.log'

        self.connect(db_name=db_name)
        self.logger = Logger(name=logger_name, filename=logger_filename)

    @property
    def Connection(self):
        return self.__conn

    @Connection.setter
    def Connection(self, db_name):
        self.__conn = sqlite3.connect(db_name)

    def connect(self, db_name=DB_NAME):
        self.Connection = db_name

    def create(self, table_name=TABLE_NAME, drop=False):
        try:
            cur = self.Connection.cursor()

            if drop:
                query = f"DROP TABLE {table_name};"
                self.logger.info(f"QUERY: {query}")

                cur.execute(query)
                self.Connection.commit()

            query = f"""
                CREATE
                TABLE {table_name} (
                    ID           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    NAME         TEXT,
                    ADDRESS      TEXT,
                    PHONE_NUMBER TEXT,
                    EMAIL        TEXT
                );
            """
            self.logger.info(f"QUERY: {query}")
   
            cur.execute(query)
            self.Connection.commit()
            status = True
        except Exception as e:
            self.Connection.rollback()
            status = False
            self.logger.error(e)
        finally:
            cur.close()
        return status

    def table_info(self):
        query = """
        SELECT tbl_name
        FROM sqlite_master
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            result = cur.fetchall()
        except Exception as e:
            self.logger.error(e)
        finally:
            cur.close()
        return result

    def table_columns(self, table_name=TABLE_NAME):
        query = f"PRAGMA table_info({table_name});"
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            result = cur.fetchall()
        except Exception as e:
            self.logger.error(e)
        finally:
            cur.close()
        return result


class AddressBookDAO(BaseDAO):

    def __init__(self, **kwargs):
        db_name = os.path.join('db', DB_NAME)
        logger_name = 'AddressBookDAO'
        filename = os.path.join('log', 'AddressBookDao.log')

        super().__init__(
            db_name=db_name,
            logger_name=logger_name,
            logger_filename=filename
        )

    def view(self, addr: AddressBook):
        query = f"""
            SELECT *
                FROM {TABLE_NAME}
            WHERE
                ID = {addr.id};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            result = cur.fetchone()
        except Exception as e:
            result = None
            self.logger.error(e)
        finally:
            cur.close()
        return result

    def view_all(self):
        query = f"""
            SELECT *
            FROM {TABLE_NAME};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            result = cur.fetchall()
        except Exception as e:
            result = None
            self.logger.error(e)
        finally:
            cur.close()
        return result

    def add(self, new: AddressBook):
        query = f"""
            INSERT
                INTO {TABLE_NAME} (
                    NAME,
                    ADDRESS,
                    PHONE_NUMBER,
                    EMAIL
                )

                VALUES (
                '{new.name}',
                '{new.address}',
                '{new.phone_number}',
                '{new.email}'
            );
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            self.Connection.commit()
            status = True
        except Exception as e:
            self.Connection.rollback()
            status = False
            self.logger.error(e)
        finally:
            cur.close()
        return status

    def edit(self, old: AddressBook, new: AddressBook):
        query = f"""
            UPDATE
            SET
                NAME = '{new.name}'
                ADDRESS = '{new.address}'
                EMAIL = '{new.email}'
            FROM {TABLE_NAME}
            WHERE
                ID = {old.id};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            self.Connection.commit()
            status = True
        except Exception as e:
            self.Connection.rollback()
            status = False
            self.logger.error(e)
        finally:
            cur.close()
        return status

    def remove(self, new: AddressBook):
        query = f"""
            DELETE
                FROM {TABLE_NAME}
            WHERE
                ID = {new.id};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            self.Connection.commit()
            status = True
        except Exception as e:
            self.Connection.rollback()
            status = False
            self.logger.error(e)
        finally:
            cur.close()
        return status

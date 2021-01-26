
import sqlite3
import os

from .log import Logger
from .models import AddressBook


DB_NAME = "addressbook.db"
TABLE_NAME = "ADDRESS_BOOK"


class AddressBookDAO:

    def __init__(self):
        db_name = os.path.join('db', DB_NAME)
        self.connect(db_name=db_name)

        filename = os.path.join('log', 'AddressBookDao.log')
        self.logger = Logger(name='AddressBookDAO', filename=filename)

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

    def table_columns(self):
        # query = f"""
        # SELECT sql
        # FROM sqlite_master
        # WHERE tbl_name='{TABLE_NAME}';
        # """
        query = f"""
        PRAGMA table_info({TABLE_NAME});
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

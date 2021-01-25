
import sqlite3

from log import Logger
from models import AddressBook


class AddressBookDAO:

    DB_NAME = "addressbook.db"
    TABLE_NAME = "ADDRESS_BOOK"

    def __init__(self):
        self.connect()
        self.logger = Logger(name='AddressBookDAO', filename='AddressBookDao.log')

    @property
    def Connection(self):
        return self.__conn

    @Connection.setter
    def Connection(self, db_name):
        self.__conn = sqlite3.connect(db_name)

    def connect(self, db_name=AddressBookDAO.DB_NAME):
        self.Connection = db_name
    
    def view(self, addr: AddressBook):
        query = f"""
            SELECT *
            FROM {AddressBookDAO.TABLE_NAME}
            WHERE
                ID = {addr.id};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
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
            FROM {AddressBookDAO.TABLE_NAME}
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
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
            INTO {AddressBookDAO.TABLE_NAME}
            VALUES(
                {new.name},
                {new.address},
                {new.phone_number},
                {new.email}
            );
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            self.Connection.commit()
            state = True
        except Exception as e:
            self.Connection.rollback()
            state = False
            self.logger.error(e)
        finally:
            cur.close()
        return state

    def edit(self, old: AddressBook, new: AddressBook):
        query = f"""
            UPDATE
            SET
                NAME = {new.name}
                ADDRESS = {new.address}
                EMAIL = {new.email}
            FROM {AddressBookDAO.TABLE_NAME}
            WHERE
                ID = {old.id};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            self.Connection.commit()
            state = True
        except Exception as e:
            self.Connection.rollback()
            state = False
            self.logger.error(e)
        finally:
            cur.close()
        return state

    def remove(self, new: AddressBook):
        query = f"""
            DELETE
            FROM {AddressBookDAO.TABLE_NAME}
            WHERE
                ID = {new.id};
        """
        self.logger.info(f"QUERY: {query}")

        try:
            cur = self.Connection.cursor()
            cur.execute(query)
            cur.commit()
        except Exception as e:
            self.logger.error(e)


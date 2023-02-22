import abc
import pymysql.cursors


class AbstractUserRepo:
    @abc.abstractmethod
    def create(self, user_data: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def edit(self, user_data: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, unique_key: str):
        raise NotImplementedError


class MySqlException(Exception):
    pass


class UserRepo(AbstractUserRepo):
    """
    Class represents User Repository that interacts with database
    """
    def __init__(self, db: pymysql.cursors):
        """
        Args:
            db: MYSQL connection
        """
        self.db = db

    def create(self, data: dict):
        """
        creates a record about new user in MYSQL table
        Args:
            data: dictionary with new user's info. Keys are columns in  the table
        Returns: None

        """
        try:
            with self.db.cursor() as cursor:
                query = "INSERT INTO users (username, first_name, last_name) VALUES(%s,%s,%s)"
                cursor.execute(query, (data['username'], data['first_name'], data['last_name']))
                self.db.commit()
        except Exception as e:
            raise MySqlException(e)

    def edit(self, data: dict):
        """
        Updates info about one user
        Args:
            data: dictionary with new user's info. Keys are columns in the table, values - new values.
             Key 'old_username' - unique username that will be used in WHERE statement

        Returns: None

        """
        with self.db.cursor() as cursor:
            values_to_set = ''
            for key, value in data.items():
                if key != 'old_username' and key != 'operation':
                    values_to_set += "{}='{}'".format(key, value) + ','

            values_to_set = values_to_set[:len(values_to_set) - 1]  # remove last ','
            query = f"UPDATE users SET {values_to_set} WHERE username='{data['old_username']}'"
            try:
                cursor.execute(query)
                self.db.commit()
            except Exception as e:
                raise MySqlException(e)

    def delete(self, unique_key: str):
        """
        Deletes info about user
        Args:
            unique_key: unique key to delete

        Returns:

        """
        try:
            with self.db.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE username='{}'".format(unique_key))
                self.db.commit()
        except Exception as e:
            raise MySqlException(e)


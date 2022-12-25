class UserRepo:
    """
    Class represents User Repository that interacts with database
    """
    def __init__(self, db):
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
        with self.db.cursor() as cursor:
            query = "INSERT INTO users (username, first_name, last_name) VALUES(%s,%s,%s)"
            cursor.execute(query, (data['username'], data['first_name'], data['last_name']))
            self.db.commit()

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
            cursor.execute(query)
            self.db.commit()

    def delete(self, data: dict):
        """
        Deletes info about user
        Args:
            data: dictionary where key - 'username' and its value - unique username to delete

        Returns:

        """
        with self.db.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE username='{}'".format(data['username']))
            self.db.commit()


from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class User:
    # THis model is for the attributes and must match the SQL table EXACTLY
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']

    @classmethod
    def create_one_user(cls, data):

        query = "INSERT INTO users (first_name, last_name, email) "
        query += "VALUES (%(user_first_name)s, %(user_last_name)s, %(user_email)s);"

        # result = connectToMySQL("users").query_db(query, data)
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM USERS;"
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_users = []

        for row in results:
            all_users.append(cls(row))  # Everything in the Users table
        return all_users

    @classmethod
    def get_one_user(cls, data):

        query = "SELECT * FROM users WHERE id = %(user_id)s ;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def edit_one_user(cls, data):
        query = "UPDATE users "
        query += "SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s  WHERE id =  %(user_id)s ;"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one_user(cls, data):

        query = "DELETE FROM users WHERE id = %(user_id)s ;"

        return connectToMySQL(DATABASE).query_db(query, data)

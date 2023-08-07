from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB


class User:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.first_name = data_dict["first_name"]
        self.last_name = data_dict["last_name"]
        self.email = data_dict["email"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    # ! all query must be in class methods
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(DB).query_db(query)
        all_user = []
        print(results)
        for row in results:
            user = cls(row)
            all_user.append(user)
        return all_user

    @classmethod
    def create_user(cls, data_dict):
        query = """
                INSERT INTO user (first_name, last_name, email)
                VALUES(%(first_name)s, %(last_name)s, %(email)s);
                """

        result = connectToMySQL(DB).query_db(query, data_dict)
        print(result)
        return None

    @classmethod
    def get_one_by_id(cls, data_dict):
        query = "SELECT * FROM user WHERE id = %(id)s;"

        results = connectToMySQL(DB).query_db(query, data_dict)
        print(results)
        return None

    @classmethod
    def update(cls, data_dict):
        query = """
                UPDATE user SET first_name = %(first_name)s, last_name = %(last_name)s, 
                email = %(email)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(DB).query_db(query, data_dict)

    @classmethod
    def delete(cls, data_dict):
        query = "DELETE FROM user WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data_dict)
        print(result)
        return result

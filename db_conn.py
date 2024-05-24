import mysql.connector
from PyQt5.QtWidgets import QMessageBox


class ConnectDatabase:
    def __init__(self):
        self._host = "localhost"
        self._user = "root"
        self._password = ""
        self._database = "db_eyegard"
        self.con = None
        self.cursor = None

    def connect_db(self):
        # Establish a database connection
        self.con = mysql.connector.connect(
            host=self._host,
            database=self._database,
            user=self._user,
            password=self._password
        )

        # Create a cursor for executing SQL queries
        self.cursor = self.con.cursor(dictionary=True)

    def add_info(self, student_id, first_name, last_name, filiere, groupe, email_address, image_path, face_encoding_json):

        self.connect_db()
            # Construct SQL query for adding information

        sql = f"""
                INSERT INTO students (studentId, firstName, lastName, filiere, groupe, emailAddress, image, face_encoding) 
                    VALUES ({student_id}, '{first_name}', '{last_name}', '{filiere}', '{groupe}', '{email_address}', '{image_path}', '{face_encoding_json}');
            """


        try:
            # Execute the SQL query for adding information
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()

    def update_info(self, student_id, first_name, last_name, filiere, groupe, email_address):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for updating information
        sql = f"""
                d, lastName='{last_name}', filiere='{filiere}', groupe='{groupe}', 
                        emailAddress='{email_address}'
                    WHERE studentId={student_id};
            """

        try:
            # Execute the SQL query for updating information
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()


    def delete_info(self, studentId):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for deleting information
        sql = f"""  
            DELETE FROM students WHERE studentId={studentId};
        """

        try:
            # Execute the SQL query for deleting information
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()

    def search_info(self, student_id=None, first_name=None, last_name=None, filiere=None, groupe=None, email_address=None):
            # Connect to the database
            self.connect_db()

            condition = ""
            if student_id:
                condition += f"studentId LIKE '%{student_id}%'"
            else:
                if first_name:
                    if condition:
                        condition += f" and firstName LIKE '%{first_name}%'"
                    else:
                        condition += f"firstName LIKE '%{first_name}%'"

                if last_name:
                    if condition:
                        condition += f" and lastName LIKE '%{last_name}%'"
                    else:
                        condition += f"lastName LIKE '%{last_name}%'"

                if filiere:
                    if condition:
                        condition += f" and filiere LIKE '%{filiere}%'"
                    else:
                        condition += f"filiere LIKE '%{filiere}%'"

                if groupe:
                    if condition:
                        condition += f" and groupe LIKE '%{groupe}%'"
                    else:
                        condition += f"groupe LIKE '%{groupe}%'"

                if email_address:
                    if condition:
                        condition += f" and emailAddress LIKE '%{email_address}%'"
                    else:
                        condition += f"emailAddress LIKE '%{email_address}%'"

            if condition:
                # Construct SQL query for searching information with conditions
                sql = f"""
                    SELECT * FROM students WHERE {condition};
                """
            else:
                # Construct SQL query for searching all information
                sql = f"""
                    SELECT * FROM students;
                 """

            try:
                # Execute the SQL query for searching information
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                return result

            except Exception as E:
                return E

            finally:
                self.con.close()


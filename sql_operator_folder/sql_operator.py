import mysql.connector
from mysql.connector import Error

class SqlOperator:


    def __init__(self):

        self.connection = mysql.connector.connect(host='localhost',
                                                database='emp_details_db',
                                                user='root',
                                                password='root')

    def sql_read(self,sql_select_query,sql_variable_values = None):
        self.__init__()
        connection = self.connection
        try:

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(sql_select_query,sql_variable_values)
                record = cursor.fetchall()
                

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return record


    def sql_write(self,sql_update_query,variables):

        
        
        self.__init__()
        connection = self.connection
        try:
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                
                cursor = connection.cursor()
                cursor.execute(sql_update_query,variables)
                print("rows changed is:",cursor.rowcount)
                connection.commit()
                cursor.close()
            
            
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


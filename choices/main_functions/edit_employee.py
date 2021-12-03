import mysql.connector
from mysql.connector import Error
from db_handler_sql.edit_employee_func import EditEmployee

obj_edit = EditEmployee()


import json

class EditEmployee:


    def edit_employee(self):

        self.emp_ids = self.get_employee_id_list()
        print("Registered Ids are ",self.emp_ids)
        
        self.input_id = int(input("Choose an Id to edit"))

        if self.input_id in self.emp_ids:
            obj_edit.edit_employee(self.input_id)
        else:
            print("ID not found")




    

    def get_employee_id_list(self):
        

        try:
            connection = mysql.connector.connect(host='localhost',
                                                    database='emp_details_db',
                                                    user='root',
                                                    password='root'
                                                    )

            
            get_emp_query = """ SELECT DISTINCT(Employee_ID) from employee_details """

            cursor = connection.cursor()
            cursor.execute(get_emp_query)
            self.records = cursor.fetchall()
            self.list_of_records = []

            for i in range(len(self.records)):
                self.list_of_records.append(self.records[i][0])

            
            
            
            
            
            cursor.close()
            connection.close()

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return self.list_of_records



    
        









    



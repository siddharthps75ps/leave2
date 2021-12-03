import json
import mysql.connector
from mysql.connector import Error

from os import access


class Create_Employee:

    
    
    def new_employee(self,employee_id,name,department,job):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.job = job

        employees = {
            'Employee_ID':self.employee_id,
            'Name':self.name,
            'Department':self.department,
            'Job':self.job
            }

        return employees

    def to_sql(self):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='emp_details_db',
                                                user='root',
                                                password='root')
            
            my_row = """ INSERT INTO employee_details(Employee_ID, Name, Department, Job) VALUES (%s, %s, %s, %s)"""
            
            list_of_row = [102,'Hari','Python','Developer']
            cursor = connection.cursor()
            
            cursor.execute(my_row,list_of_row)
            connection.commit()
            print(cursor.rowcount," row has been successfully inserted ")
            cursor.close()
         
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
            

        







    



 
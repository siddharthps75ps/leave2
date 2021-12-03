import json
import mysql.connector
from mysql.connector import Error
from sql_operator_folder.sql_operator import SqlOperator

obj_sql_op = SqlOperator()



class Create_Employee:

    
    
    def new_employee(self,employee_id,name,department,job):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.job = job

        self.employees = {
            'Employee_ID':self.employee_id,
            'Name':self.name,
            'Department':self.department,
            'Job':self.job
            }

        self.to_sql()

       

    def to_sql(self):

 
        sql_insert_Query = """INSERT INTO employee_details (Employee_ID, Name, Department, Job) VALUES (%s , %s, %s , %s)"""
        values = (self.employees["Employee_ID"],self.employees["Name"],self.employees["Department"],self.employees["Job"])
        
        obj_sql_op.sql_write(sql_insert_Query,values)  

        print("Employee Added")      

        







    



 
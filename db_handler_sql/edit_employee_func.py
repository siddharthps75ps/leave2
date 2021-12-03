import mysql.connector
from mysql.connector import Error

from sql_operator_folder.sql_operator import SqlOperator

obj_sql_op = SqlOperator()


class EditEmployee:



    def enter_new_details(self):
        self.Employee_ID = int(input("Enter new ID"))
        self.Name = input("Enter new Name")
        self.Department = input("Enter new Department")
        self.Job = input("Enter new Job") 

        self.new_details = {

            "employee_id" : self.Employee_ID,
            "name" : self.Name,
            "department":self.Department,
            "job":self.Job
        }

        return self.new_details


    def edit_employee(self,input_id):

        self.new_details_dict = self.enter_new_details()

        
            
        sql_update_query = "UPDATE employee_details SET Employee_ID = %s , Name = %s, Department = %s, Job = %s WHERE Employee_ID = %s"
        values = (self.new_details_dict["employee_id"],self.new_details_dict["name"],self.new_details_dict["department"],self.new_details_dict["job"],input_id)

        obj_sql_op.sql_write(sql_update_query,values)


            

        









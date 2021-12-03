import mysql.connector
from mysql.connector import Error

from sql_operator_folder.sql_operator import SqlOperator

obj_sql_op = SqlOperator()




class DeleteEmployeeFunc:

    def delete_emp(self,input_id):
    
        sql_delete_query = "DELETE FROM employee_details WHERE Employee_ID = %s "
        values = (input_id,)
        obj_sql_op.sql_write(sql_delete_query,values)
        print("Employee Deleted")

            



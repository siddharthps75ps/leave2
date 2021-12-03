import datetime
import json
from db_handler.add_attendance_func import AddAttendanceFunc


from sql_operator_folder.sql_operator import SqlOperator
from db_handler_sql.add_attendance_func import AddAttendanceFunc

obj_sql_op = SqlOperator()
obj_att_func = AddAttendanceFunc()

from datetime import date
class AddAttendance:

 
    
    


    def add_attendance(self):

        self.enter_date = input("Enter date")
        sql_select_query = " SELECT Employee_ID,Name from employee_details"
        self.employee_list = obj_sql_op.sql_read(sql_select_query)
        obj_att_func.add_attendance_func(self.employee_list,self.enter_date)
 
        



        

        

        


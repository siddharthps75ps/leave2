
from choices.main_functions.add_attendance import AddAttendance
from db_handler_sql.search_view_funcs import SearchViewFunc
from sql_operator_folder.sql_operator import SqlOperator
sql_op = SqlOperator()
obj_add = AddAttendance()
obj_search = SearchViewFunc() 
import json

class ChangeForADate:

    def change_for_date(self):

        self.enter_date = self.get_date_input()
        self.emp_id_list = self.get_emp_list()
        self.changing()


    def get_date_list(self):
        self.get_date_list_query = "SELECT DISTINCT(Date) FROM attendance_details"
        self.get_date_list = sql_op.sql_read(self.get_date_list_query)
        return self.get_date_list



    
    def get_date_input(self):

        date_enter = input("Enter Date to Change Attendance")
        date_list = self.get_date_list()
        for i in range(len(date_list)):
            if date_list[i][0] == date_enter:
                
                return date_enter
            else:
                print("Date not Found")






    def changing(self):
        

        for i in range(len(self.emp_id_list)):
            
            print("Enter Attendance for",self.emp_id_list[i][0])
            attendance = input()
            update_query = " UPDATE attendance_details SET Attendance = %s WHERE Date = %s AND Employee_ID = %s"
            values=(attendance,self.enter_date,self.emp_id_list[i][0])

            sql_op.sql_write(update_query,values)





    
    def get_emp_list(self):

        get_emp_list_query = " SELECT Employee_ID FROM employee_details "
        emp_id_list = sql_op.sql_read(get_emp_list_query)

        return emp_id_list


        


        



    
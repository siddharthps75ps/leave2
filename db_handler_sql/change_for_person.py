from db_handler_sql.change_for_a_date import ChangeForADate
from sql_operator_folder.sql_operator import SqlOperator

obj_op = SqlOperator()


obj_change = ChangeForADate()


class ChangeForPerson:

    def change_for_person(self):
        

        self.enter_date = obj_change.get_date_input()
        self.emp_id_list = obj_change.get_emp_list()
        self.enter_id = int(input("Enter ID to change attendance"))
        emp_id = self.get_emp()

        print("Enter Attendance for",emp_id)
        attendance = input()
        update_query = " UPDATE attendance_details SET Attendance = %s WHERE Date = %s AND Employee_ID = %s"
        values=(attendance,self.enter_date,emp_id)

        obj_op.sql_write(update_query,values)

        
        
    def get_emp(self):

            for i in range(len(self.emp_id_list)):
                if self.emp_id_list[i][0] == self.enter_id:
                    return self.emp_id_list[i][0]


        
            

        



    
        

    
    

        




        


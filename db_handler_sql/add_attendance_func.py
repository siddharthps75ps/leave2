
from sql_operator_folder.sql_operator import SqlOperator

obj_sql_op = SqlOperator()


class AddAttendanceFunc:

    def add_attendance_func(self, employee_list, enter_date):

        for i in range(len(employee_list)):

            print(f"Enter attendance for ID:{employee_list[i][0]} & Name:{employee_list[i][1]}")
            attendance = input("Enter p for Present or a for Absent")
            sql_attendance_query = " INSERT INTO attendance_details(Date, Employee_ID, Attendance) VALUES (%s, %s, %s)"
            values = (enter_date, employee_list[i][0], attendance)
            obj_sql_op.sql_write(sql_attendance_query, values)

        print("Attendance Added to the date:",enter_date)
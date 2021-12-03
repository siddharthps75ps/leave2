import json

from sql_operator_folder.sql_operator import SqlOperator

obj_sql_op = SqlOperator()

class SearchViewFunc:


    def search_options(self):

        print("Choose The Method You Want To View")
        print("\n 1.Filter by Date")
        print("\n 2.Filter by Department")
        print("\n 3.Search for Employee ID")

        choice = int(input("Enter Choice"))
        return choice

        

    

    def get_date_input(self):

        date_enter = input("Enter Date to View Attendance")
        for i in range(len(self.get_date_list)):
            if self.get_date_list[i][0] == date_enter:
                print("Printing Attendance details on the date :",date_enter) 
                return date_enter
            else:
                print("Date not Found")


    def get_department_input(self):

        department_enter = input("Enter Department to View Attendance")
        for i in range(len(self.get_department_list)):
            if self.get_department_list[i][0] == department_enter:
                print("Printing Attendance details on the department :",department_enter) 
                return department_enter
            else:
                print("Department not Found")


    def get_emp_id_input(self):

        emp_id_enter = int(input("Enter Employee ID to View Attendance"))
        
        for i in range(len(self.emp_id_list)):
            if self.emp_id_list[i][0] == emp_id_enter:
                print("Printing Attendance details on the department :",emp_id_enter) 
                return emp_id_enter
            else:
                print("Employee_ID not Found")


    def display_details(self,filter_data,filter_value):
        print("Attendance of the Filter:",filter_value)

        for i in range(len(filter_data)):

            
            print("\n", filter_data[i])


    def filter_by_date(self):

        self.get_date_list_query = "SELECT DISTINCT(Date) FROM attendance_details"
        self.get_date_list = obj_sql_op.sql_read(self.get_date_list_query)
        self.date_enter = self.get_date_input()

        self.filter_query = "   SELECT a.Date, e.Employee_ID, e.Name, a.Attendance FROM employee_details e JOIN attendance_details a ON e.Employee_ID = a.Employee_ID WHERE a.Date = %s "
        self.values=(self.date_enter,)
        self.filter_date_details = obj_sql_op.sql_read(self.filter_query,self.values)
        self.display_details(self.filter_date_details,self.date_enter)
    
    def filter_by_department(self):

        self.get_department_list_query = "SELECT DISTINCT(Department) FROM employee_details"
        self.get_department_list = obj_sql_op.sql_read(self.get_department_list_query)
        self.department_enter = self.get_department_input()

        self.filter_query = "   SELECT a.Date, e.Employee_ID, e.Name, a.Attendance FROM employee_details e JOIN attendance_details a ON e.Employee_ID = a.Employee_ID WHERE e.Department = %s "
        self.values = (self.department_enter,)
        self.filter_department_details = obj_sql_op.sql_read(self.filter_query,self.values)

        self.display_details(self.filter_department_details,self.department_enter)



    def filter_by_emp_id(self):

        self.get_emp_id_list_query = "SELECT DISTINCT(Employee_ID) FROM employee_details"
        self.emp_id_list = obj_sql_op.sql_read(self.get_emp_id_list_query)
        self.emp_id_enter = self.get_emp_id_input()

        self.filter_query = "   SELECT a.Date, e.Employee_ID, e.Name, a.Attendance FROM employee_details e JOIN attendance_details a ON e.Employee_ID = a.Employee_ID WHERE e.Employee_ID = %s "
        self.values = (self.emp_id_enter,)
        self.filter_emp_id_details = obj_sql_op.sql_read(self.filter_query,self.values)
        self.display_details(self.filter_emp_id_details,self.emp_id_enter)


















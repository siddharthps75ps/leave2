import json


class SearchViewFunc:


    def search_options(self):

        print("Choose The Method You Want To View")
        print("\n 1.Filter by Date")
        print("\n 2.Filter by Department")
        print("\n 3.Search for Employee ID")

        choice = int(input("Enter Choice"))
        return choice

        

    
    
    
    
    def read_attendance_json(self):

        with open('database/attendance_file.json','r') as access_json:
            data = json.load(access_json)
        return data["attendance_details"]


    def get_date_index(self,file_data):
        date_input = input("Enter date to search")
        
        for i in range(len(file_data)):
            if file_data[i]["date"] == date_input:
                return i
            else:
                pass
        


    def display_by_date(self,index,file_data):
        
        date_index = index

        for i in range(len(file_data[date_index]["details"])):
            print("\n")
            print(file_data[date_index]["details"][i])

    
    
    
    
    def read_json_employee(self):
        with open('database/sample2.json','r') as access_json:
            data = json.load(access_json)
        return data["employee_details"]

    
    def get_id_list(self,file_data_employee):
        id_list = []
        for i in range(len(file_data_employee)):
            id_list.append(file_data_employee[i]["Employee_ID"])

        return set(id_list)
        




    
    def get_department_list(self,file_data_employee):
        department_list = []
        for i in range(len(file_data_employee)):
            department_list.append(file_data_employee[i]["Department"])

        return set(department_list)

    def get_employee_id_from_department(self,dept,file_data_employee):

        emp_id_list = []

        for i in range(len(file_data_employee)):
            if file_data_employee[i]["Department"]==dept:
                emp_id_list.append(file_data_employee[i]["Employee_ID"])
            else:
                pass

            
        return emp_id_list

    def filter_by_date(self):

        file_data = self.read_attendance_json()
        date_index = self.get_date_index(file_data)
        self.display_by_date(date_index,file_data)


    def filter_by_department(self):
        file_data_attendance = self.read_attendance_json()
        file_data_employee = self.read_json_employee()
        department_list = list(self.get_department_list(file_data_employee))
        
        date_index = self.get_date_index(file_data_attendance)
        
        
        print(f"Choose Department  \n 1.{list(department_list)[0]} \n 2.{list(department_list)[1]} \n 3.{list(department_list)[2]}")
        choice = int(input("Select a Department"))

        if choice == 1:
            
            self.dept_choice(0,department_list,file_data_employee,file_data_attendance,date_index)

        if choice == 2:
            self.dept_choice(1,department_list,file_data_employee,file_data_attendance,date_index)

        if choice ==3:
            self.dept_choice(2,department_list,file_data_employee,file_data_attendance,date_index)


    def dept_choice(self,dept_no,department_list,file_data_employee,file_data_attendance,date_index):
        emp_id_list = self.get_employee_id_from_department(department_list[dept_no],file_data_employee)
            
        print(f"Attendance Details of {department_list[dept_no]} Department")
        for i in (file_data_attendance[date_index]["details"]):
            if i["id"] in emp_id_list:
                print(i)


    

    def filter_by_emp_id(self):

        file_data_attendance = self.read_attendance_json()
        file_data_employee = self.read_json_employee()
        id_list = self.get_id_list(file_data_employee)
        date_index = self.get_date_index(file_data_attendance)

        print (f"Choose an ID {list(id_list)}")

        input_id = input()

        if input_id in list(id_list):
            for i in (file_data_attendance[date_index]["details"]):
                if i['id']==input_id:
                    print(i)


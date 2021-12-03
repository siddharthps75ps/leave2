from choices.main_functions.add_attendance import AddAttendance
from db_handler.search_view_funcs import SearchViewFunc
from db_handler.change_for_a_date import ChangeForADate
from db_handler.search_view_funcs import SearchViewFunc
obj_search_view = SearchViewFunc()
obj_change = ChangeForADate()
obj_add = AddAttendance()
obj_search = SearchViewFunc() 

class ChangeForPerson:

    
    def change_attendance(self,file_data_attendance,date_index,person_index,id_input):
        attendance_value = input(f"Enter attendance for {id_input}")

        file_data_attendance[date_index]["details"][person_index]["attendance"] = attendance_value
        print(file_data_attendance[date_index]["details"][person_index]["attendance"])
    
    
    def enter_emp_id(self,emp_id_list):

        id_input = input("Enter Employee ID")
        
        if id_input in emp_id_list:
            return id_input
        else:
            print("Entered ID not registered")
    
    def get_person_index(self,file_data_attendance,date_index,id_input):
        for i in range(len(file_data_attendance[date_index]["details"])):
            if file_data_attendance[date_index]["details"][i]["id"] == id_input:
                return i
            else:
                pass

    def change_for_person(self):

        file_data_attendance = obj_search.read_attendance_json()
        file_data_employee = obj_search.read_json_employee()
        
        date_index = obj_change.find_index_position_of_date()
        emp_id_list = obj_search_view.get_id_list(file_data_employee)
        
        id_input = self.enter_emp_id(emp_id_list)
        person_index = self.get_person_index(file_data_attendance,date_index,id_input)
        self.change_attendance(file_data_attendance,date_index,person_index,id_input)

        dict_attendance = {
            "attendance_details":file_data_attendance
        }

        obj_change.to_json(dict_attendance)

        




        


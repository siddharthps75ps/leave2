from db_handler.search_view_funcs import SearchViewFunc
from choices.main_functions.add_attendance import AddAttendance
obj_add = AddAttendance()
obj_search = SearchViewFunc() 
import json

class ChangeForADate:

    def date_enter(self):

        date_to_change = input("Input date to change Attendance")
        return date_to_change

    def find_index_position_of_date(self):

        date_to_change = self.date_enter()
        data_file_attendance = obj_search.read_attendance_json()

        for i in range(len(data_file_attendance)):
            if data_file_attendance[i]["date"] == date_to_change:
                return i
            else:
                pass

                


    
    
    def to_json(self,dict_out):

        with open('database/attendance_file.json','w') as outfile:
            data = json.dumps(dict_out,indent =4)
            outfile.write(data)
            outfile.close()
    
    
    def change_for_date(self):
        print("inside change for date")
        data_file_attendance = obj_search.read_attendance_json()
        data_file_employee = obj_search.read_json_employee()
        date_index = self.find_index_position_of_date()

        new_details = obj_add.details_list(data_file_employee)

        # attendance_dict = {
        #     "date":self.date_enter,
        #     "details":new_details
        # }

        data_file_attendance[date_index]["details"]=new_details

        dict_out = {
            "attendance_details":data_file_attendance
        }


        self.to_json(dict_out)

        


        



    
import json

class DeleteEmployeeFunc:

    def list_of_employees_id(self,data_as_list):
            employee_ids = []
            length = len(data_as_list['employee_details'])

            for i in range(length):
                employee_ids.append(data_as_list['employee_details'][i]['Employee_ID'])

            return employee_ids


    def read_from_json(self):
        with open('database/sample2.json','r') as access_json:
            data = json.load(access_json)
            access_json.close()

        return data



    def find_position(self,employee_ids,id):
        
        position = employee_ids.index(id)
        return position
import json
from db_handler.delete_employee_func import DeleteEmployeeFunc
object_delete = DeleteEmployeeFunc()

from choices.main_functions.edit_employee import EditEmployee
from db_handler_sql.delete_employee_func import DeleteEmployeeFunc

obj_del = DeleteEmployeeFunc()

obj_edit = EditEmployee()


class DeleteEmployee:

    def delete_emp(self):
    

        self.list_of_records = obj_edit.get_employee_id_list()
        print("Registered IDs are ",self.list_of_records)
        self.input_id = int(input("Choose an Id to edit "))

        if self.input_id in self.list_of_records:
            obj_del.delete_emp(self.input_id)
        else:
            print("ID not registerd")
            









from choices.main_functions.add_employee import AddEmployee
from choices.main_functions.edit_employee import EditEmployee
from choices.main_functions.delete_employee import DeleteEmployee
from choices.main_functions.add_attendance import AddAttendance
from choices.main_functions.search_and_view import SearchAndView
from choices.main_functions.change_attendance import ChangeAttendance

ob_add_emp=AddEmployee()
ob_edit_emp=EditEmployee()
ob_delete_emp=DeleteEmployee()
ob_add_att=AddAttendance()
ob_search=SearchAndView()
ob_change_att=ChangeAttendance()


class MainChoice:

    def select_choice(self, ch):

        if ch==1:
            
            ob_add_emp.add_emp_func()

        elif ch==2:
            
            ob_edit_emp.edit_employee()

        elif ch==3:
            
            ob_delete_emp.delete_emp()

        elif ch==4:
            
            ob_add_att.add_attendance()
            

        elif ch==5:
            
            ob_search.search_view()

        elif ch==6:

            ob_change_att.change_attendance()

            
        

        

        
            
        


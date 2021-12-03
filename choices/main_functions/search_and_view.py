import json
from db_handler_sql.search_view_funcs import SearchViewFunc
obj = SearchViewFunc()

class SearchAndView:

    
    def search_view(self):

        choice = obj.search_options()
        
        if choice == 1:
            obj.filter_by_date()

        elif choice == 2:
            
            obj.filter_by_department()

        elif choice == 3:

            obj.filter_by_emp_id()

                    




        




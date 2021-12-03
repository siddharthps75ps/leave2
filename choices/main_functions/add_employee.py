from db_handler_sql.add_employee_func import Create_Employee


class AddEmployee:

    def add_emp_func(self):

                while(True):

                    employee_id = input("Enter Employee ID")
                    name = input("Enter name")
                    department = input("Enter Department")
                    job = input("Enter job")

                    ob = Create_Employee()
                    ob.new_employee(employee_id,name,department,job)
                    
                    
                    
                    try:
                        do_you_want_to_continue = str(input("Do You Want To Continue ? Enter Y or N"))
                    except TypeError:
                        print("You entered the wrong command")
                        continue

                    if do_you_want_to_continue == 'y' or do_you_want_to_continue == 'Y':
                        continue
                    else:
                        break

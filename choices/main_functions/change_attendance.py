from db_handler_sql.change_for_a_date import ChangeForADate
from db_handler_sql.change_for_person import ChangeForPerson
obj_change_date = ChangeForADate()
obj_change_person = ChangeForPerson()


class ChangeAttendance:

    def change_attendance(self):

        print("\n 1. Change for a date")
        print("\n 2. Change for a Person")

        choice = int(input("Enter choice"))

        if choice == 1:
            obj_change_date.change_for_date()

        elif choice == 2:
            obj_change_person.change_for_person()


        

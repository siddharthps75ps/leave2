
from choices.choice_main import MainChoice

def choice_func():

    print('LEAVE MANAGEMENT SYSTEM')

    print('\n 1. Add new Employee')
    print('\n 2. Edit an Employee')
    print('\n 3. Delete an Employee')
    print('\n 4. Attendance Details')
    print("\n 5. Filter Attendance Page")
    print("\n 6. Change Attendence")
    print("\n 7. Exit ")


    
    choice=int(input("Enter choice"))
    return choice


if __name__ == '__main__':
    choice = 0
    while(choice!=7):

        choice = choice_func()

        
        MainChoice().select_choice(choice)

    


    
        


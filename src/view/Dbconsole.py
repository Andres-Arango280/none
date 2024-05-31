import sys
sys.path.append("src")

import controller.usercontroller as usercontroller
from controller.usercontroller import *

"""Consola de entrega final, ejecutar esta para hacer ultima entrega #5"""

def search_by_id():
    try:
        idnumber = input("Enter the ID of the user you want to search: ")
        searched_user = usercontroller.SearchById(idnumber)
        print(f"User found: {searched_user.firstname} {searched_user.surname} {searched_user.idnumber} {searched_user.mail}")
    except Exception as err:
        print("Error:", err)

def search_by_name_surname():
    try:
        firstname = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        searched_user = usercontroller.SearchByNameAndSurname(firstname, surname)
        if searched_user:
            print(f"User found: {searched_user.firstname} {searched_user.surname} {searched_user.idnumber} {searched_user.mail}")
        else:
            print("User not found.")
    except Exception as err:
        print("Error:", err)

def search_by_id_tables():
    try:
        idnumber = input("Enter the ID of the user you want to search: ")


        print(f"Debug: Searching for user with ID: {idnumber}")

        result = SearchInAllTablesByID(idnumber)

        if not result:
            raise ValueError(f"No data returned from SearchInAllTablesByID for ID: {idnumber}.")

        employee, accruals, deductions = result

        if not employee:
            raise ValueError("No employee data found.")
        if not accruals:
            raise ValueError("No accruals data found.")
        if not deductions:
            raise ValueError("No deductions data found.")

        print(f"Name: {employee.firstname}")
        print(f"Username: {employee.surname}")
        print(f"ID: {employee.idnumber}")
        print(f"Mail: {employee.mail}")

        print(f"Basic salary: {accruals.BasicSalary}")
        print(f"Worked days: {accruals.WorkedDays} for the value of {accruals.CalculateDailySalary()}")
        print(f"Holiday time worked: {accruals.HolidayTimeWorked} for the value of {accruals.CalculateValueOfHolidaysWorked(accruals.CalculateDailySalary())}")
        print(f"Extra daylight hours worked: {accruals.ExtraDaylightHoursWorked} for the value of {accruals.CalculateDaylightExtraHoursCharge()}")
        print(f"Extra night hours worked: {accruals.ExtraNightHoursWorked} for the value of {accruals.CalculateExtraNightHoursCharge()}")
        print(f"Holiday extra daylight hours worked: {accruals.HolidayExtraDaylightHoursWorked} for the value of {accruals.CalculateHolidayExtraDaylightHoursWorkedValue()}")
        print(f"Holiday extra night hours worked: {accruals.HolidayExtraNightHoursWorked} for the value of {accruals.CalculateHolidayExtraNightHoursWorkedValue()}")
        print(f"Days of disability: {accruals.DaysOfDisability} with a value of {accruals.CalculateDisabilityTimeValue()}")
        print(f"Leave days: {accruals.LeaveDays} with a value of {accruals.CalculateLeaveDaysValue()}")

        print(f"Health insurance percentage: {deductions.HealthInsurancePercentage} that costs: {deductions.CalculateHealthInsurance()}")
        print(f"Pension contribution percentage: {deductions.PensionContributionPercentage}")
        print(f"Pension solidarity fund contribution percentage: {deductions.PensionSolidarityFundContributionPercentage} that costs: {deductions.CalculatePensionSolidarityFundContribution()}")

        salary_calculator = SalaryCalculator(accruals, deductions)
        net_salary = salary_calculator.calculate_net_salary()
        print(f"Net salary: {net_salary}")

    except ErrorNotfound as err:
        print(err)
    except Exception as err:
        print("Error:", err)


def modify_employee_info():
    try:
        idnumber = input("Enter the ID of the user you want to change any info: ")
        employee = SearchById(idnumber)

        if employee is not None:
            print(f"Employee found: {employee.firstname} {employee.surname}, ID: {employee.idnumber}, Email: {employee.mail}")
            
            valid_field = False
            while not valid_field:
                field_to_change = input("Which info would you like to change? (firstname, surname, mail): ")

                if field_to_change in ['firstname', 'surname', 'mail']:
                    valid_field = True
                    new_value = input(f"Enter the new value for {field_to_change}: ")
                    
                    setattr(employee, field_to_change, new_value)
                    
                    Update(employee)

                    print(f"{field_to_change} changed successfully")
                else:
                    print("Invalid field. Please enter either 'firstname', 'surname', or 'mail'.")
        else:
            print("Employee not found.")

    except ErrorNotfound as e:
        print(e)

def input_employee():
    firstname = input("Enter first name: ")
    surname = input("Enter surname: ")
    idnumber = input("Enter ID number: ")
    mail = input("Enter email: ")
    return Employee(firstname, surname, idnumber, mail)

def input_accruals():
    idnumber = input("Type your id number: ")
    BasicSalary = input("Enter basic salary: ")
    WorkedDays = input("Enter worked days: ")
    HolidayTimeWorked = input("Enter holiday time worked: ")
    ExtraDaylightHoursWorked = input("Enter extra daylight hours worked: ")
    ExtraNightHoursWorked = input("Enter extra night hours worked: ")
    HolidayExtraDaylightHoursWorked = input("Enter holiday extra daylight hours worked: ")
    HolidayExtraNightHoursWorked = input("Enter holiday extra night hours worked: ")
    DaysOfDisability = input("Enter days of disability: ")
    LeaveDays = input("Enter leave days: ")
    return Accruals(idnumber, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays)

def input_deductions():
    idnumber = input("Type your id number: ")
    accruals = Accruals
    HealthInsurancePercentage = input("Enter health insurance percentage: ")
    PensionContributionPercentage = input("Enter pension contribution percentage: ")
    PensionSolidarityFundContributionPercentage = input("Enter pension solidarity fund contribution percentage: ")
    return Deductions(idnumber, accruals, HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage)

def table_modification_menu():
    while True:
        print("\n--- Table Modification Menu ---")
        print("1. Create 'employees' table")
        print("2. Create 'Deductions' table")
        print("3. Create 'Accruals' table")
        print("4. Delete 'employees' table")
        print("5. Delete 'Deductions' table")
        print("6. Delete 'Accruals' table")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            CreateTable()
        elif choice == '2':
            CreateTableDeductions()
        elif choice == '3':
            CreateAccrualsTable()
        elif choice == '4':
            DeleteTable()
        elif choice == '5':
            DeleteTableDeductions()
        elif choice == '6':
            DeleteTableAccruals()
        elif choice == '7':
            print("Leaving the program.")
            break
        else:
            print("Invalid option. Please try again.")

def input_all_information():
    firstname = input("Enter first name: ")
    surname = input("Enter surname: ")
    idnumber = input("Enter ID number: ")
    mail = input("Enter email: ")

    print("\n--- Accruals Information ---")
    BasicSalary = input("Enter basic salary: ")
    WorkedDays = input("Enter worked days: ")
    HolidayTimeWorked = input("Enter holiday time worked: ")
    ExtraDaylightHoursWorked = input("Enter extra daylight hours worked: ")
    ExtraNightHoursWorked = input("Enter extra night hours worked: ")
    HolidayExtraDaylightHoursWorked = input("Enter holiday extra daylight hours worked: ")
    HolidayExtraNightHoursWorked = input("Enter holiday extra night hours worked: ")
    DaysOfDisability = input("Enter days of disability: ")
    LeaveDays = input("Enter leave days: ")

    print("\n--- Deductions Information ---")
    HealthInsurancePercentage = input("Enter health insurance percentage: ")
    PensionContributionPercentage = input("Enter pension contribution percentage: ")
    PensionSolidarityFundContributionPercentage = input("Enter pension solidarity fund contribution percentage: ")

    employee = Employee(firstname, surname, idnumber, mail)
    accruals = Accruals(idnumber, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays)
    deductions = Deductions(idnumber, accruals, HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage)

    return employee, accruals, deductions

def information_insertion_menu():
    while True:
        print("\n--- Information Insertion Menu ---")
        print("1. Insert all information")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            employee, accruals, deductions = input_all_information()
            try:
                Insert(employee)
                InsertAccruals(accruals)
                InsertDeductions(deductions)
                print("All information inserted successfully.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inserting information: {e}")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Search by ID")
        print("2. Search by Name and Surname")
        print("3. Consult payroll by ID")
        print("4. Modify Employee Info")
        print("5. Insert an user")
        print("6. Modify, add and delete Tables")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            search_by_id()
        elif choice == '2':
            search_by_name_surname()
        elif choice == '3':
            search_by_id_tables()
        elif choice == '4':
            modify_employee_info()
        elif choice == '5':
            information_insertion_menu()
        elif choice == '6':
            table_modification_menu()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()

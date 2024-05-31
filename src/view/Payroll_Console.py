"""User console that prompts for the input data required to calculate the employee's payroll."""

import sys

sys.path.append("src")

from model.Payroll_Logic import *

def main():
    print("This program allows you to calculate the payroll accounting.")

    print("")
    
    while True:
        try:
            BasicSalary = float(input("Enter the monthly base salary: "))
            if BasicSalary < 30000:
                raise ValueError("The base salary cannot be less than 30000.")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: Por favor, ingresa un número válido.")
            else:
                print("Error: " + str(ve))

    while True:
        try:
            WorkedDays = int(input("Enter the days worked: "))
            if WorkedDays > 30:
                raise ValueError("it may be less than 30 days to make the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for worked days, please correct it.")
            else:
                print("Error: " + str(ve))

    while True:
        try:
            HolidayTimeWorked = int(input("Enter the holidays worked: "))
            if HolidayTimeWorked > 3:
                raise ValueError("3 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Holiday time worked, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            ExtraDaylightHoursWorked = int(input("Enter the number of daylight extra hours worked: "))
            if ExtraDaylightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Daylight hours worked, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            ExtraNightHoursWorked = int(input("Enter the number of night extra hours worked: "))
            if ExtraNightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for night worked hours, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            HolidayExtraDaylightHoursWorked = int(input("Enter the number of holiday daylight extra hours worked: "))
            if HolidayExtraDaylightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Holiday Daylight hours worked, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            HolidayExtraNightHoursWorked = int(input("Enter the number of holiday night extra hours worked: "))
            if HolidayExtraNightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Holiday night worked hours, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            HealthInsurancePercentage = float(input("Enter the health contribution percentage: "))
            if HealthInsurancePercentage > 4:
                raise ValueError("4% cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: invalid value for health percentage, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            PensionContributionPercentage = float(input("Enter the pension contribution percentage: "))
            if PensionContributionPercentage > 4:
                raise ValueError("4% cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: invalid value for pension contribution, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            PensionSolidarityFundContributionPercentage = float(input("Enter the percentage of pension solidarity fund contribution: "))
            if PensionSolidarityFundContributionPercentage > 3:
                raise ValueError("3% cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: invalid value for pension solidarity fund, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            DaysOfDisability = int(input("Enter the number of days of disability:"))
            if DaysOfDisability > 30:
                raise ValueError("30 days cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for days of disability, please correct it")
            else:
                print("Error: " + str(ve))    
    
    while True:
        try:
            LeaveDays = int(input("Enter the license number you had:\n1. Maternity leave\n2. Paternity leave\n3. Bereavement leave\n4. Leave to care for minor children\n5. I didn't have leave days "))
            if LeaveDays > 5:
                raise ValueError("This option does not exist, choose an option between 1 to 5")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10" in str(ve):
                print("Error: invalid value for leave days, please correct it")
            else:
                print("Error: " + str(ve))
    
    """Instance of Accruals class"""
    accruals = Accruals(BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, 
                        HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays)

    """Instance of Deductions class"""
    deductions = Deductions(accruals, HealthInsurancePercentage, PensionContributionPercentage, 
                            PensionSolidarityFundContributionPercentage)

    """Instance of SalaryCalculator class"""
    calculator = SalaryCalculator(accruals, deductions)

    print("")

    print(f"Daily salary: ${accruals.CalculateDailySalary():,.2f}")
    print("Subsidy transport: ", accruals.CalculateSubsidyTransport())
    print(f"Total salary is: ${accruals.CalculateTotalSalary():,.2f}")
    print(f"Value of holidays worked: ${accruals.CalculateValueOfHolidaysWorked(accruals.CalculateDailySalary()):,.2f}")
    print(f"Value of daylight extra hours worked: ${accruals.CalculateDaylightExtraHoursCharge():,.2f}")
    print(f"Value of extra night hours worked: ${accruals.CalculateExtraNightHoursCharge():,.2f}")
    print(f"Value of holiday extra daylight hours worked: ${accruals.CalculateHolidayExtraDaylightHoursWorkedValue():,.2f}")
    print(f"Value of holiday extra night hours worked: ${accruals.CalculateHolidayExtraNightHoursWorkedValue():,.2f}")
    print(f"Value of disability time: ${accruals.CalculateDisabilityTimeValue():,.2f}")
    print(f"Value of leave days: ${accruals.CalculateLeaveDaysValue():,.2f}")

    print("")
    print("Total accruals: {:,.2f}".format(accruals.calculate_total_accruals()))
    print("")

    print(f"Health insurance percentage discounted: {deductions.CalculateHealthInsurance():,.2f}")
    print(f"Pension contribution percentage discounted: {deductions.CalculatePensionContribution():,.2f}")
    print(f"Pension solidarity fund contribution percentage discounted: {deductions.CalculatePensionSolidarityFundContribution():,.2f}")

    print("")
    print("Total deductions: {:,.2f}".format(deductions.calculate_total_deductions()))
    print("")

    print(f"Net salary to be paid: ${calculator.calculate_net_salary():,.2f}")

if __name__ == "__main__":
    main()




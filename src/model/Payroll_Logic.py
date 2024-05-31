from datetime import date

class Employee:

    def __init__(self, firstname, surname, idnumber, mail):
        self.firstname = firstname
        self.surname = surname
        self.idnumber = idnumber
        self.mail = mail

    def __eq__(self, other):
        if isinstance(other, Employee):
            return (self.firstname == other.firstname and 
                    self.surname == other.surname and 
                    self.idnumber == other.idnumber and 
                    self.mail == other.mail)
        return False

"""Accruals are all the items for which an employee receives remuneration."""
class Accruals:
    
    def __init__(self,idnumber, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked,
                ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked,
                HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays):
        
        self.idnumber = int(idnumber)
        self.BasicSalary = float(BasicSalary)
        self.WorkedDays = int(WorkedDays)
        self.HolidayTimeWorked = float(HolidayTimeWorked)
        self.ExtraDaylightHoursWorked = float(ExtraDaylightHoursWorked)
        self.ExtraNightHoursWorked = float(ExtraNightHoursWorked)
        self.HolidayExtraDaylightHoursWorked = float(HolidayExtraDaylightHoursWorked)
        self.HolidayExtraNightHoursWorked = float(HolidayExtraNightHoursWorked)
        self.DaysOfDisability = int(DaysOfDisability)
        self.LeaveDays = int(LeaveDays)


    def __eq__(self, other):
        if isinstance(other, Accruals):
            return self.__dict__ == other.__dict__
        return False



    """This function calculates the employee's daily salary"""
    def CalculateDailySalary(self):

        Monthly = 30

        if self.WorkedDays == Monthly:
            DailySalary = self.BasicSalary / self.WorkedDays
        
        else:
            DailySalary = (self.BasicSalary / Monthly)

        return DailySalary
    
    """This function calculates the employee's total salary based on days worked."""
    def CalculateTotalSalary(self):
        DailySalary = self.CalculateDailySalary()

        TwoLegalMinimumSalaries = 2600000
        
        TransportSubsidyValue = 162000

        TotalSalary = DailySalary * self.WorkedDays

        if self.BasicSalary <= TwoLegalMinimumSalaries:
            TotalSalary += TransportSubsidyValue
        
        else:
            TotalSalary = TotalSalary

        return TotalSalary
    
    """This function evaluates whether the base salary applies to the transportation subsidy"""
    def CalculateSubsidyTransport(self):
        TwoLegalMinimumSalaries = 2600000

        if self.BasicSalary <= TwoLegalMinimumSalaries:
            return "Your base salary applies for the transportation subsidy which is 162,000"
        else:
            return "Your base salary does not apply to the transportation subsidy"

    """This function calculates the surcharge value of a worked holiday."""
    def CalculateValueOfHolidaysWorked(self, DailySalary):
        """The surcharge for holiday hours worked according to the law is 75%."""
        HolidaySurchargePercentage = 0.75

        HolidayRecharge = (DailySalary * HolidaySurchargePercentage) * self.HolidayTimeWorked
        return HolidayRecharge

    """This function calculates the surcharge value of daylight extra hours worked."""
    def CalculateDaylightExtraHoursCharge(self):
        """The value for a daylight hour worked according to the law is 6915COP."""
        DaylightHourSurcharge = 6915

        DaylightSurchargeValue = DaylightHourSurcharge * self.ExtraDaylightHoursWorked
        return DaylightSurchargeValue

    """This function calculates the surcharge value of night extra hours worked."""
    def CalculateExtraNightHoursCharge(self):
        """The surcharge for night hours worked according to the law is 9681COP."""
        NightHourSurcharge = 9681

        NightSurchargeValue = NightHourSurcharge * self.ExtraNightHoursWorked
        return NightSurchargeValue
    
    """This function calculates the value of daylight extra hours on worked holidays."""
    def CalculateHolidayExtraDaylightHoursWorkedValue(self):

        """The surcharge for a holiday extra daylight hour worked according to the law is 11064COP."""
        HolidayExtraDaylightHoursWorkedSurcharge = 11064
        HolidayExtraDaylightHoursWorkedSurchargeValue = HolidayExtraDaylightHoursWorkedSurcharge * self.HolidayExtraDaylightHoursWorked
        
        return HolidayExtraDaylightHoursWorkedSurchargeValue

    """This function calculates the value of night extra hours on worked holidays."""
    def CalculateHolidayExtraNightHoursWorkedValue(self):

        """The surcharge for a holiday extra night hour worked according to the law is 13830COP."""
        HolidayExtraNightHoursWorkedSurcharge = 13830
        HolidayExtraNightHoursWorkedSurchargeValue = HolidayExtraNightHoursWorkedSurcharge * self.HolidayExtraNightHoursWorked
        
        return HolidayExtraNightHoursWorkedSurchargeValue
    
    """This function calculates the value to be paid according to the days of disability."""
    def CalculateDisabilityTimeValue(self):

        """The surcharge of 0.6666 must be made to the daily salary per day of disability if these are in the range of 1 to 90 days."""
        Percentage1to90Days = 0.6666
        """The surcharge of 0.5 must be made to the daily salary per day of disability if these are in the range of 90 to 540 days."""
        Percentage90to540Days = 0.5
        
        if self.DaysOfDisability >= 1 and self.DaysOfDisability <= 90: 
            DaysOfDisabilityValue = Percentage1to90Days * self.CalculateDailySalary()
            TotalDisabilityValue = DaysOfDisabilityValue * self.DaysOfDisability

        elif self.DaysOfDisability > 90 and self.DaysOfDisability <= 540:
            DaysOfDisabilityValue = Percentage90to540Days * self.CalculateDailySalary()
            TotalDisabilityValue = DaysOfDisabilityValue * self.DaysOfDisability

        else:
            TotalDisabilityValue = 0

        return TotalDisabilityValue
    
    """This function calculates the value to be paid according to the days of leave."""
    def CalculateLeaveDaysValue(self):
        DailySalary = self.CalculateDailySalary()

        """The number of days for maternity leave is 126."""
        DaysOfMaternityLeave = 126
        """The number of days for paternity leave is 14."""
        DaysOfPaternityLeave = 14
        """The number of days per bereavement leave is 5."""
        DaysOfBereavementLeave = 5
        """The number of days per leave for the care of minor children is 10."""
        DaysOfCareForMinorChildrenLeave = 10

        if self.LeaveDays == 1:
            LeaveDaysValue = DailySalary * DaysOfMaternityLeave
        elif self.LeaveDays == 2:
            LeaveDaysValue = DailySalary * DaysOfPaternityLeave
        elif self.LeaveDays == 3:
            LeaveDaysValue = DailySalary * DaysOfBereavementLeave
        elif self.LeaveDays == 4:
            LeaveDaysValue = DailySalary * DaysOfCareForMinorChildrenLeave
        else:
            LeaveDaysValue = 0

        return LeaveDaysValue
    
    """This function calculates the total of accruals by adding the calculated value of each one above"""
    def calculate_total_accruals(self):
        total_accruals = 0
        total_accruals += self.CalculateTotalSalary()
        total_accruals += self.CalculateValueOfHolidaysWorked(self.CalculateDailySalary())
        total_accruals += self.CalculateDaylightExtraHoursCharge()
        total_accruals += self.CalculateExtraNightHoursCharge()
        total_accruals += self.CalculateHolidayExtraDaylightHoursWorkedValue()
        total_accruals += self.CalculateHolidayExtraNightHoursWorkedValue()
        total_accruals += self.CalculateDisabilityTimeValue()
        total_accruals += self.CalculateLeaveDaysValue()

        return total_accruals

"""Deductions are the discounts that are made at the time of paying the salary to the employees."""
class Deductions:

    def __init__(self,idnumber, accruals, HealthInsurancePercentage, PensionContributionPercentage,
                PensionSolidarityFundContributionPercentage):
        
        self.idnumber = int(idnumber)
        self.accruals = accruals
        self.HealthInsurancePercentage = float(HealthInsurancePercentage)
        self.PensionContributionPercentage = float(PensionContributionPercentage)
        self.PensionSolidarityFundContributionPercentage = float(PensionSolidarityFundContributionPercentage)

    """This function calculates the employee's health contribution percentage to be discounted."""
    def CalculateHealthInsurance(self):
        total_accruals = self.accruals.calculate_total_accruals()
        HealthInsuranceValue = total_accruals * (self.HealthInsurancePercentage/100)
        return HealthInsuranceValue

    """This function calculates the pension contribution percentage to be discounted."""
    def CalculatePensionContribution(self):
        total_accruals = self.accruals.calculate_total_accruals()
        PensionContributionValue = total_accruals* (self.PensionContributionPercentage/100)
        return PensionContributionValue
    
    """This function calculates the contribution percentage to the pension solidarity fund to be discounted."""
    def CalculatePensionSolidarityFundContribution(self):
        total_accruals = self.accruals.calculate_total_accruals()
        PensionSolidarityFundContributionValue = total_accruals * (self.PensionSolidarityFundContributionPercentage/100)
        return PensionSolidarityFundContributionValue
    
    """This function calculates the witholding tax percentage to be discounted."""
    def CalculateWithholdingTax(self):
        """The value of the current taxable value unit is 47065 according to the law."""
        ActualTaxableValueUnit = 47065   

        """We calculate the taxable base in Actual Taxable value unit"""
        """This function converts the basic salary to the Tax base"""
        TaxBase = self.accruals.BasicSalary / ActualTaxableValueUnit

        """The ranges for calculating the withholding tax are:
        from 0 to 95 with a marginal rate of 0%;
        from 95 to 150 with a marginal rate of 19%;
        from 150 to 360 with a marginal rate of 28%;
        from 360 to 640 with a marginal rate of 33%;
        from 640 to 945 with a marginal rate of 35%;
        from 945 to 2300 with a marginal rate of 37%;
        from 2300 and upwards with a marginal rate of 39%"""

        RangeTaxableValueUnit1 = 95  
        RangeTaxableValueUnit2 = 150
        RangeTaxableValueUnit3 = 360
        RangeTaxableValueUnit4 = 640
        RangeTaxableValueUnit5 = 945
        RangeTaxableValueUnit6 = 2300

        """Depending on the basic salary converted to uvt, the function determines the range in which the salary falls, applies the formula
        with its corresponding marginal rate and Taxable value unit aggregate."""
        """Withholding percentage comes from the range and the marginal rate"""
        """The constant is a Taxable value added to the formula for calculating the withholding tax"""

        if TaxBase > RangeTaxableValueUnit1 and TaxBase < RangeTaxableValueUnit2:
            WithholdingPercentage = 0.19
            WithholdingTax = (TaxBase - RangeTaxableValueUnit1) * WithholdingPercentage

        elif TaxBase > RangeTaxableValueUnit2 and TaxBase < RangeTaxableValueUnit3:
            WithholdingPercentage = 0.28
            TaxValueUnitinRange = 10
            WithholdingTax = (TaxBase - RangeTaxableValueUnit2) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit3 and TaxBase < RangeTaxableValueUnit4:
            WithholdingPercentage = 0.33
            TaxValueUnitinRange = 69
            WithholdingTax = (TaxBase - RangeTaxableValueUnit3) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit4 and TaxBase < RangeTaxableValueUnit5:
            WithholdingPercentage = 0.35
            TaxValueUnitinRange = 162
            WithholdingTax = (TaxBase - RangeTaxableValueUnit4) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit5 and TaxBase < RangeTaxableValueUnit6:
            WithholdingPercentage = 0.37
            TaxValueUnitinRange = 268
            WithholdingTax = (TaxBase - RangeTaxableValueUnit5) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit6:
            WithholdingPercentage = 0.39
            TaxValueUnitinRange = 770
            WithholdingTax = (TaxBase - RangeTaxableValueUnit6) * WithholdingPercentage + TaxValueUnitinRange
        
        else:
            WithholdingTax = 0

        """Withholding tax is converted to pesos"""
        WithholdingCOP = WithholdingTax * ActualTaxableValueUnit

        return WithholdingCOP
    
    """This function calculates the total of deductions by adding the calculated value of each one above"""
    def calculate_total_deductions(self):
        total_deductions = 0
        total_deductions += self.CalculateHealthInsurance()
        total_deductions += self.CalculatePensionContribution()
        total_deductions += self.CalculatePensionSolidarityFundContribution()
        total_deductions += self.CalculateWithholdingTax()
        return total_deductions

class SalaryCalculator:

    def __init__(self, accruals, deductions):
        self.accruals = accruals
        self.deductions = deductions

    def __str__(self):
        net_salary = self.calculate_net_salary()
        return f"{net_salary}"

    """This function calculates the total payment by subtracting the total deductions from the total accruals."""
    def calculate_net_salary(self):
        total_accruals = self.accruals.calculate_total_accruals()
        total_deductions = self.deductions.calculate_total_deductions()

        net_salary = total_accruals - total_deductions

        return net_salary

class NegativeSalary(Exception):
    pass

def VerifyNegativeSalary(BasicSalary):
    """This function evaluates an error case where basic salary is negative."""
    if BasicSalary < 0:
        raise NegativeSalary("The basic salary cannot be negative.")

class IllegalParameters(Exception):
    pass

def VerifyNegativeWorkedDays(WorkedDays):
    """This function evaluates an error case where worked days are negative."""
    if WorkedDays < 0:
        raise IllegalParameters("The number of worked days cannot be negative.")
    
def VerifyNonZeroWorkedDays(WorkedDays):
    """This function evaluates an error case where worked days are equal to zero."""
    if WorkedDays == 0:
        raise IllegalParameters("The number of worked days cannot be zero.")

def VerifyNegativeDisabilityDays(DaysOfDisability):
    """This function evaluates an error case where the number of disability days is negative"""
    if DaysOfDisability < 0:
        raise IllegalParameters("The number of disability days cannot be negative.")
    
class DataTypeError(Exception):
    pass

def VerifyBasicSalaryDataTypeError(**kwargs):
    """This function verifies that BasicSalary value is numeric."""
    for key, value in kwargs.items():
        if key == 'BasicSalary':
            if isinstance(value, str):
                raise DataTypeError("BasicSalary must be a number, not a string.")
        elif not isinstance(value, (int, float)):
            raise DataTypeError("All input values must be numbers.")
        
def VerifyWorkedDaysDataTypeError(**kwargs):
    """This function verifies that WorkedDays value is numeric."""
    for key, value in kwargs.items():
        if key == 'WorkedDays':
            if isinstance(value, str):
                raise DataTypeError("WorkedDays must be a number, not a string.")
        elif not isinstance(value, (int, float)):
            raise DataTypeError("All input values must be numbers.")
        
class DataSizeLimitExceeded(Exception):
    pass

def VerifyLimitOfExtraDaylightHoursWorked(ExtraDaylightHoursWorked):
    """This function verifies that the number of extra daylight hours worked doesn't exceed 60."""
    if ExtraDaylightHoursWorked > 60:
        raise DataSizeLimitExceeded("The number of extra daylight hours worked cannot exceed 60.")
    
def VerifyLimitOfExtraNightHoursWorked(ExtraDayNightHoursWorked):
    """This function verifies that the number of extra night hours worked doesn't exceed 60."""
    if ExtraDayNightHoursWorked > 60:
        raise DataSizeLimitExceeded("The number of extra daylight hours worked cannot exceed 60.")

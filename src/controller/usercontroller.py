import psycopg2
import sys
sys.path.append("src")
import controller.SecretConfig as SecretConfig
from model.Payroll_Logic import *

class ErrorNotfound( Exception ):
    """Exception indicating that a searched row was not found"""
    pass

class RepeatedUser(Exception):
    pass



def Insert(employee: Employee):
    try:
        cursor = GetCursor()
        cursor.execute(
            "INSERT INTO employees (firstname, surname, idnumber, mail) VALUES (%s, %s, %s, %s)", 
            (employee.firstname, employee.surname, employee.idnumber, employee.mail)
        )
        cursor.connection.commit()
    except Exception as e:
        cursor.connection.rollback()
        if "duplicate" in str(e).lower(): 
            raise RepeatedUser(f"Id repeated. It was not possible to add the employee: {employee.idnumber}")
        else:
            raise
    finally:
        cursor.close()

def SearchById(idnumber):
    cursor = GetCursor()
    consulta = f"""SELECT firstname, surname, idnumber, mail
                    FROM employees WHERE idnumber = '{idnumber}' """
    cursor.execute(consulta)
    result = cursor.fetchone()

    if result is not None:
        return Employee(result[0], result[1], result[2], result[3])
    else:
        return None

class UpdateError(Exception):
    pass

def Update(employee: Employee):
    cursor = GetCursor()
    try:
        cursor.execute(f"""
            UPDATE employees
            SET 
                firstname='{employee.firstname}',
                surname='{employee.surname}',
                mail='{employee.mail}'
            WHERE idnumber='{employee.idnumber}'
        """)
        if cursor.rowcount == 0:
            raise UpdateError(f"Failed to update employee with id {employee.idnumber}: Employee does not exist")
        cursor.connection.commit()
    except Exception as e:
        cursor.connection.rollback()
        raise UpdateError(f"Failed to update employee with id {employee.idnumber}: {str(e)}")

    
class DeleteError(Exception):
    pass

def DeleteById(employee):
    sql = f"DELETE FROM employees WHERE idnumber = '{employee.idnumber}'"
    cursor = GetCursor()
    try:
        cursor.execute(sql)
        cursor.connection.commit()
        if cursor.rowcount == 0:
            raise DeleteError(f"Failed to delete employee with id {employee.idnumber}: Not found.")
    except Exception as e:
        cursor.connection.rollback()
        raise DeleteError(f"Failed to delete employee with id {employee.idnumber}: {str(e)}")

class UserNotFoundError(Exception):
    pass

def SearchByNameAndSurname(firstname, surname):
    cursor = GetCursor()
    consulta = f"""SELECT firstname, surname, idnumber, mail
                FROM employees WHERE firstname = '{firstname}' AND surname = '{surname}'"""
    cursor.execute(consulta)

    result = cursor.fetchone()

    if result is not None:
        return Employee(result[0], result[1], result[2], result[3])
    else:
        raise UserNotFoundError(f"User with name {firstname} {surname} not found.")



class RepeatedPrimarykey(Exception):
    pass

    def primary_key(firstname, idnumber, module):
        value = module.QueryWorker(firstname, idnumber)
        if value is not None:
            raise RepeatedPrimarykey("This user already exists: {} - {}".format(firstname, idnumber))
        
def GetCursor( ) :
    connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
    return connection.cursor()


def CreateTable():
    try:
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                    password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        cursor.execute("""create table employees (
            firstname text not null,
            surname text not null,
            idnumber varchar( 20 ) PRIMARY KEY NOT NULL,
            mail text
            );""")
        connection.commit()
        print("Table 'employees' created successfully.")
    except Exception as e:
        print(f"Error creating table 'employees': {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def CreateAccrualsTable():
    try:
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                    password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        cursor.execute("""create table accruals (
                        idnumber varchar( 20 ) PRIMARY KEY NOT NULL,
                        BasicSalary varchar( 20 ) not null,
                        WorkedDays varchar( 20 ) not null,
                        HolidayTimeWorked varchar( 20 ) not null,
                        ExtraDaylightHoursWorked varchar( 20 ) not null,
                        ExtraNightHoursWorked varchar( 20 ) not null,
                        HolidayExtraDaylightHoursWorked varchar( 20 ) not null,
                        HolidayExtraNightHoursWorked varchar( 20 ) not null,
                        DaysOfDisability varchar( 20 ) not null,
                        LeaveDays varchar( 20 ) not null                    
            );""")
        connection.commit()
    except Exception as e:
        print(f"Error creating table 'Deductions': {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def CreateTableDeductions():
    try:
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                    password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        cursor.execute("""create table Deductions (
            idnumber varchar( 20 ) PRIMARY KEY NOT NULL,
            HealthInsurancePercentage varchar( 5 ) NOT NULL,
            PensionContributionPercentage varchar( 5 ) NOT NULL,
            PensionSolidarityFundContributionPercentage varchar( 5 ) NOT NULL
            );""")
        connection.commit()
        print("Table 'Deductions' created successfully.")
    except Exception as e:
        print(f"Error creating table 'Deductions': {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def DeleteTable():

    sql = "drop table employees;"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()

def DeleteTableAccruals():

    sql = "drop table accruals;"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()

def DeleteTableDeductions():

    sql = "drop table deductions;"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()

def Deletelines():

    """Danger!"""
    sql = "delete from employees;"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()

    
def SearchInAllTablesByID(idnumber):
    cursor = GetCursor()
    consulta = f"""
    SELECT e.firstname, e.surname, e.idnumber, e.mail, 
           a.BasicSalary, a.WorkedDays, a.HolidayTimeWorked, a.ExtraDaylightHoursWorked, a.ExtraNightHoursWorked,
           a.HolidayExtraDaylightHoursWorked, a.HolidayExtraNightHoursWorked, a.DaysOfDisability, a.LeaveDays, 
           d.HealthInsurancePercentage, d.PensionContributionPercentage, d.PensionSolidarityFundContributionPercentage
    FROM employees e
    JOIN accruals a ON e.idnumber = a.idnumber
    JOIN deductions d ON e.idnumber = d.idnumber
    WHERE e.idnumber = '{idnumber}'
    """
    
    
    cursor.execute(consulta)
    result = cursor.fetchone()
    

    if result is not None:
        employee = Employee(result[0], result[1], result[2], result[3])
        accruals = Accruals(result[2], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12])
        deductions = Deductions(result[2], accruals, result[13], result[14], result[15])
        return (employee, accruals, deductions)
    else:
        raise ErrorNotfound("Employee not found")

    

def SearchAccrualsById(idnumber):

    cursor = GetCursor()
    consulta = f"""SELECT idnumber, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked,
                ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked,
                HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays
                from accruals where idnumber = '{idnumber}' """
    cursor.execute(consulta)

    result = cursor.fetchone()

    if result is not None:
        return Accruals(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9])
    else:
        raise ErrorNotfound("Accruals not found")


    
def InsertAccruals(accruals: Accruals):
    """ Save an user in the database """


    cursor = GetCursor()
    cursor.execute(f"""insert into accruals (
        idnumber, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked,
        HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays               
    )
    values 
    (
        '{accruals.idnumber}','{accruals.BasicSalary}',  '{accruals.WorkedDays}', '{accruals.HolidayTimeWorked}', '{accruals.ExtraDaylightHoursWorked}',
        '{accruals.ExtraNightHoursWorked}',  '{accruals.ExtraDaylightHoursWorked}',
        '{accruals.HolidayExtraNightHoursWorked}', '{accruals.DaysOfDisability}', '{accruals.LeaveDays}'
    );
                    """)
    cursor.connection.commit()


def InsertDeductions( deductions:Deductions):
    """ Guarda un Usuario en la base de datos """
    cursor = GetCursor()
    cursor.execute(f"""insert into deductions (idnumber, HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage          
    )
    values 
    (
        '{deductions.idnumber}','{deductions.HealthInsurancePercentage}',  '{deductions.PensionContributionPercentage}',
        '{deductions.PensionSolidarityFundContributionPercentage}'
    );
    """)
    cursor.connection.commit()

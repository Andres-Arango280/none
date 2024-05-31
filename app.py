from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append("src")
from model.Payroll_Logic import Employee, Accruals, Deductions, SalaryCalculator
from controller.usercontroller import Insert, InsertAccruals, InsertDeductions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    firstname = request.form.get('firstname')
    surname = request.form.get('surname')
    idnumber = request.form.get('idnumber')
    mail = request.form.get('mail')
    basicsalary = float(request.form['basicsalary'])
    workeddays = int(request.form['workeddays'])
    holidaytimeworked = int(request.form['holidaytimeworked'])
    extradaylighthoursworked = int(request.form['extradaylighthoursworked'])
    extranighthoursworked = int(request.form['extranighthoursworked'])
    holidayextradaylighthoursworked = int(request.form['holidayextradaylighthoursworked'])
    holidayextranighthoursworked = int(request.form['holidayextranighthoursworked'])
    daysofdisability = int(request.form['daysofdisability'])
    leavedays = int(request.form['leavedays'])
    healthinsurancepercentage = float(request.form['healthinsurancepercentage'])
    pensioncontributionpercentage = float(request.form['pensioncontributionpercentage'])
    pensionsolidarityfundcontributionpercentage = float(request.form['pensionsolidarityfundcontributionpercentage'])

    employee = Employee(firstname, surname, idnumber, mail)
    accruals = Accruals(idnumber, basicsalary, workeddays, holidaytimeworked, extradaylighthoursworked, extranighthoursworked, holidayextradaylighthoursworked, holidayextranighthoursworked, daysofdisability, leavedays)
    deductions = Deductions(idnumber, accruals, healthinsurancepercentage, pensioncontributionpercentage, pensionsolidarityfundcontributionpercentage)

    try:
        Insert(employee)
        InsertAccruals(accruals)
        InsertDeductions(deductions)
        return redirect(url_for('result', idnumber=idnumber))
    except Exception as e:
        return f"Error inserting information: {e}"

@app.route('/buscar_usuario', methods=['GET'])
def buscar_usuario():
    return render_template('BuscarUsuario.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/search_user', methods=['GET', 'POST'])
def search_user():
    if request.method == 'POST':
        search_by = request.form.get('search_by')
        if not search_by:
            return "El campo 'search_by' es requerido"

        if search_by == 'idnumber':
            idnumber = request.form.get('idnumber')
            try:
                employee_details = GetEmployeeDetails(idnumber)
                return render_template('result.html', employee_details=employee_details)
            except Exception as e:
                return f"Error retrieving information: {e}"
        elif search_by == 'name':
            firstname = request.form.get('firstname')
            surname = request.form.get('surname')
            try:
                employee_details = GetEmployeeDetailsByName(firstname, surname)
                return render_template('result.html', employee_details=employee_details)
            except Exception as e:
                return f"Error retrieving information: {e}"
        else:
            return "Valor de 'search_by' inválido"
    return render_template('BuscarUsuario.html')

@app.route('/result/<idnumber>', methods=['GET'])
def result(idnumber):
    try:
        employee_details = GetEmployeeDetails(idnumber)
        return render_template('result.html', employee_details=employee_details)
    except Exception as e:
        return f"Error retrieving information: {e}"

@app.route('/result_by_name')
def result_by_name():
    firstname = request.args.get('firstname')
    surname = request.args.get('surname')
    try:
        employee_details = GetEmployeeDetailsByName(firstname, surname)
        return render_template('result.html', employee_details=employee_details)
    except Exception as e:
        return f"Error retrieving information: {e}"

def GetEmployeeDetails(idnumber):
    employee = Employee(idnumber)
    if not employee:
        raise ValueError(f"Employee not found with ID: {idnumber}")

    accruals = Accruals(idnumber)
    deductions = Deductions(idnumber)

    if not accruals or not deductions:
        raise ValueError(f"Accruals or deductions not found for employee with ID: {idnumber}")

    salary_calculator = SalaryCalculator(accruals, deductions)
    net_salary = salary_calculator.calculate_net_salary()

    employee_details = {
        'employee': employee,
        'net_salary': net_salary
    }

    return employee_details

def GetEmployeeDetailsByName(firstname, surname):
    employee = Employee(firstname, surname)
    if not employee:
        raise ValueError(f"Employee not found with name: {firstname} {surname}")

    idnumber = employee.idnumber
    accruals = Accruals(idnumber)
    deductions = Deductions(idnumber)

    if not accruals or not deductions:
        raise ValueError(f"Accruals or deductions not found for employee with name: {firstname} {surname}")

    salary_calculator = SalaryCalculator(accruals, deductions)
    net_salary = salary_calculator.calculate_net_salary()

    employee_details = {
        'employee': employee,
        'net_salary': net_salary
    }

    return employee_details

if __name__ == '__main__':
    app.run(debug=True)


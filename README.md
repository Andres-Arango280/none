# PayrollPayment

## List of authors:

- Angie Norela Diaz Abaunza
- Mateo Molina Alvarez

## What is it?

Payroll accounting is the process by which the employer calculates the value to be paid to its employees. 

In essence, the key aspects of payroll settlement are:

- Payments: These are the items that add to the employee's salary. They include the base salary, transportation allowance, time worked (week, month, year, etc.),  holiday time worked, daytime overtime, nighttime overtime and holiday overtime worked.

- Deductions: These are the deductions that are applied to the gross salary to obtain the net salary. Some common deductions are the percentage health contribution percentage, pension contribution percentage, pension solidarity fund contribution percentage, disability time and leave time.

## What for?

This program is designed to automate the calculations performed in the payroll process by determining the accrued values for the days worked and the deductions that are applied to the employee's salary in a specific period of time depending on the case, with the objective of obtaining a total value to be paid. In addition, it seeks to ensure accuracy and consistency in the process, thus minimizing human errors and speeding up the process of  payroll settlement process.

## Prerequisites for using the program: 

## Prerequisites:

Make sure you have a PostgreSQL database and its respective access data

Psycopg is a PostgreSQL adapter for the Python programming language. It is a wrapper for the libpq, the official PostgreSQL client library

Quick install:
For most operating systems, the quickest way to install Psycopg is using the wheel package available on PyPI:

$ pip install psycopg2-binary

This will install a pre-compiled binary version of the module which does not require the build or runtime prerequisites described below. Make sure to use an up-to-date version of pip (you can upgrade it using something like pip install -U pip).

You may then import the psycopg2 package, as usual:

"""
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM my_data")

# Retrieve query results
records = cur.fetchall()
"""

## Connection to DataBase:

Copy the file SecretConfig-sample.py as SecretConfig.py and set the connection data to your database in this file.

In the SecretConfig-Sample file you will find the data required to connect to the database, this data can be found in the Dashboard of your database

## How to use it?

This application requires the creation of three essential tables: employees, earnings, and deductions. The tables can be created through the console. Employee information will be linked by their ID. The tables can be modified, deleted, and information can be inserted into them. Additionally, it allows for querying and calculating payroll settlements for users in the database.

To create a table, go to the "view" folder and the "create_table" file. To insert information into the table, go to the "create_user" file. For queries in the database, navigate to the "search_user" file. And to update or modify information, go to the "modify_info" file.

### Python Installed:

1. Open your web browser and go to the official [Python](https://www.python.org/) site.

2. On the home page, you will see a download button in the center area of the screen. This button usually displays the 
most recent version of Python available for download.

3. Click the download button to access the download page.

4. On the download page, you will see several versions of Python available for download. The recommended version is the most recent one, 
as it will include the latest features and security updates.

5. Select the version of Python you want to install. Typically, you will see options for Windows, macOS and Linux operating systems. 
Linux operating systems. Click on the version that corresponds to your operating system.

6. Once you have selected the version and operating system, the Python installer download will start.
Once the download is complete, find the downloaded file on your computer and open it.

7. Follow the instructions in the installer to complete the installation process. Generally, this involves 
accepting the terms of use, selecting the installation location and clicking "Install".

8. After completing the installation, it is advisable to verify that Python has been properly installed on your system.
Open the terminal or command prompt on your operating system.

Type the following command and press Enter:

css
Copy code
python --version

This should display the version of Python you have installed on your system. If you see a message indicating the version of Python, 
it means the installation was successful.

### Development environment or text editor installed: 

You will need an integrated development environment (IDE) or text editor to write, edit and run your Python code. Some options are: 

- PyCharm(preferably): Developed by JetBrains, PyCharm is a popular choice among Python developers. It offers advanced features 
such as automatic code completion, refactoring, integration with version control tools and more. In the following link you will find
a detailed guide to install it (https://www.jetbrains.com/help/pycharm/installation-guide.html#toolbox)

- Visual Studio Code: Developed by Microsoft, Visual Studio Code (VS Code) has gained popularity among Python developers due to its performance, flexibility and wide range of features, its performance, flexibility and wide range of available extensions. In the following link you will find a detailed guide to install it: (https://mundowin.com/guia-para-instalar-y-configurar-visual-studio-code/)

### Python Libraries Required: 

You need to install the necessary Python libraries to use the program, in this case make sure to install the Unittest library using pip, the Python package manager. You can install the library by running the following command at your terminal or command prompt:

pip install unittest

### Input data:

The program will need input data to calculate payroll. This may include information such as base salary, transportation allowance, time worked (week, fortnight, decade, other), holiday time worked, daytime overtime, nighttime overtime and holiday overtime worked, health contribution, percentage of pension contribution, percentage of contribution to the pension solidarity fund, time of incapacity and time of leaves of absence.

## How is this project made?

**Components and Modules:** 

1. PayrollConsole: This module is responsible for managing the user interface through an interactive console. It provides the user a means to interact with the system, entering data and receiving results in an intuitive and friendly way.

2. PayrollLogic: Here lies the essence of the code, where all the logic and algorithms necessary to perform the relevant calculations are located. From the processing of input data to the generation of results, this module is in charge of executing all the necessary operations for payroll in an accurate and efficient manner.

3. PayrollTests: This module is dedicated exclusively to unit testing of the system. It includes test cases to validate the behavior of the code in various situations, such as error scenarios, exceptional cases and normal situations. These tests ensure the robustness and reliability of the system.

**Library used: unittest

It is a Python standard library module that provides a framework for writing and running unit tests. 
Unit testing is a software development technique in which individual units of code, such as functions, methods or classes, are checked for correct operation, individual units of code, such as functions, methods or classes.

1. **Test Structure:** unittest allows you to define test suites by creating test classes that inherit from the unittest.TestC class. 
from the unittest.TestCase class. Within these classes, test methods are functions that verify the behavior of a specific unit of code.

2. **Assertions:** unittest provides a variety of assertion methods (assertions) that allow you to verify conditions during test execution. 
These methods include assertEqual, assertTrue, assertFalse, assertRaises, among others, which are used to verify the equality, truth or falsity of certain conditions.

3. **Test Fixture:** unittest supports the use of setup and cleanup methods (setUp and tearDown) that are executed before and after each test method. These methods are used to configure the test environment and perform cleanup tasks after the execution of each test.

4. **Automatic Test Discovery and Execution:** unittest provides the ability to automatically discover and execute all tests defined in a project. 
This facilitates the execution of all tests efficiently and automatically, which helps ensure code integrity during development.

5. **Integration with Other Tools:** unittest can be integrated with other development tools and continuous integration systems to facilitate automated test execution as part of the development process. In addition, it can be used in combination with third-party testing frameworks to extend its functionality and facilitate the writing of more complex tests


## Instructions to run 
- To execute the graphic interface elaborated with kivy, you must open the file in an interpreter and run it from the module "src" where the GUI (Graphic user interface) folder is located, which contains "payrollgui", which is where the interface is executed.
  
**To run the console**
  
- Open the terminal on your computer
- In the terminal use the command cd to enter the desktop; "cd Desktop" (it depends on the name of your desktop or what path you have to get to it).
- Use the same command to enter the application "cd Payroll-main".
- Use the same command to enter the src folder, which is where the folders with the files necessary for the application to work are organized "cd src".
- then copy the path you have so far in the terminal and then type the command set PYTHONPATH= here is the path you copied, example set PYTHONPATH=C:\ruta=C:\ruta=Desktop "Payroll-main".
- use the cd command to enter the console folder which is where the "cd console" menu is located.
- Then use the command "python Payroll_Console.py".
**A menu will appear and you'll type the information needed.

**To run the tests**

- Open the terminal on your computer
- In the terminal use the command cd to enter the desktop; "cd Desktop" (it depends on the name of your desktop or what path you have to get to it).
- Use the same command to enter the application "cd Payroll-main".
- Use the same command to enter the tests folder, which is where the folders with the files necessary for the application to work are organized "cd tests".
- then copy the path you have so far in the terminal and then type the command set PYTHONPATH= here is the path you copied, example set PYTHONPATH=C:\ruta=Desktop "Payroll-main".
- Then use the command "python test_unittest.py".
**A menu will appear and you'll type the information needed.



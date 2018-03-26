# EmployeeWorkLogManagement
An app to manage the employee work hours log like checked-in, break, lunch, checked-out
### Project Working Demo
- [Video Link]() to be updated soon
- [Working Demo Files](https://github.com/vivekVells/EmployeeWorkTimeLogManagement/tree/master/demo) - click the .pdf file
### Objective
- To maintain a working time log of all the employees (this will be useful to run the payroll since the working hours of each employee is recorded)
### Tech Involved 
- Frontend languages, Python, Django, sqllite3, Bootstrap
### Versions
- Python: 3.6.2 || Django: 2.0.3
### Features
- Register an Employee of a particular department
- Log working hours
- Retrieve the working hours log report via Mail, Document, PDF, Image
### Concepts I Newly Learnt & Practiced
- Django, Bootstrap v3.3.7
### Future Code
- Enhancement tweaks
### Instructions to run this code in your machine:
#### In console (Tested in Windows using GitBash cmd) - follow the steps
- Step 1: Make sure Python setup is available in your machine (coded when python was on version 3.6.2) & do django version as 2.0.3
- Step 2: Open console command prompt or gitbash (I love git bash. Try this one)
- Step 3: Pull this code to your machine and run it (Install git and use git bash for the followings) (you could also do git clone and proceed from Step 3.4)
  - Step 3.1: Create a folder and do 
    - **git init**
  - Step 3.2: Add this repo as your remote origin 
    - **git remote add origin https://github.com/vivekVells/EmployeeWorkTimeLogManagement**
  - Step 3.3: Pull the code in this repo to your remote origin 
    - **git pull origin master**   
  - Step 3.4: Move to the directory 'emptimeclklogmgmt'
    - **Vivek-Pc@kev MINGW64 /e/kevDev/ProjectWorks/EmployeeWorkTimeLogManagement (master)**
      $ cd emptimelogmgmt/      
  - Step 3.5: Make migrations and migrate
    - **Vivek-Pc@kev MINGW64 /e/kevDev/ProjectWorks/EmployeeWorkTimeLogManagement/emptimelogmgmt (master)**
      $ python manage.py makemigrations emptimeclklogmgmt
      **Vivek-Pc@kev MINGW64 /e/kevDev/ProjectWorks/EmployeeWorkTimeLogManagement/emptimelogmgmt (master)**
      $ python manage.py migrate --run-syncdb
  - Step 3.6: Run the server and goto port link: http://127.0.0.1:8000/
    - **Vivek-Pc@kev MINGW64 /e/kevDev/ProjectWorks/EmployeeWorkTimeLogManagement/emptimelogmgmt (master)**
      $ python manage.py runserver
- Step 4: In 'Login Page', click 'Register User' and register the user
- Step 5: In 'New Registration Page', create the user
- Step 6: In 'Login Page', input the login credentials and toto 'Time Clock Home Page' and log your working hours 

## App Working Functionality Previews
### Preview 
![](https://github.com/vivekVells/EmployeeWorkTimeLogManagement/blob/master/demo/Employee%20Time%20Clock%20Mgmt%20-%20Working%20GIF%20v1.0.gif)
### Images
Login Page![](https://github.com/vivekVells/EmployeeWorkTimeLogManagement/blob/master/memories/v1.1%20-%20Login%20Page.png)
Home Page![](https://github.com/vivekVells/EmployeeWorkTimeLogManagement/blob/master/memories/v1.1%20-%20Home%20Page.png)
Registration Page![](https://github.com/vivekVells/EmployeeWorkTimeLogManagement/blob/master/memories/v1.0%20-%20Registration%20Page.png)

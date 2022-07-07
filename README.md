# dummy_fast_apis
This project is to demonstrate the fast api knowledge

This project will show, add and delete employee details.

Employee details will be stored in a dictionary and it will be stored till server runs.

<h3>Setup Steps</h3>
- Create Virtual Environment by running following command
  - <code>python -m venv venv</code>
- Activate it
  - <code>source venv/bin/activate</code>
- Run requirements.txt file to install packages
  - <code>pip install -r requirements.txt</code>
- Run server using uvicorn and mark reload option to apply code changes dynamically
  - <code>uvicorn main:app --reload</code>
- Use the swagger page by using following link
  - <code>https://127.0.0.1:8000/doc</code>
  - <b>Note</b>: By default localhost (127.0.0.1) is the host and 8000 is the port

<h3>End Points</h3>
- GET    (/v1/emps/list)
  - This will list all the employees.
- GET    (/v1/emps/<emp_id: int>)
  - This will give details of employee with provided id.
- POST   (/v1/emps/new)
  - This will create new employee with provided details in json format.
- DELETE (/v1/emps/<emp_id: int>)
  - This will delete the employee with provided id.
  - This will do the hard delete.

<h3>Code Validation</h3>
Black and flake8 have been used for code validation.
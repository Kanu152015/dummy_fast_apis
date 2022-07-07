# dummy_fast_apis
This project is to demonstrate the fast api knowledge

This project will show, add and delete employee details.

Employee details will be stored in a dictionary and it will be stored till server runs.

<h3>Setup Steps</h3>
- Create Virtual Environment by running following command<br/>
  <code>python -m venv venv</code><br/>
- Activate it<br/>
  - <code>source venv/bin/activate</code><br/>
- Run requirements.txt file to install packages<br/>
  - <code>pip install -r requirements.txt</code><br/>
- Run server using uvicorn and mark reload option to apply code changes dynamically<br/>
  - <code>uvicorn main:app --reload</code><br/>
- Use the swagger page by using following link<br/>
  - <code>https://127.0.0.1:8000/doc</code><br/>
  - <b>Note</b>: By default localhost (127.0.0.1) is the host and 8000 is the port<br/><br/>

<h3>End Points</h3>
- GET    (/v1/emps/list)<br/>
  - This will list all the employees.<br/>
- GET    (/v1/emps/<emp_id: int>)<br/>
  - This will give details of employee with provided id.<br/>
- POST   (/v1/emps/new)<br/>
  - This will create new employee with provided details in json format.<br/>
- DELETE (/v1/emps/<emp_id: int>)<br/>
  - This will delete the employee with provided id.<br/>
  - This will do the hard delete.<br/>

<h3>Code Validation</h3>
Black and flake8 have been used for code validation.

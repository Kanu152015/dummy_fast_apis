# dummy_fast_apis
This project is to demonstrate the fast api knowledge

This project will show, add and delete employee details.

Employee details will be stored in a dictionary and it will be stored till server runs.

<h3>Setup Steps</h3>
- Create Virtual Environment by running following command<br/><br/>
<code>python -m venv venv</code><br/><br/>
- Activate it<br/><br/>
<code>source venv/bin/activate</code><br/><br/>
- Run requirements.txt file to install packages<br/><br/>
<code>pip install -r requirements.txt</code><br/><br/>
- Run server using uvicorn and mark reload option to apply code changes dynamically<br/><br/>
<code>uvicorn main:app --reload</code><br/><br/>
- Use the swagger page by using following link<br/><br/>
<code>https://127.0.0.1:8000/doc</code><br/><br/>
<b>Note</b>: By default localhost (127.0.0.1) is the host and 8000 is the port<br/><br/>

<h3>End Points</h3>
- GET    (/v1/emps/list)<br/><br/>
  - This will list all the employees.<br/><br/>
- GET    (/v1/emps/<emp_id: int>)<br/><br/>
  - This will give details of employee with provided id.<br/><br/>
- POST   (/v1/emps/new)<br/><br/>
  - This will create new employee with provided details in json format.<br/><br/>
- DELETE (/v1/emps/<emp_id: int>)<br/><br/>
  - This will delete the employee with provided id.<br/><br/>
  - This will do the hard delete.<br/><br/>

<h3>Code Validation</h3>
Black and flake8 have been used for code validation.

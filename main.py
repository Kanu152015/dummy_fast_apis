from fastapi import FastAPI
from src.details import emp_data


app = FastAPI()


@app.get("/v1/emps/list")
async def list_emps():
    return {"employees": emp_data}


@app.get("/v1/emps/{emp_id}")
async def get_emp_by_id(emp_id: int):
    if emp_id in emp_data:
        return {"employees": emp_data[emp_id]}
    else:
        return {"error_message": "Employee not found!"}


@app.post("/v1/emps/new")
async def create_new_emp(request):
    import json

    new_emp = json.loads(request)
    next_num = max(emp_data.keys()) + 1
    emp_data[next_num] = new_emp
    return {"message": "New emp details stored."}


@app.delete("/v1/emps/{emp_id}")
async def delete_emp_by_id(emp_id: int):
    if emp_id in emp_data:
        del emp_data[emp_id]
        return {"message": "Employee deleted successfully!"}
    else:
        return {"error_message": "Employee not found!"}

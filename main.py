from fastapi import FastAPI
from src.details import emp_data


app = FastAPI()


# @app.get("/greet")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.post("/greet")
# async def root():
#     return {"message": "Hello World with POST"}

@app.get("/v1/emps/list")
async def root():
    return {"employees": emp_data}


# @app.get("/v1/emps/{emp_id}")
# async def root(emp_id):
#     if emp_id.isdigit() and int(emp_id) in emp_data:
#         return {"employees": emp_data[int(emp_id)]}
#     else:
#         return {"error_message": "Employee not found!"}


@app.get("/v1/emps/{emp_id}")
async def root(emp_id: int):
    # return {"message": emp_id}
    if emp_id in emp_data:
        return {"employees": emp_data[emp_id]}
    else:
        return {"error_message": "Employee not found!"}


@app.post("/v1/emps/new")
async def root(request):
    # return {"message": request}
    import json
    new_emp = json.loads(request)
    next_num = max(emp_data.keys()) + 1
    emp_data[next_num] = new_emp
    return {"message": "New emp details stored."}


@app.delete("/v1/emps/{emp_id}")
async def root(emp_id: int):
    # return {"message": emp_id}
    if emp_id in emp_data:
        del emp_data[emp_id]
        return {"message": "Employee deleted successfully!"}
    else:
        return {"error_message": "Employee not found!"}

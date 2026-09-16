from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
#学会编写基础的接口
@app.get('/hello')
def say():
    return {"message":"This is my first API"}

@app.get('/me')
def myinfo():
    return {
        "School": "Hainan University",
        "Grade": 2025,
        "Major": "Computer"
    }

students = {
    1:{"name":"John", "major":"软件工程"},
    2:{"name":"Celine", "major":"化学"}
}

#路径参数：
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="未找到该学生"
        )#如何返回404
    return students[student_id]
    # if student_id in students:
    #     return students[student_id]
    # return "没有找到该学生"

@app.get("/square/{number}")
def get_square(number: int):
    return {
        "Number": number,
        "Square": number**2
    }

#查询参数
#路径参数通常指定“哪一个”，查询参数通常描述“按什么条件、怎么查”。
@app.get("/greet")
def greet(name:str = "同学"):
    return {"message": f"Hello, {name}!!!"}

@app.get("/add")
def add(a:int = 1, b:int = 2):
    return {
        "a":a,
        "b":b,
        "result": a+b
    }

@app.get("/rectangle")
def rectangle(width: float = 3.0, height: float = 4.0):
    return {
        "Width":width,
        "Height":height,
        "Result": width*height
    }

class StudentCreate(BaseModel):
    #继承了 Pydantic 的 BaseModel，因此具备数据解析和验证能力。你现在先理解为“一张规定填写内容的表格”。
    name : str
    age : int
    major : str = "软件工程"

@app.post("/students", status_code=201)#表示这个接口正常执行并返回结果时，响应的状态码为 201，含义是“创建成功”。
def studentcreate(student: StudentCreate):
    new_id = max(students, default=0) + 1

    students[new_id] = {
        "name": student.name,
        "age": student.age,
        "major": student.major
    }
    return {
        "id": new_id,
        **students[new_id]# **在这里表示把已有字典的键值对展开到新字典中。
    }

@app.put("/students/{student_id}")#还是需要通过requests进行调用
def updatestudent(student_id: int, student: StudentCreate):
    if student_id not in students:
        raise HTTPException(
                    status_code=404,
                    detail="未找到该学生"
                )
    students[student_id] = {
        "name": student.name,
        "age": student.age,
        "major":student.major
    }

    return {
        "id":student_id,
        **students[student_id]
    }
    

#使用delete删除学生
@app.delete("/students/{id}", status_code=201)
def deletestudent(id: int):
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="没有找到该学生"
        )
    del students[id]

    return {
        "message": "删除成功",
        "id": id
    }
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
app = FastAPI()
from data_base import get_connection
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
    # if student_id not in students:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="未找到该学生"
    #     )#如何返回404
    # return students[student_id]
    # # if student_id in students:
    # #     return students[student_id]
    # # return "没有找到该学生"
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('select id,name,major from students where id = %s', (student_id,))
            #%s 是参数占位符，具体值通过第二个参数交给驱动处理
            #(student_id,) 是一个只有一个元素的元组，末尾的逗号不能省略。
            student = cursor.fetchone()
    finally:
        conn.close()#无论查询成功还是中途出错，都执行关闭操作，避免连接一直占用资源。
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="未找到该学生的信息"
        )
    return student

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
def rectangle(width: float, height: float = 1):
    return {
        "Width":width,
        "Height":height,
        "Result": width*height
    }

class StudentCreate(BaseModel):
    #继承了 Pydantic 的 BaseModel，因此具备数据解析和验证能力。你现在先理解为“一张规定填写内容的表格”。
    name : str = Field(min_length=1, max_length=50)
    age : int = Field(ge=1, le=150)
    major : str = Field(
        default="软件工程",
        min_length=1,
        max_length=100
    )

@app.post("/students", status_code=201)#表示这个接口正常执行并返回结果时，响应的状态码为 201，含义是“创建成功”。
def studentcreate(student: StudentCreate):
    # new_id = max(students, default=0) + 1

    # students[new_id] = {
    #     "name": student.name,
    #     "age": student.age,
    #     "major": student.major
    # }
    # return {
    #     "id": new_id,
    #     **students[new_id]# **在这里表示把已有字典的键值对展开到新字典中。
    # }
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('insert into students (name, age, major) values (%s, %s, %s)',
                           (student.name, student.age, student.major))
            new_id = cursor.lastrowid
        conn.commit()#执行 INSERT 后，需要提交事务才能保存修改。
    except Exception:
        conn.rollback()
        raise
    
    finally:
        conn.close()

    return {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "major": student.major
    }
            

@app.put("/students/{student_id}")#还是需要通过requests进行调用
def updatestudent(student_id: int, student: StudentCreate):
    # if student_id not in students:
    #     raise HTTPException(
    #                 status_code=404,
    #                 detail="未找到该学生"
    #             )
    # students[student_id] = {
    #     "name": student.name,
    #     "age": student.age,
    #     "major":student.major
    # }

    # return {
    #     "id":student_id,
    #     **students[student_id]
    # }
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('select id from students where id = %s for update',
                           (student_id,))
            if cursor.fetchone() is None:
                raise HTTPException(
                    status_code=404,
                    detail="未找到该学生"
                )
            cursor.execute(
                """
                update students 
                set name = %s, age = %s, major = %s 
                where id = %s
                """,
                (student.name, 
                 student.age, 
                 student.major, 
                 student_id)
                )
            conn.commit()
    except Exception:
        conn.rollback()#撤销当前事务中尚未提交的修改。
        raise
    finally:
        conn.close()

    return {
        "id": student_id,
        "name": student.name,
        "age": student.age,
        "major": student.major
    }
    

#使用delete删除学生
@app.delete("/students/{id}", status_code=200)
def deletestudent(id: int):
    # if id not in students:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="没有找到该学生"
    #     )
    # del students[id]

    # return {
    #     "message": "删除成功",
    #     "id": id
    # }
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "delete from students where id = %s",
                (id,)
                        )
            if cursor.rowcount == 0:
                raise HTTPException(
                    status_code=404,
                    detail="未找到学生信息"
                )
            
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return {
        "id":id,
        "message": "删除成功"
    }
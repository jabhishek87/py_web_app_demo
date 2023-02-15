from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fakedb = []

class Course(BaseModel):
    id:int
    name:str
    price:float
    is_early_bird: Optional[bool] = None


@app.get("/")
def get_home():
    return {"message": "helloworld"}


@app.get("/courses")
def get_courses():
    return fakedb


@app.get("/courses/{course_id}")
def get_course(course_id:int):
    course = course_id - 1
    return fakedb[course]


@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/courses")
def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {"message": "deleted successfully"}
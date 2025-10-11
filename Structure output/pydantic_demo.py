from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    
    name : str = 'suman'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0,lt=10)  # constrants applied 

new_student = {'age': 21, 'email':'sumankumarpanditpur520@gmail.com'}

student = Student(**new_student)

print(student)
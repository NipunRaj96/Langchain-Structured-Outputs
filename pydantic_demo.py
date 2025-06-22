from pydantic import BaseModel , EmailStr , Field 
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int]=None #none is the default value which you have to provide 
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student={'name':'nipun' , 'email':'abc@gmail.com', 'cgpa':'5'}

student = Student(**new_student)

student_dict = dict(student)

student_json = student.model_dump_json()

print(student_dict['name'])
print(student)
from typing import TypedDict

class Person(TypedDict):
      name : str
      age : int


new_person : Person = {'name':'suman','age':21}

print(new_person)
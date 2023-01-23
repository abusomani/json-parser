import json
from collections import namedtuple
from json import JSONEncoder

class Student:
    def __init__(self, rollNumber, name, marks) -> None:
        self.rollNumber, self.name, self.marks = rollNumber, name, marks

    # Optional for interview
    def __repr__(self):
        return '{' + self.name + ', ' + str(self.rollNumber) + ', ' + str(self.marks) + '}'

class Marks:
    def __init__(self, english, maths) -> None:
        self.english, self.maths = english, maths

    # Optional for interview
    def __repr__(self):
        return '{' + str(self.english) + ', ' + str(self.maths) + '}'

class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())
marks1 = Marks(82, 74)
student1 = Student(10, "Emma", marks1)
studentJson = json.dumps(student1, indent=4, cls=StudentEncoder)
print(studentJson)
studObj = json.loads(studentJson, object_hook=customStudentDecoder)

marks2 = Marks(80, 70)
student2 = Student(2, "Mark", marks2)
students = [student1, student2]
students.sort(key=lambda x: x.marks.english, reverse=True)


class Employee:
  def __init__(self, id, first_name, last_name, dept, position, manager_id, level) -> None:
      self.id = id
      self.first_name = first_name
      self.last_name = last_name
      self.dept = dept
      self.position = position
      self.manager_id = manager_id
      self.level = level

  def __repr__(self):
    print(self.__dict__)
    return ''
  

class Employees:
  def __init__(self, employees) -> None:
      self.employees = employees

  def __str__(self):
    for emp in self.employees:
      print(emp.__dict__)
    return ''

  def get_level(self, employee):
    return employee.level

  def get_sorted_levels(self):
    self.employees.sort(key=self.get_level)
    print(self.employees)

class Reportees:
  def __init__(self, reportees) -> None:
      self.reportees = reportees


class Encoder(JSONEncoder):
  def default(self, o):
    return o.__dict__

def CustomDecoder(obj):
  return namedtuple('Employee', obj.keys())(*obj.values())


def all_employees_in_dept(dept, employees):
  return list(filter(lambda x: x.dept == dept,  employees))

def get_all_reportees(id, employees):
  return list(filter(lambda x: x.manager_id == id, employees))

def get_first_name(employee):
  return employee.first_name

def get_last_name(employee):
  return employee.last_name
  
def get_sorted_reportees_by_first_name(employees):
  employees.sort(key=get_first_name)
  return employees

  
def get_sorted_reportees_by_last_name(employees):
  employees.sort(key=get_last_name)
  return employees

brian = Employee(1, "Brian", "A", "Exec", "CEO", 1, 10)
emilie = Employee(2, "Emilie", "A", "Exec", "CPO", 1, 9)
max = Employee(3, "Max", "B", "Retail", "CTO", 2, 8)
pankaj = Employee(4, "Pankaj", "A", "Risk", "COO", 2, 8)

allEmps = Employees([brian, emilie, max, pankaj])
brianString = json.dumps(brian, cls=Encoder)
b  = json.loads(brianString, object_hook=CustomDecoder)
print(b)

# Sort the employees based on their levels
allEmps.get_sorted_levels()

# Filter the employee based on maximum number of immediate reports

# Sort the reportees of a manager according to first name
print(get_sorted_reportees_by_first_name(get_all_reportees(2, allEmps.employees)))

# Sort the reportees of a manager according to first name
print(get_sorted_reportees_by_last_name(get_all_reportees(2, allEmps.employees)))

# Return all the employees in a certain deparment
print(all_employees_in_dept("Exec", allEmps.employees))

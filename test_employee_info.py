import employee_info

def test_employee_age_range():
    correct_result=[{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result=employee_info.get_employees_by_age_range(39,50)
    assert (result==correct_result)
    
def test_average_salary():
    correct_result=60166.666666666664
    result=employee_info.calculate_average_salary()
    assert (result==correct_result)

def test_employee_by_dept():
    correct_result=[    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result=employee_info.get_employees_by_dept("Marketing")
    assert(result==correct_result)
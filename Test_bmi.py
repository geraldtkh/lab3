import lab2.bmi as bmi
def test_bmi_normal_weight():
    correct_result=0
    result=bmi.calculate_bmi(1.72,65)
    assert(correct_result==result)
def test_bmi_over_weight():
    correct_result=1
    result=bmi.calculate_bmi(1.5,75)
    assert(correct_result==result)
def test_bmi_under_weight():
    correct_result=-1
    result=bmi.calculate_bmi(1.75,50)
    assert(correct_result==result)
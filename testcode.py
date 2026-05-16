from abcd import calculate_marks
def checking_grades1():
    assert calculate_marks(67) == "Grade C"
def checking_grades2():
    assert calculate_marks(96) == "Grade A"
def checking_grades3():
    assert calculate_marks(82) == "Grade: B"
def checking_grades4():
    assert calculate_marks(44) == "Grade: Fail"
def checking_grades5():
    assert calculate_marks(99) == "Grade A"




print("Student Grade Calculator")
print("------------------------")

name = input("Enter Your Name")
marks = int(input("Enter Marks"))

print("Students Name:", name)
print("Marks:", marks)

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
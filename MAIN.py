# x=int(input("enter the value of x :"))
# y=int(input("enter the value of y :"))
#
# TOTAL=x+y
# file =open('user.txt','a')
# file.write(str(TOTAL))
# file.write('\n')
#
# file.close()
file = open('user.txt','a')

start = 1
number = int(input("enter number of the student: "))
student_marks = []
while start <= number:
    print(f"======student{start}==========")
    for mark in range(1):
        print(input("enter name of the person"))
        subject1 = int(input("enter marks of science:"))
        subject2 = int(input("enter marks of math:"))
        subject3 = int(input("enter marks of social:"))
        subject4 = int(input("enter marks of computer:"))
        subject5 = int(input("enter name of optmath:"))
        data = [subject1, subject2, subject3, subject4, subject5]
        student_marks.append(data)

    start += 1




total_student = []
for student in student_marks:
    total = 0
    for marks in student:
        total = total + marks

    total_student.append(total)

student1 = 1
for tt in total_student:
    pre = tt / 5
    division = ""
    if pre > 30 and pre < 40:
        division += 'just passs'

    elif pre > 60 and pre < 70:
        division+= 'second  division'

    elif pre > 70 and pre < 80:
        division+= 'firt division'

    elif pre > 90 and pre < 100:
        division+= 'distinction'

    else:
        print('failed')

    print(f"student:{student1} total:{tt} pre{pre} division{division}")

    student1 += 1
file.write()
file.write('\n')
file.close()
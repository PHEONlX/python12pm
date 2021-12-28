# tyoes f loop :for loop, . while loop, 3. nested loop

# while loop
# if x%2==0
# start=1
#
# while start <=10:
#     print("hello")
#     start +=1

# classwork----
# evenum=0
# start= 1
# total_odd=0
# while start <=10:
#     if start%2==0:
#         evenum = evenum+start
#     else:
#         total_odd=total_odd +start
#     start=+1
#
# print(evenum)
# print(total_odd)

# ____classwork2___+

#
# start=1
# names=[]
# while start<5:
#     names =input("enter names")
#     names.append(names)
#     start+=1
# print(names)


# ______class work3_______
# [[names,age,phone],[name,age,phone]

#
# start=1
# names=[]
#
#
# while start <=2:
#     names=input("enter name of the person:")
#     age=input("enter age of person")
#     phone = input("enter phone number")
#     a=[]
#     start=+1
#     a.append(names)
#     a.append(age)
#     a.append(phone)
#     names.append(a)
# print(names)


#
# x=1
# num=int(input("enter number of student:"))
# users=[]
# while x<=num:
#     name=input("enter name:")
#     address=input("enter address")
#     phone=int(input("enter phone no:"))
#     student=[name,address,phone]
#     users.append(student)
#
#     x+=1
#
#
# print=users
#


# 9843363725
# dhan prasad dahal

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
# print (student_marks)

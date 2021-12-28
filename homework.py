# theory_marks = 35
# practical_marks=45
#
# if theory_marks + practical_marks >=100:
#
#     print ("your are passed")
# else:
#     print("you are failed")

# print("1. NTC 2. NCELL")
# total_amount = 100
# question = int(input("select sim :"))
# if question == 1:
#     cd = int(input("enter call duration :"))
#
#     if cd < 10:
#         print("your earned rs1 bonus")
#
#     elif cd > 11 or cd < 20:
#         print("you earned rs 5 bonus")
#
#     elif cd > 21 or cd < 30:
#         print("you earned rs 10 bonus ")
#     elif cd > 31 or cd < 40:
#         print('you earned rs 15 bonus')
#     elif cd > 41 or cd < 50:
#         print("you earned rs 20")
#     elif cd > 51 or cd < 60:
#         print("you earned rs 25")
#     elif cd > 61 or cd < 70:
#         print("you earned  rs30 bonus")
#     elif cd > 71 or cd < 80:
#         print("you earned bonus rs 35 ")
#     elif cd > 81 or cd < 90:
#         print("you earned bonus rs 40")
#     elif cd > 91 or cd < 100:
#         print("you earned rs 50")
#     else:
#         print("invalid")
#         print("your max bonus is  rs 50")
#         exit()
#
# elif question ==2:
#     cd=int(input("enter call duration:"))
#     if cd < 10:
#         print("you earned rs 5 bonus")
#     elif cd <20:
#         print("you earned rs 10 bonus ")
#     elif cd <30:
#         print("you earned rs 15 bonus ")
#     elif cd <40:
#         print ("you earned rs 20 bonus")
#     elif cd < 50:
#         print  ("you earned rs 25 bonus")
#     elif cd <60:
#         print ("you earned rs 30 bonus")
#     elif cd <70:
#         print("you earned rs 35 bonus")
#     elif cd <80:
#         print("you earned rs 40 bonus")
#     elif cd <90:
#         print("you earned rs 50")
#     elif cd <100:
#         print("you earned rs 60 bonus")
#         exit()


#distance
# a=15
# b=10
# c=5
# print("select starting location:")
# print("1.samakushi 2.banasthali 3.jamal 4.gongabu 5.ratnapark")
# location1 = int(input())
# if location1 == 1:
#     print("starting point samskushi")
#     print("select drop location")
#     print("1.samakushi 2.banasthali 3.jamal 4.sanepa 5.ratnapark")
#     location2=int(input())
#     if location2 ==2:
#         print ("drop location banasthali")
#         print ("do you have a student id")
#         print("1.yes 2.no")
#         studentid=int(input())
#         if studentid==1:
#             print("it will take ",b,"rs")
#         else:
#             print ("it will take ",a,"rs")
#     elif location2 ==3:
#         print ("drop location jamal")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid==1:
#             print("it will take ",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2== 4:
#         print("drop location sanepa")
#         print('do youy have a student id')
#         print("1.yes 2. no")
#         studentid=int(input())
#         if studentid ==1:
#             print("it will take",b,"rs")
#         else:
#             print("it will take",a+c,"rs")
#
#     elif location2  ==5:
#         print ("drop location ratnapark")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid=int(input())
#         if studentid ==1:
#             print("it will take ",b,"rs")
#         else:
#             print("it will take",a,"rs")
#
# elif location1 ==2:
#     print("starting location banasthali")
#     print("select drop location")
#     print("1.samakushi 2.banasthali 3.jamal 4.sanepa 5.ratnapark")
#     location2=int(input())
#     if location2 ==1:
#         print("drop location is smakushi")
#         print ("do you have a student id")
#         print("1.yes 2.no")
#         studentid=int(input())
#         if studentid ==1:
#             print("it will take ",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2==3:
#         print("drop location is jamal")
#         print("do you have student id")
#         print ("1.yes 2.no")
#         studentid=int(input())
#         if studentid==1:
#             print ("then it will take",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2 == 4:
#         print("drop location is sanepa")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#     elif location2 == 5:
#         print("drop location is ratnapark")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#
# elif location1 ==3:
#     print("starting location jamal")
#     print("select drop location")
#     print("1.samakushi 2.banasthali 3.jamal 4.sanepa 5.ratnapark")
#     location2=int(input())
#     if location2 ==1:
#         print("drop location is smakushi")
#         print ("do you have a student id")
#         print("1.yes 2.no")
#         studentid=int(input())
#         if studentid ==1:
#             print("it will take ",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2==2:
#         print("drop location is banathali")
#         print("do you have student id")
#         print ("1.yes 2.no")
#         studentid=int(input())
#         if studentid==1:
#             print ("then it will take",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2 == 4:
#         print("drop location is sanepa")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#     elif location2 == 5:
#         print("drop location is ratnapark")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#
#
# elif location1 ==4:
#     print("starting location sanepa")
#     print("select drop location")
#     print("1.samakushi 2.banasthali 3.jamal 4.sanepa 5.ratnapark")
#     location2=int(input())
#     if location2 ==1:
#         print("drop location is smakushi")
#         print ("do you have a student id")
#         print("1.yes 2.no")
#         studentid=int(input())
#         if studentid ==1:
#             print("it will take ",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2==2:
#         print("drop location is banasthali")
#         print("do you have student id")
#         print ("1.yes 2.no")
#         studentid=int(input())
#         if studentid==1:
#             print ("then it will take",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2 == 3:
#         print("drop location is jamal")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#     elif location2 == 5:
#         print("drop location is ratnapark")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#
# elif location1 ==5:
#     print("starting location ratnapark")
#     print("select drop location")
#     print("1.samakushi 2.banasthali 3.jamal 4.sanepa 5.ratnapark")
#     location2=int(input())
#     if location2 ==1:
#         print("drop location is smakushi")
#         print ("do you have a student id")
#         print("1.yes 2.no")
#         studentid=int(input())
#         if studentid ==1:
#             print("it will take ",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2==2:
#         print("drop location is banasthali")
#         print("do you have student id")
#         print ("1.yes 2.no")
#         studentid=int(input())
#         if studentid==1:
#             print ("then it will take",b,"rs")
#         else:
#             print("it will take ",a,"rs")
#     elif location2 == 3:
#         print("drop location is jamal")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")
#     elif location2 == 4:
#         print("drop location is sanepa")
#         print("do you have a student id")
#         print("1.yes 2.no")
#         studentid = int(input())
#         if studentid == 1:
#             print("it will take ", b, "rs")
#         else:
#             print("it will take ", a+c, "rs")

#homework

samsung=30000
mi=20000
oppo=45000
servicecharges=100
plastic=500
bag=1000
giftwrap=1250
print("Best Mobile bazar")
print("the product you would like to buy")
print("1.mi for rs 20000")
print("2.samsung for rs 30000")
print("3.oppo for 45000")
item=int(input())
if item ==1:
    print("do you want to buy this item")
    print("1.yes 2.no")
    item2=int(input())
    if item2==1:
        print("in what quantity would you like to buy this")
        Q=int(input())
        q=Q *mi
        print("would you like this item to be deliverd,cost=1000")
        print("please kindly press 1 for delivery")
        delivery =int(input())
        if delivery == 1:
            print ("where would you like it delivered")
            print("press 1.for ktm ,13% tax included")
            print("press 2 for bhaktapur,10%tax included")
            print ("press3 for lalitpur,5% tax included")
            servicecharges=int(input())
            if servicecharges==1:
                o=q
                q=(13/100)*q
                o=o+q
                print("how would you like it packed")
                print ("1. would like it in plastic ,cost =500 ")
                print ("2. would you like it in bag ,cost= 1000")
                print ("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage=int(input())
                if pacakage ==1:
                    print("you choose plastic")
                    print("your grand total is",o+plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage==2:
                    print("you choose bag")
                    print ("your grand total is",o+bag)
                    print("thank you for using mobile bazar app")
                elif pacakage==3:
                    print("you choose giftwrap" )
                    print("your grand total is ",o+giftwrap)
                    print("thank you for using mobile bazar app")
            elif servicecharges==2:
                o=q
                q= (10/100)*q
                o=o+q
                print("how would you like it packed")
                print ("1. would like it in plastic ,cost =500 ")
                print ("2. would you like it in bag ,cost= 1000")
                print ("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage=int(input())
                if pacakage ==1:
                    print("you choose plastic")
                    print("your grand total is",o+plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage==2:
                    print("you choose bag")
                    print ("your grand total is",o+bag)
                    print("thank you for using mobile bazar app")
                elif pacakage==3:
                    print("you choose giftwrap" )
                    print("your grand total is ",o+giftwrap)
                    print("thank you for using mobile bazar app")
            elif servicecharges==3:
                o=q
                q= (5/100)*q
                o=o+q
                print("how would you like it packed")
                print ("1. would like it in plastic ,cost =500 ")
                print ("2. would you like it in bag ,cost= 1000")
                print ("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage=int(input())
                if pacakage ==1:
                        print("you choose plastic")
                        print("your grand total is",o+plastic)
                        print("thank you for using mobile bazar app")
                elif pacakage==2:
                        print("you choose bag")
                        print ("your grand total is",o+bag)
                        print("thank you for using mobile bazar app")
                elif pacakage==3:
                        print("you choose giftwrap" )
                        print("your grand total is ",o+giftwrap)
                        print("thank you for using mobile bazar app")
        else:
             print("how would you like it packed")
             print ("1. would like it in plastic ,cost =500 ")
             print ("2. would you like it in bag ,cost= 1000")
             print ("3.would you like it giftwrapped,cost=1250")
             print("4.none")
             pacakage=int(input())
             if pacakage ==1:
                print("you choose plastic")
                print("your grand total is",q+plastic)
                print("thank you for using mobile bazar app")
             elif pacakage==2:
                print("you choose bag")
                print ("your grand total is",q+bag)
                print("thank you for using mobile bazar app")
             elif pacakage==3:
                print("you choose giftwrap" )
                print("your grand total is ",q+giftwrap)
                print("thank you for using mobile bazar app")
    else:
        print("thank you for you using")
        exit()

if item ==2:
    print("do you want to buy this item")
    print("1.yes 2.no")
    item2=int(input())
    if item2==1:
        print("in what quantity would you like to buy this")
        Q=int(input())
        q=Q *samsung
        print("would you like this item to be deliverd,cost=1000")
        print("please kindly press 1 for delivery")
        delivery =int(input())
        if delivery == 1:
            print ("where would you like it delivered")
            print("press 1.for ktm ,13% tax included")
            print("press 2 for bhaktapur,10%tax included")
            print ("press3 for lalitpur,5% tax included")
            servicecharges=int(input())
            if servicecharges==1:
                o=q
                q=(13/100)*q
                o=o+q
                print("how would you like it packed")
                print ("1. would like it in plastic ,cost =500 ")
                print ("2. would you like it in bag ,cost= 1000")
                print ("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage=int(input())
                if pacakage ==1:
                    print("you choose plastic")
                    print("your grand total is",o+plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage==2:
                    print("you choose bag")
                    print ("your grand total is",o+bag)
                    print("thank you for using mobile bazar app")
                elif pacakage==3:
                    print("you choose giftwrap" )
                    print("your grand total is ",o+giftwrap)
                    print("thank you for using mobile bazar app")
            elif servicecharges==2:
                o=q
                q= (10/100)*q
                o=o+q
                print("how would you like it packed")
                print ("1. would like it in plastic ,cost =500 ")
                print ("2. would you like it in bag ,cost= 1000")
                print ("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage=int(input())
                if pacakage ==1:
                    print("you choose plastic")
                    print("your grand total is",o+plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage==2:
                    print("you choose bag")
                    print ("your grand total is",o+bag)
                    print("thank you for using mobile bazar app")
                elif pacakage==3:
                    print("you choose giftwrap" )
                    print("your grand total is ",o+giftwrap)
                    print("thank you for using mobile bazar app")
            elif servicecharges==3:
                o=q
                q= (5/100)*q
                o=o+q
                print("how would you like it packed")
                print ("1. would like it in plastic ,cost =500 ")
                print ("2. would you like it in bag ,cost= 1000")
                print ("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage=int(input())
                if pacakage ==1:
                        print("you choose plastic")
                        print("your grand total is",o+plastic)
                        print("thank you for using mobile bazar app")
                elif pacakage==2:
                        print("you choose bag")
                        print ("your grand total is",o+bag)
                        print("thank you for using mobile bazar app")
                elif pacakage==3:
                        print("you choose giftwrap" )
                        print("your grand total is ",o+giftwrap)
                        print("thank you for using mobile bazar app")
        else:
             print("how would you like it packed")
             print ("1. would like it in plastic ,cost =500 ")
             print ("2. would you like it in bag ,cost= 1000")
             print ("3.would you like it giftwrapped,cost=1250")
             print("4.none")
             pacakage=int(input())
             if pacakage ==1:
                print("you choose plastic")
                print("your grand total is",q+plastic)
                print("thank you for using mobile bazar app")
             elif pacakage==2:
                print("you choose bag")
                print ("your grand total is",q+bag)
                print("thank you for using mobile bazar app")
             elif pacakage==3:
                print("you choose giftwrap" )
                print("your grand total is ",q+giftwrap)
                print("thank you for using mobile bazar app")
    else:
        print("thank you for visiting mobile bazar")

if item == 3:
    print("do you want to buy this item")
    print("1.yes 2.no")
    item2 = int(input())
    if item2 == 1:
        print("in what quantity would you like to buy this")
        Q = int(input())
        q = Q * oppo
        print("would you like this item to be deliverd,cost=1000")
        print("please kindly press 1 for delivery")
        delivery = int(input())
        if delivery == 1:
            print("where would you like it delivered")
            print("press 1.for ktm ,13% tax included")
            print("press 2 for bhaktapur,10%tax included")
            print("press3 for lalitpur,5% tax included")
            servicecharges = int(input())
            if servicecharges == 1:
                o = q
                q = (13 / 100) * q
                o = o + q
                print("how would you like it packed")
                print("1. would like it in plastic ,cost =500 ")
                print("2. would you like it in bag ,cost= 1000")
                print("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage = int(input())
                if pacakage == 1:
                    print("you choose plastic")
                    print("your grand total is", o + plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage == 2:
                    print("you choose bag")
                    print("your grand total is", o + bag)
                    print("thank you for using mobile bazar app")
                elif pacakage == 3:
                    print("you choose giftwrap")
                    print("your grand total is ", o + giftwrap)
                    print("thank you for using mobile bazar app")
            elif servicecharges == 2:
                o = q
                q = (10 / 100) * q
                o = o + q
                print("how would you like it packed")
                print("1. would like it in plastic ,cost =500 ")
                print("2. would you like it in bag ,cost= 1000")
                print("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage = int(input())
                if pacakage == 1:
                    print("you choose plastic")
                    print("your grand total is", o + plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage == 2:
                    print("you choose bag")
                    print("your grand total is", o + bag)
                    print("thank you for using mobile bazar app")
                elif pacakage == 3:
                    print("you choose giftwrap")
                    print("your grand total is ", o + giftwrap)
                    print("thank you for using mobile bazar app")
            elif servicecharges == 3:
                o = q
                q = (5 / 100) * q
                o = o + q
                print("how would you like it packed")
                print("1. would like it in plastic ,cost =500 ")
                print("2. would you like it in bag ,cost= 1000")
                print("3.would you like it giftwrapped,cost=1250")
                print("4.none")
                pacakage = int(input())
                if pacakage == 1:
                    print("you choose plastic")
                    print("your grand total is", o + plastic)
                    print("thank you for using mobile bazar app")
                elif pacakage == 2:
                    print("you choose bag")
                    print("your grand total is", o + bag)
                    print("thank you for using mobile bazar app")
                elif pacakage == 3:
                    print("you choose giftwrap")
                    print("your grand total is ", o + giftwrap)
                    print("thank you for using mobile bazar app")
        else:
            print("how would you like it packed")
            print("1. would like it in plastic ,cost =500 ")
            print("2. would you like it in bag ,cost= 1000")
            print("3.would you like it giftwrapped,cost=1250")
            print("4.none")
            pacakage = int(input())
            if pacakage == 1:
                print("you choose plastic")
                print("your grand total is", q + plastic)
                print("thank you for using mobile bazar app")
            elif pacakage == 2:
                print("you choose bag")
                print("your grand total is", q + bag)
                print("thank you for using mobile bazar app")
            elif pacakage == 3:
                print("you choose giftwrap")
                print("your grand total is ", q + giftwrap)
                print("thank you for using mobile bazar app")
    else:
        print("thank you for visiting mobile bazar")



else:
    print("invalid number")
    exit()


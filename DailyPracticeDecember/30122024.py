def Reverse_String():
    str="jarahaM"
    rev_str=str[::-1]
    print(rev_str)
Reverse_String()

def Reverse_Number():
    num=12345
    Rev_Num=str(num)[::-1]
    print(Rev_Num)
Reverse_Number()

def Is_palindrome(str):
    Condition=str==str[::-1]
    if Condition==1:
      print("String is Palindrome")
    else:
        print("String is not Palindrome")
Is_palindrome("Raje")

def missing_number():
    my_list=[1,2,3,4,5,6,7,8,9,11,15]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end+1))-set(my_list))
    print(result)
missing_number()

def factorial_num():
    num=5
    if num<0:
        print("Number should be positive")
    elif num==0:
        print(0)
    elif num==1:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
         result*=i
        print(result)
factorial_num()

def duplicates():
    my_test_list=[1,2,4,5,5,9,10,11,4,2]
    seen=set()
    duplicates=set()
    for num in my_test_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates()

def LargestinList():
    test_list=[45,74,85,96,71,85,523]
    Largest=test_list[0]
    for num in test_list:
        if num > Largest:
            Largest=num
    print(Largest)
LargestinList()


def Replaceinlist():
    My_List=[1,2,3,4,5,6,7,8]
    My_List.insert(3,11)
    print(My_List)
Replaceinlist()

def ReveseList():
    demo_list=[1,2,3,4,5,6]
    demo_list.reverse()
    print(demo_list)
ReveseList()

def Number_Table():
 n = int(input("Enter the number to print the tables for:"))
 for i in range(1, 11):
    print(n, "x", i, "=", n * i)
Number_Table()

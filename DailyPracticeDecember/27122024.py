def Reverse_String():
    str= "MyString"
    rev_str=str[::-1]
    print(rev_str)
Reverse_String()

def Factorial_num():
    num=4
    if num<0:
        print("Number should be non negative")
    elif num==0:
        print(0)
    elif num==1:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
            result*=i
        print(result)
Factorial_num()

def Missing_number():
    my_list=[3,4,5,6,7,9,11,12,15,17,18,20]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end+1))-set(my_list))
    print(result)

Missing_number()

def duplicates():
    test_list=[4,2,3,6,8,9,4,6,1,7,2,5,7,11]
    seen=set()
    duplicates=set()
    for num in test_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates()

def Largest_in_list():
    test_in_list=[45,85,985,263,415,1258,7451,4555,4150]
    Largest=test_in_list[0]
    for num in test_in_list:
        if num >Largest:
            Largest=num
    print(Largest)
Largest_in_list()

def Smallest():
    demo_list=[1,5,2,4,0.1,8,9,5,3,44]
    Smallest=demo_list[0]
    for num in demo_list:
        if num < Smallest:
            Smallest=num
    print(Smallest)
Smallest()

def Is_Palindrome(str):
    condition=str==str[::-1]
    if condition==1:
        print("String is palinrome")
    else:
        print("String is not palindrome")
Is_Palindrome("Maharaj")

def Multiplication():
    num1=30
    num2=20
    num3=num2*num1
    print(num3)
Multiplication()
def EvenOdd(num):
    if num%2==0:
        print ("Number is even")
    else:
        print ("number is ODD")

EvenOdd(8)


def rev_string():
   str="you"
   rev_str=str[::-1]
   print(rev_str)
rev_string()

def rev_number():
    num=123
    rev_num=str(num)[::-1]
    print(rev_num)
rev_number()

def missing_number_list():
    my_list=[1,2,3,5,9,7,15,18,20]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end+1))-set(my_list))
    print(result)
missing_number_list()

def duplciates():
    my_test_list=[1,2,3,4,5,6,4,8,9,10,11,12,2]
    seen=set()
    duplicates=set()
    for num in my_test_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplciates()

def factorial_num(num):
    if num<0:
        print("Number should be positive")
    elif num==0 or num==1:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
            result*=i
        print(result)
factorial_num(3)

def palindrome_check():
    str="bnjk"
    if str==str[::-1]:
      print("String is Palindrome")
    else:
     print("String is not palindrome")
palindrome_check()

def String_in_upper():
    str="yogesh"
    str=str.upper()
    print(str)
String_in_upper()

def String_in_lower():
    str="MAHESH"
    str=str.lower()
    print(str)
String_in_lower()

def String_replace():
    str="Rajesh"
    str=str.replace("Rajesh","Umesh")
    print(str)
String_replace()

def Largest_in_List():
    test_list=[1,54,26,89,45,364,1005]
    Largest=test_list[0]
    for num in test_list:
        if num>Largest:
            Largest=num
    print(Largest)
Largest_in_List()


def rev_string():
    str="DEMOSTRING"
    rev_str=str[::-1]
    print(rev_str)
rev_string()

def rev_number():
    num=1461
    rev_num=str(num)[::-1]
    print(rev_num)
rev_number()

def Largest_in_List():
    my_list=[1,5,62,35,4,58,9,7,4,1]
    Largest=my_list[0]
    for num in my_list:
        if num > Largest:
            Largest=num
    print(Largest)
Largest_in_List()

def SmallestinList():
    my_test_list=[6,2,14,5,8,9,7,89,12,0.6]
    Smallest=my_test_list[0]
    for num in my_test_list:
        if num<Smallest:
            Smallest=num
    print(Smallest)
SmallestinList()

def missing_number():
    my_list=[1,2,3,4,6,8,10,12]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end+1))-set(my_list))
    print(result)
missing_number()

def duplicates():
    my_list=[1,52,6,5,6,1,25,84,9,7,83,41,7]
    seen=set()
    duplicates=set()
    for num in my_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates()

def palindrome_num():
    str="kmkono"
    if str==str[::-1]:
        print("String is Palindrome")
    else:
        print("String is not palindrome")
palindrome_num()



def factorial_num():
    n=0
    if n<0:
        print("Number is not negative")
    elif n==0 or n==1:
        print(1)
    else:
        result=1
        for i in range(2,n+1):
            result *=i
        print(result)
factorial_num()

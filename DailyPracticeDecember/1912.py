def rev_string():
    str="Yogesh"
    rev_str=str[::-1]
    print(rev_str)
rev_string()

def rev_number():
    num=12345
    rev_num=str(num)[::-1]
    print(rev_num)
rev_number()

def Largest_in_List():
    my_list=[1,2,3,4,5,6,849,45,17]
    largest=my_list[0]
    for num in my_list:
        if num > largest:
         largest =num
    print(largest)
Largest_in_List()

def Largest_in_list():
    my_testlist=[7,8,5,78,45,12,956,24]
    Largest=max(my_testlist)
    print(Largest)
Largest_in_list()

def Smallest_in_List():
    my_list_Demo=[0.5,8,5,6,8,9,4,5,2,3,4,1,888]
    Smallest=my_list_Demo[0]
    for num in my_list_Demo:
        if num<Smallest:
            Smallest=num
    print(Smallest)
Smallest_in_List()

def Smallest_in_list():
    My_Test_List=[12151,15,15,24,6,2,4,8,7]
    smallest=min(My_Test_List)
    print(smallest)
Smallest_in_list()

def missing_number_List():
    MyList=[2,3,4,5,6,7,9,11,13,15]
    start=MyList[0]
    end=MyList[-1]
    result=sorted(set(range(start, end+1))-set(MyList))
    print(result)
missing_number_List()


def duplicates_list():
    test_list=[2,5,5,9,8,6,4,8]
    seen=set()
    duplicates=set()
    for num in test_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(duplicates)
duplicates_list()

def Palindrome():
    str='radar'
    if str==str[::-1]:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")
Palindrome()


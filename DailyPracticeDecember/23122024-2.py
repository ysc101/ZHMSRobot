def duplicates_in_list():
    my_list=[1,2,3,4,5,2,5,6,8,9,41,4]
    seen=set()
    duplicates=set()
    for num in my_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates_in_list()

def missing_number_list():
    test_list=[1,2,3,4,5,8,9,14,15]
    start=test_list[0]
    end=test_list[-1]
    result=sorted(set(range(start,end+1))-set(test_list))
    print(result)
missing_number_list()

def factorial_num():
    num=10
    if num<0:
        print("Number should be positive")
    elif num==0 or num==1:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
            result *=i
        print(result)
factorial_num()

def LargestList():
    my_test_list=[1,5,85,95,62,4,1,5,3,84]
    Largest=my_test_list[0]
    for num in my_test_list:
       if num >Largest:
         Largest=num
    print(Largest)
LargestList()





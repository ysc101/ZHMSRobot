def rev_string():
    str="My String"
    rev_str=str[::-1]
    print(rev_str)
rev_string()

def rev_number():
    num=12345
    rev_num=str(num)[::-1]
    print(rev_num)
rev_number()

def missing_list():
    my_list=[1,2,5,8,9,10,13,15]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end +1))-set(my_list))
    print(result)
missing_list()

def duplicates():
    test_list=[1,5,5,12,8,10,11,6,6]
    seen=set()
    duplicates=set()
    for num in test_list:
       if num in seen:
        duplicates.add(num)
       else:
        seen.add(num)
    print(sorted(duplicates))
duplicates()



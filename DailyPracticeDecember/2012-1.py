def missing_number_list():
    myList=[1,2,4,6,8,10,11,12,14,15,17]
    start=myList[0]
    end=myList[-1]
    result=sorted(set(range(start,end+1))-set(myList))
    print(result)
missing_number_list()


def duplicateinlist():
    mylist=[3,5,6,6,8,7]
    seen=set()
    duplicates=set()
    for num in mylist:
        if num in seen:
           duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicateinlist()


def Palindrome_check():
    str='Mylist'
    if str==str[::-1]:
        print("String is Palindrome")
    else:
        print("String is not palindrome")
Palindrome_check()


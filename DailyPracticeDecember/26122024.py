def rev_string():
    str="ECILOP"
    rev_str=str[::-1]
    print(rev_str)
rev_string()

def Is_Palindrome():
    str="OYO"
    condition=str==str[::-1]
    if condition==1:
        print("String is palindrome")
    else:
        print("String is not palindrome")
Is_Palindrome()

def Largest_in_List():
    num_list=[14,85,95,456,358,123,741]
    Largest=num_list[0]
    for num in num_list:
        if num>Largest:
            Largest=num
    print(Largest)
Largest_in_List()

def Largest_in_testlist():
    testlist=[78,98,56,23,56,41,52,78,95,4,2,850]
    Largest=max(testlist)
    print(Largest)
Largest_in_testlist()

def factorial_Num(num):
   if num<0:
       print("Number should be positive")
   elif num==1:
       print(1)
   elif num==0:
       print(0)
   else:
       result=1
       for i in range(2,num+1):
           result*=i
       print(result)
factorial_Num(15)

def missing_number():
    demo_list=[3,4,5,6,7,9,10,12]
    start=demo_list[0]
    end=demo_list[-1]
    condition=sorted(set(range(start,end+1))-set(demo_list))
    print(condition)
missing_number()

def duplicates():
    demo_test_list=[1,5,1,6,7,8,9,10,11,7]
    seen=set()
    duplicates=set()
    for num in demo_test_list:
      if num in seen:
          duplicates.add(num)
      else:
        seen.add(num)
    print(sorted(duplicates))
duplicates()

def String_Swap():
    str="yOGESh"
    str=str.swapcase()
    print(str)
String_Swap()


def missing_number_list():
    my_list=[1,2,3,6,9,10,12,15,16,17,20]
    start=my_list[0]
    end=my_list[-1]
    result=sorted(set(range(start,end+1))-set(my_list))
    print(result)
missing_number_list()

def factorial_num():
    num=4
    if num<0:
        print("number shoul be positive")
    elif num==1 or num==0:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
            result*=i
    print(result)
factorial_num()

def duplicates():
    my_test_list=[1,5,2,1,6,8,4,3,9,7,10,11,6]
    seen=set()
    duplicates=set()
    for num in my_test_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(sorted(duplicates))
duplicates()

def Largest_in_list():
  test_list=[15,85,42,65,32,25,98,74,14,123,18,10]
  Largest=test_list[0]
  for num in test_list:
      if num >Largest:
          Largest=num
  print(Largest)
Largest_in_list()

def Smallest_in_List():
    test_in_List=[1,85,9,6,5,4,19,63,521,7]
    Smallest=test_in_List[0]
    for num in test_in_List:
        if num<Smallest:
         Smallest=num
    print(Smallest)
Smallest_in_List()



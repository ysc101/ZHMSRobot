import requests

from DailyPracticeDecember.tokenfile import ZPToken

url="http://192.168.0.162:8080/api/work/GetWorkOrderDetailsByZPIDandDeptID"
headers={"Authorization":f"Bearer {ZPToken}"}
payload= {
        "ZPID":3,
        "DeptID":9,
        "BlockID":1,
        "FinancialYear":"2019-20"
    }
response=requests.get(url,headers=headers,json=payload)
if response.status_code==200:
    try:
     data=response.json()
     print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Response not in JSON")
else:
    print("Response Code :",response.status_code)
    print(f"Response text is: ",{response.text})


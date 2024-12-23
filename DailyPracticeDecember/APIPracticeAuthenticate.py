import requests
url="http://192.168.0.162:8080/api/Users/authenticate"
payload={
    "MobileNo":"8087333794",
    "Password":"Pass@123"
}
response=requests.post(url,json=payload)
if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Response in json")
else:
    print("Response Code ",response.status_code)
    print(f"Response Text",{response.text})

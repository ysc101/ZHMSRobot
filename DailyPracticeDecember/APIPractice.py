import requests
url="http://192.168.0.162:8080/api/Contractor/CheckMobileNumber"
#headers={"Authorization":"Zp_Token"}
payload={"Mobile":"8087333794"}

response=requests.get(url,json=payload)
if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Reponse not in JSON")
else:
    print("Response Code ",response.status_code)
    print(f"Response text: ",{response.text})


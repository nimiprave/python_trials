import requests

url = "https://databuffermta-dev.cfapps.sap.hana.ondemand.com/actuator"
response = requests.get(url, timeout=10)
# response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("API Response:", data)
else:
    print("Failed to retrieve data:", response.status_code)

#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://dev70265.service-now.com/api/now/table/incident?sysparm_query=priority=3'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'b2uUVYOgZkv5'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)


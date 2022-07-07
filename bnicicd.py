import requests


print ("Hello world")
print ("Testing CICD BNI")

response = requests.get("https://www.google.com")

print (response.text)
import requests


url = input("Enter the url : ")
r = requests.get(url)

file_name = input("Enter file name : ")
with open(file_name,'w') as file:
    file.write(r.text)


import requests
import base64

url = "http://10.110.20.64:5000/photo"
file_path = "/home/vmuser/agentforP/image1.jpg" 
file_name=file_path.split('/')[-1]
file = open(file_path, 'rb')
files   = {'file':(file_name, file, 'image/jpg')}
r = requests.post(url, files=files)

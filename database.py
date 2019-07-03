# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:09:26 2019

@author: Nishant
"""
#https://www.geeksforgeeks.org/get-post-requests-using-python/
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "http://websmartattendance.000webhostapp.com/mark_attendance.php"
  
# your API key here 
API_KEY = "XXXXXXXXXXXXXXXXX"
  
# your source code here 
source_code = ''' 
print("Hello, world!") 
a = 1 
b = 2 
print(a + b) 
'''
  
# data to be sent to api 
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python',
        'teacher_id':'1245',
        'student_id':'1245stu',
        'subject_id':'1245sub',
        'time':'125445'} 
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
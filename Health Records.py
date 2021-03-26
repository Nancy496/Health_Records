#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!pip install pymongo


# In[8]:


#import pymongo as Healthcare #healthcare is an alias
#!pip3 install dnspython


# In[9]:


#!pip install dnspython==2.0.0


# In[10]:


#!pip install dnspython==1.15.0


# In[2]:


import dns
import pymongo


# In[3]:


import pymongo
conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["Heathcare"]
collection = db["Hospital"]


# In[14]:




post =[{"Hospital_Id": 32,"Hospital_Name": " Mwanza_Hospital", "Bed_Count": 120, "Address": "234 Nairobi"},
    {"Hospital_Id": 33,"Hospital_Name": "Uganda-Kampala", "Bed_Count": 150, "Address": "446 Texas"},
    {"Hospital_Id": 34,"Hospital_Name": "Ontario River","Bed_Count":180,"Address":"759 Tanzania"},
    {"Hospital_Id": 35,"Hospital_Name": "DFW Hospital","Bed_Count":100,"Address":"329 Kenya"}]
     
collection.insert_many(post)

print(post)


# In[17]:


#conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["Heathcare"]
collection1 = db["Doctor"]

post =[{"Doctor_Id": 81,"Hospital_Id":32, "Doctor_Name":"Esther_Waitumbi", "Date_Joined":"2021-03-03" , "Speciality": "Oncology","Salary":500000,"Experience":"2_Years"},
    {"Doctor_Id": 82,"Hospital_Id":33, "Doctor_Name": "Maggy_Omondi" , "Date_Joined": "2020-05-12" ,"Speciality": "Dermatologist","Salary":100000,"Experience":"3_Years"},
    {"Doctor_Id": 83,"Hospital_Id":34, "Doctor_Name": "Hellen_Kibisu", "Date_Joined":"2019-02-08","Speciality": "Gynacologist","Salary":200000,"Experience":"10_Years"},
    {"Doctor_Id": 84,"Hospital_Id":35, "Doctor_Name": "Kamau_Ngegi","Date_Joined":"2018-04-09"," Speciality":"Pediatric","Salary":300000,"Experience":"15_Years"}]
     
collection1.insert_many(post)
print(post)


# In[13]:


#dblist = Health.list_database_names()
#if "Heathcare" in dblist:
 #   print("The database exists.")


# In[19]:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Heathcare"]
mycol = mydb["Doctor"]


# In[20]:


print(mydb.list_collection_names())


# In[7]:


import pymongo
conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = conn["Heathcare"]
collection1 = db["Doctor"]

post1 =[{"Doctor_Id": 81,"Hospital_Id":32, "Doctor_Name":"Esther_Waitumbi", "Date_Joined":"2021-03-03" , "Speciality": "Oncology","Salary":"500000","Experience":"2_Years"},
    {"Doctor_Id": 82,"Hospital_Id":33, "Doctor_Name": "Maggy_Omondi" , "Date_Joined": "2020-05-12" ,"Speciality": "Dermatologist","Salary":"100000","Experience":"3_Years"},
    {"Doctor_Id": 83,"Hospital_Id":34, "Doctor_Name": "Hellen_Kibisu", "Date_Joined":"2019-02-08","Speciality": "Gynacologist","Salary":"200000","Experience":"10_Years"},
    {"Doctor_Id": 84,"Hospital_Id":35, "Doctor_Name": "Kamau_Ngegi","Date_Joined":"2018-04-09"," Speciality":"Pediatric","Salary":"300000","Experience":"15_Years"}]
     
collection1.insert_many(post1)
print(post1)


# In[33]:


#import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["Heathcare"]
#mycol = mydb["Doctors"]

#path = [
    {"Doctor_Id": 89,"Hospital_Id":33, "Doctor_Name": "Maggy_Omondi" , "Date_Joined": "2020-05-12" ,"Speciality": "Dermatologist","Salary":"100000","Experience":"3_Years"},
    {"Doctor_Id": 88,"Hospital_Id":32, "Doctor_Name":"Esther_Waitumbi", "Date_Joined":"2021-03-03" , "Speciality": "Oncology","Salary":"500000","Experience":"2_Years"},
    {"Doctor_Id": 87,"Hospital_Id":34, "Doctor_Name": "Hellen_Kibisu", "Date_Joined":"2019-02-08","Speciality": "Gynacologist","Salary":"200000","Experience":"10_Years"},
    {"Doctor_Id": 86,"Hospital_Id":35, "Doctor_Name": "Kamau_Ngegi","Date_Joined":"2018-04-09"," Speciality":"Pediatric","Salary":"300000","Experience":"15_Years"}]
     
#mycol.insert_many(path)
#collection.insert_many(post)
#print(post)


# In[4]:


join_cursor = db.Hospital.aggregate(
[
    {
        "$lookup": {
        "from": "Doctor",
        "localField" : "Hospital_Id", 
       "foreignField" : "Hospital_Id",
     "as" : "Hospital_join"       
    }
    }
]
)

for x in join_cursor:
    print (x)


# In[24]:


import pymongo
import webbrowser
#from pymongo import Mongoclient
conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = conn["Healthcare"]
collection = db["Hospital"]
hosi = []
tbl = "<tr><td>Hospital_Id</td><td>Hospital_Name</td><td>Bed_Count</td><td>Address</td></tr>"
hosi.append(tbl)

for y in collection.find():
    a = "<tr><td>%s</td>"%y['_id']
    hosi.append(a)
    b = "<td>%s</td>"%y['Hospital_Id']
    hosi.append(b)
    c = "<td>%s</td>"%y['Hospital_Name']
    hosi.append(c)
    d = "<td>%s</td>"%y['Bed_Count']
    hosi.append(d)
    e = "<td>%s</td></tr>"%y['Address']
    hosi.append(e)
    
    


# In[19]:


for y in collection.find():
    print (y)


# In[20]:


import pymongo
import webbrowser
#from pymongo import Mongoclient
conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = conn["Healthcare"]
collection1 = db["Doctor"]
doc = []
tbl2 = "<tr><td>Doctor_Id</td><td>Doctor_Name</td><td>Hospital_Id</td><td>Date_Joined</td><td>Speciality</td><td>Salary</td><td>Experience</td></tr>"
doc.append(tbl2)

for z in collection1.find():
    a = "<tr><td>%s</td>"%y['_id']
    doc.append(a)
    b = "<td>%s</td>"%y['Doctor_Id']
    doc.append(b)
    c = "<td>%s</td></tr>"%y['Doctor_Name']
    doc.append(c)
    d = "<td>%s</td></tr>"%y['Hospital_Id']
    doc.append(d)
    e = "<td>%s</td></tr>"%y['Date_Joined']
    doc.append(e)
    f = "<td>%s</td></tr>"%y['Speciality']
    doc.append(f)
    g = "<td>%s</td></tr>"%y['Salary']
    doc.append(g)
    h = "<td>%s</td></tr>"%y['Experience']
    doc.append(h)


# In[25]:


import webbrowser

#Create html file
f = open('health.html', 'w')

#First part of html docstring
m = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta cSharset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hosi</title>
</head>
<body>
 <h1>Health records</h1>
    <table>
%s
</table>
 <table>
%s
</table>
</body>
</html>'''%(hosi,doc) #html from empty list

#write to html file
f.write(m)



#close file
f.close()

#Open file in browser
webbrowser.open_new_tab('health.html')


# In[ ]:





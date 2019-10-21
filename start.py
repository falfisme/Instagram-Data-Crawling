from crawler import *
from inscrawler.fetch import *
from inscrawler.settings import *
from followers import *
import json

#database
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client["instagramcr"]
col = db["akun"]


import os

### ---->>>>>> Faqihuddin Al Farisi - 1313617025  | Wisnu Aji - 1313617027 ---->>>>>>

###  mengambil class inscrawler
ins = InsCrawler()

### >>>>>>>> mengambil follower (list dari akun yang diisi)
list_followers = ambilfollowers('faizaakmal')
print("-- Follower 1 --")

list_followers2 = []

### >>>>>>>> mengambil follower dari list isi manual (uncomment jika ingin menggunakannya)
#list_followers = ['instaunjcrawl','ihsn.m','instaunjcrawl','faizaakmal']
print(list_followers)

def follower1(list_flw):
    for i in list_flw:
        print(i) 
        try:
            inti(i)
            pass
        except:
            print('Akun Ini adalah Akun Private')
            continue
        

def follower2(): 
    print("-- Followers 2 --")
   
    for f in list_followers:
        flw = ambilfollowers(f)
        list_followers2.append(flw)
        
    print(list_followers2)
        
    for s in list_followers2:
        for j in s:
            if s[0] != j:
                print(j)
                try:
                    inti(j)
                    pass
                    
                except:
                    print('Akun Ini adalah Akun Private')
                    continue
    

def inti(user): 
    yangTelahAda = col.distinct("username")
    if user not in yangTelahAda:
        # querycek = {"username" : j}
        # col.delete_many(querycek)
        data_perakun = ins.get_user_posts(user)
        col.insert_many(data_perakun)
        print("data telah dimasukan ke database")
    else:
        print("data telah diupload sebelumnya")

follower1(list_followers)
follower2()



    


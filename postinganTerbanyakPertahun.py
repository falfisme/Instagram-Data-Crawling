import pymongo
from pymongo import MongoClient
from collections import Counter

##############################################################
# MENGECEK POSTINGAN TERBAYAK DALAM SATU NETWORK PERTAHUNNYA #
##############################################################
# ----------------- MASUKKAN ANGKA TAHUN ------------------- #

tahun = '2019'

# -----------------

client = MongoClient('localhost', 27017)
db = client["instagramcr"]
col = db["akun"]

myquery = { "datetime": { "$regex": tahun } }
mydoc = col.find(myquery)
tersimpan = []
for x in mydoc:
  tersimpan.append(x['username'])

counter = Counter(tersimpan)
print("Akun Paling Banyak Postingan Pertahun " + tahun + " adalah = ")
print(counter.most_common(1))
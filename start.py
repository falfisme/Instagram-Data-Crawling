from crawler import *
from inscrawler.fetch import *
from inscrawler.settings import *
from followers import *

import os

### Faqihuddin Al Farisi - 1313617025  | Wisnu Aji - 1313617027 

### mengambil class inscrawler
ins = InsCrawler()

### mengambil follower (list dari akun yang diisi)
list_followers = ambilfollowers('falfisme')

### mengambil follower dari list isi manual (uncomment jika ingin menggunakannya)
# list_followers = ['falfisme']

### variable data digunakan untuk menyimpan akun
data = []

count = 1
for i in list_followers:
    data.extend(ins.get_user_posts(i))
    naming_file = "data_" + str(count) + "_akun3.json"
    output(data, naming_file)
    
    print("data " + i + " berhasil dikeluarkan pada file " + naming_file)
    
    if count > 1 :
        os.remove("data_" + str(count-1) + "_akun3.json")
        print("data sebelumya telah dihapus dan data telah diperbaharui!")
        
    count += 1 



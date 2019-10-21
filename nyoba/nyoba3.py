from crawler import *
from inscrawler.fetch import *
from inscrawler.settings import *
from followers import *

import os

#mengambil class inscrawler
ins = InsCrawler()

#mengambil follower
list_followers = ambilfollowers('omanbdur')
#list_followers = ["wisnu_whiskas", "khymykhdyy9"]

#variable data digunakan untuk menyimpan akun
data = []
count = 1
for i in list_followers:
    data.extend(ins.get_user_posts(i))
    naming_file = "data_" + str(count) + "_akun5.json"
    output(data, naming_file)
    
    print("data " + i + " berhasil dikeluarkan pada file " + naming_file)
    
    if count > 1 :
        os.remove("data_" + str(count-1) + "_akun5.json")
        print("data sebelumya telah dihapus dan data telah diperbaharui!")
        
    count += 1 

#output(data, "yaallahiniudahjadifix.json")



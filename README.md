# Instagram-Data-Crawling

## UPDATED! Instagram Crawler V2

### 1.	Scrap until level 2 followers

Kami telah berhasil mendapatkan followers dan data postingan dari level 2 instagram followernya. Kami menggunakan pendekatan BFS yang lumayan. Pertama, satu akun Instagram kami ambil semua follower dan postingannya, dari situ followernya kita keep kedalam sebuah list dan postingannya kita masukan ke dalam database mongoDB. Setelah semua telah terdownload dengan baik, kami mengambil list follower dari akun yang pertama kita ambil dan kita lakukan hal yang sama (yaitu mengambil post dan followernya) ke semua akun yang memfollow akun pertama yang kita pilih. Setelah semua data telah terdownload dengan baik, berarti kita sudah memiliki level 1 Friend.

Lalu, kita menggunakan semua data follower dari level 1 friend untuk diambil semua postingannya dan kita masukkan ke dalam database lagi. Setelah semua postingan telah terdownload, maka kita telah berhasil mendapatkan level 2 Friend secara urut.

Kami membuat 3 function untuk menjalankannya. Yang pertama fungsi untuk friend level 1 ```def follower1()``` dengan parameter list follower friend level 1, friend level 2 ```def follower2()``` dan program inti ```def inti()``` berguna untuk mengambil datanya. Bisa dicek pada program kami di ```start.py```

### 2.	Do some statistical task from fetched data, explain what are the tasks
Kami berhasil membuat program yaitu “Mengecek postingan terbanyak dalam satu network pertahunnya”. Misalnya akun ```‘A’``` mengupload ke Instagram di tahun 2019 sebanyak 15 kali. Dan akun ```‘B’``` hanya 2 kali. Maka yang akan ditampilkan adalah akun ‘A’ dan banyaknya jumlah postingan itu.
 

### 3.	Saving & Querying to MongoDB
Kami telah berhasil menyimpan seluruh data dari semua postingan langsung ke dalam database. Jika kita menjalankan ```start.py```, maka semua data akan secara otomatis disimpan kedalam database. Dan data juga sudah di filter agar jika ada double data tidak dimasukan kedalam database.


### Terimakasih, dan Selamat Mencoba!

Kelompok :
- Faqihuddin Al Farisi : 1313617025
- Wisnu Aji : 1313617027

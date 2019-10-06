![image](https://d1afx9quaogywf.cloudfront.net/sites/default/files/Logos/Instagram400x230.png)
# Instagram-Data-Crawling
Hello Everyone! Ini adalah Projek tentang pengambilan data instagram otomatis mengenai banyaknya jumlah like, caption, comment, hashtag dan mention profile pengguna yang disebut dari setiap postingan instagram seseorang. Projek ini bertujuan untuk memenuhi tugas matakuliah PKB saya yang ngulang.


### Requirement

Sebelum menggunakan ini, sebaiknya anda menginstall beberapa tools yang saya gunakan terlebih dahulu
- Python 3 keatas (karena program ini menggunakan Python) -> [Website Python](https://www.python.org/)
- Code Editor (vscode recomended) -> [Download Visual Studio Code](https://code.visualstudio.com/download)
- [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjwoebsBRCHARIsAC3JP0JeSMXX6dBnc07t6j64KK7l2VEml0kz_9F5W6Xmu3ZVaf4auB4gfVgaAkhkEALw_wcB&gclsrc=aw.ds) 
- Install [Huaying Instagram Crawler](https://github.com/huaying/instagram-crawler)
- Install [Instaloader](https://instaloader.github.io/)
- download file file diatas


### Cara menggunakan
Cukup mudah
1. Buka file ```start.py``` dengan kode editor
2. Isi username yang kamu inginkan untuk diambil list followernya, contoh ingin mengambil data para follower @faizaakmal ```list_followers = ambilfollowers('faizaakmal')``` 
3. Jalankan file tersebut
4. Jika sudah selesai, file akan keluar didalam folder yang sama dengan nama ```data_(banyaknya)_akun.json``` contoh: sistem berhasil mengambil 50 akun. maka outputnya ```data_50_akun.json```
5. selesai

### Output
Output dari project ini adalah sebuah file berekstensi ```.json``` yang berisikan data siapa saja yang telah terambil.

Berikut contoh outputnya:
```
 {
        "key": "https://www.instagram.com/p/Br66xC2A3JE/",
        "username": "falfisme",
        "location": "Jakarta, Indonesia",
        "datetime": "2018-12-28T06:15:39.000Z",
        "likes": 129,
        "caption": "Liburan hampir tiba.\nKayanya.\n.\nPersimpangan Sisingamangaraja, Jakarta Selatan\n.\n#jakarta #jakartabanget #explorejakarta #jktinfo #enjoyjakarta #indonesia #jakartaku #jakartacityscape #amazingjakarta #vsco\n#magnificentjakarta",
        "hashtags": [
            "jakarta",
            "jakartabanget",
            "explorejakarta",
            "jktinfo",
            "enjoyjakarta",
            "indonesia",
            "jakartaku",
            "jakartacityscape",
            "amazingjakarta",
            "vsco",
            "magnificentjakarta"
        ],
        "comments": [
            {
                "author": "sunnydream.id",
                "comment": "Assalamualaykum sahabat"
            },
            {
                "author": "falfisme",
                "comment": "@sunnydream.id waalaikumsalamm",
                "mentions": [
                    "sunnydream.id"
                ]
            },
            {
                "author": "omanbdur",
                "comment": "Sek suwe lur"
            },
            {
                "author": "omanbdur",
                "comment": "@falfisme balik jakarta ntar juga normal lagi",
                "mentions": [
                    "falfisme"
                ]
            },
            {
                "author": "falfisme",
                "comment": "@omanbdur sini dur kite poto poto",
                "mentions": [
                    "omanbdur"
                ]
            },
            {
                "author": "omanbdur",
                "comment": "@falfisme januari",
                "mentions": [
                    "falfisme"
                ]
            }
        ]
    },
```

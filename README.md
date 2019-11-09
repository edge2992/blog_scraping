# scraping
# blog_scraping

はてなブックマークの人気エントリを250件くらいurlとタイトルとテキストデータを取ってくる

# 初期設定
MongoDBの設定

MongoDB Compassがあると便利

https://garafu.blogspot.com/2019/02/install-mongod-on-macos.html

https://qiita.com/____easy/items/4dcda6cc4f5e7de13d36


# 現在のmongoDBの状態
| url | URL |
| title | ブログタイトル |
| html | htmlそのまま |
| content | 文章|

# 使い方
ルートディレクトリ で

`scrapy crawl broad`

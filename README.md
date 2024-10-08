
# Vercel Scrapy Monotaro Project

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2Fvercel-scrapy-monotaro)

Vercel上で動作する Monotaro の商品詳細ページをスクレーピングするための WebAPI です。
上のボタンを押すと Vercel ＆ Github を新規作成できます。

なお、ローカルPCでも動作させたい場合は[Running Locally](#running-locally)を参照ください。

## 目次

- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment on Vercel](#deployment-on-vercel)
- [License](#license)

## Installation

前提：ローカルPCに **git、ptyhon3.12** がインストール済

1. **ローカルPCにリポジトリのクーロン作成:**

   ```cmd
   git clone https://github.com/katsu-yoshimu/vercel-scrapy-monotaro.git
   ```

2. **ローカルPCに仮想完了作成と仮想環境アクティベート:**

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **ローカルPCに必要なPythonパッケージをインストール:**

   ```cmd
   cd vercel-scrapy-monotaro
   pip install -r requirements.txt  
   pip install fastapi-cli
   ```

   fastapi-cli はローカルPCで動作させたい場合のみ必要

## Running Locally

1. **WebAPIサーバ起動:**

   ```cmd
   fastapi dev api/main.py
   ```

2. **ブラウザで以下のURLでアクセス:**

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. このページからWebAPIの実行できる

## Deployment on vercel

1. **Vercel & Github 新規追加:**

   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2Fvercel-scrapy-monotaro)

   上のボタンを押すと Vercel ページに遷移します。その後、Vercel & Github を追加します。

2. **ブラウザで以下のURLでアクセス:**

   [https://scrapy-monotaro-katsu-yoshimus-projects.vercel.app/docs](https://scrapy-monotaro-katsu-yoshimus-projects.vercel.app/docs)

   注意：「scrapy-monotaro-katsu-yoshimus-projects」は1.の結果で書き替えてください。


3. このページからWebAPIの実行できる

## License

ライセンスは Apache2 License に準拠します。

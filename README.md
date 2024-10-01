# Vercel Scrapy Monotaro Project
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2Fvercel-scrapy-monotaro)

Monotaroの商品詳細ページをスクレーピングするためのWebAPIです。
Vercel上で動作します。上のボタンを押すとVercel＆Githubを新規作成できます。

なお、ローカルPCでも動作させたい場合は[Running Locally](#running-locally)を参照ください。

## 目次
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment on Vercel](#deployment-on-vercel)
- [License](#license)

## Installation

**前提：ローカルPCに git、ptyhon3.12 がインストール済**

1. **ローカルPCにリポジトリのクーロン作成:**

   ```cmd
   git clone https://github.com/katsu-yoshimu/vercel-fastapi.git
   cd vercel-fastapi
   ```

2. **ローカルPCに仮想完了作成と仮想環境アクティベート:**

	```cmd
	python -m venv venv
	venv\Scripts\activate
	```
3. **ローカルPCに必要なPythonパッケージをインストール:**
	```cmd
	pip install -r requirements.txt  
	pip install fastapi-cli
	```
   fastapi-cli はローカルPCで動作させたい場合のみ必要
   
## Running Locally
1. **WebAPIサーバ起動:**
```fastapi dev api/main.py```

2. **ブラウザで以下のURLでアクセス:**
```http://127.0.0.1:8000/docs```

3. このページからWebAPIの実行できる

## License
ライセンスは Apache2 License に準拠します。

# FastAPI Project
[![Deploy with Vercel](https://vercel.com/button)]([https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkatsu-yoshimu%2vercel-scrapy-monotaro])


This is a FastAPI project designed to be lightweight using FastAPI-Slim and ready for deployment on Vercel. It includes instructions for running the project locally using FastAPI-CLI.

## Table of Contents
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment on Vercel](#deployment-on-vercel)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```cmd
   git clone https://github.com/katsu-yoshimu/vercel-fastapi.git
   cd vercel-fastapi
	 ```

2. **Create and activate a virtual environment:**

	```cmd
	python -m venv venv
	venv\Scripts\activate
	```
3. **Install dependencies:**
	```cmd
	pip install -r requirements.txt  
	pip install fastapi-cli # This is required to use fastapi command locally
	```

## Running Locally
1. **Start the FastAPI server:**
```fastapi dev api/main.py```

2. **Open your browser and navigate to:**
```http://127.0.0.1:8000```

3. You should see your FastAPI application running.

## License
This project is licensed under the Apache2 License. Feel free to adjust any parts to better fit your specific project details and structure.

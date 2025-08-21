![main workflow](https://github.com/mongodb-developer/pymongo-fastapi-crud/actions/workflows/main.yml/badge.svg)

# PyMongo with FastAPI CRUD application

This is a simple CRUD application built using PyMongo and FastAPI. You can also follow the step-by-step [tutorial](https://www.mongodb.com/languages/python/pymongo-tutorial) for building this application.

## Running the server

Set your [Atlas URI connection string](https://docs.atlas.mongodb.com/getting-started/) as a parameter in `.env`. Make sure you replace the username and password placeholders with your own credentials.

```
ATLAS_URI=mongodb+srv://<username>:<password>@sandbox.jadwj.mongodb.net
DB_NAME=pymongo_tutorial
```

Install the required dependencies:

```
python -m pip install -r requirements.txt
```

Start the server:
```
python -m uvicorn main:app --reload
```

When the application starts, navigate to `http://localhost:8000/docs` and try out the `book` endpoints.

## Deploying to Vercel

This application can be deployed to Vercel. To do so:

1. Create a new project on Vercel and connect it to your GitHub repository
2. In the Vercel project settings, add the following environment variables:
   - `ATLAS_URI`: Your MongoDB Atlas connection string
   - `DB_NAME`: The name of your database (e.g., `ultimate_library`)
3. Vercel will automatically detect the `vercel.json` file and use it for deployment
## Running the tests

Install `pytest`:

```
python -m pip install pytest
```

Execute the tests:

```
python -m pytest
```

## Disclaimer

Use at your own risk; not a supported MongoDB product

FastAPI example app
fastapi-0.46.0-informational GitHub Workflow Status Twitter Follow Fast-Api-tests

This repository contains code for asynchronous example api using the Fast Api framework ,Uvicorn server and Postgres Database to perform crud operations on notes.

Installation method 1 (Run application locally)
Clone this Repo git clone (https://github.com/KenMwaura1/Fast-Api-example)
Cd into the Fast-Api folder cd Fast-Api-example
Create a virtualenv python3 -m virtualenv env
Activate virtualenv source /bin/activate
Cd into the src folder cd src
Install the required packages python -m pip install -r requirements.txt
Start the app using Uvicorn uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002
Ensure you have a Postgres Database running locally. Additionally create a Fast_api_dev db with user fast_api having required priviledges OR Change the DATABASE_URL variable in the .env file to reflect db settings (user:password/db)
Check the app on notes
Api documentation generated on docs
Installation method 2 (Run Locally using Docker)
1.Ensure Docker is installed 2.Ensure Docker Compose is installed 3.Clone this Repo git clone (https://github.com/KenMwaura1/Fast-Api-example)

4.cd Fast-Api-example

5.Use Docker-Compose to spin up containers docker-compose up -d --build

6.If everything completes should be available on notes

7.Docs are generated on docs

Tests
Tests are available using pytest Run them using pytest . while in the root directory (/Fast-Api-example)

Documentation
Open API Documentation is provided by Redoc

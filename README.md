# Project

## Setup and Launch

Follow the steps below to set up the environment and launch the project using Docker.

### Step 1: Create the `.env` configuration file

Copy the `.env.sample` file to a new `.env` file. This file will contain the necessary environment variables for project.

```bash
cp .env.sample .env
```
### Step 2: Start the container using Docker

To build and start all the required containers, run the following command:
```bash
docker-compose up --build 
```

### Step 4: Usage
Docs: http://0.0.0.0:8000/docs
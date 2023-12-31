Airflow Basics
---
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

- Clone this repo
- Install the prerequisites
- Run the service
- Check http://localhost:8080


### Prerequisites

- Install [Docker](https://www.docker.com/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

### Usage

Run the web service with docker

```
docker-compose up -d

# Build the image
# docker-compose up -d --build
```

Airflow UI: http://localhost:8080/
- Username : airflow
- Password : airflow

- `docker-compose logs` - Displays log output
- `docker-compose ps` - List containers
- `docker-compose down` - Stop containers

## Other commands

If you want to run airflow sub-commands and access airflow CLI:

- `docker-compose ps`
- `docker exec -it airflow_basics-airflow-scheduler-1 /bin/bash` - To Launch Airflow cli
- `docker-compose run --rm webserver airflow list_dags` - List dags
- `docker-compose run --rm webserver airflow test [DAG_ID] [TASK_ID] [EXECUTION_DATE]` - Test specific task

Airflow default config location:
- `docker cp airflow_basics-airflow-scheduler-1:/opt/airflow/airflow.cfg`

## flower UI 
To connect flower:
- `docker-compose down && docker-compose --profile flower up -d` - To know the celery worker details
- `http://localhost:5555/`- Flower UI

## Connect to database
To connect psql:
- `docker exec -it airflow_basics-postgres-1 /bin/bash`
- `psql -Uairflow`
If you want to use Ad hoc query, make sure you've configured connections:
Go to Admin -> Connections and Edit "postgres_default" set this values:
- Host : postgres
- Schema : airflow
- Login : airflow
- Password : airflow

## Connect Elastic Airflow docker
To start es docker:
- `docker-compose -f docker-compose-es.yaml up -d`

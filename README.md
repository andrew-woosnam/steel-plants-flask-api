# Global Steel Plant Counts API

This project is a Flask-powered API that provides access to a SQL database of global steel plant counts by country and production method, based on data from Global Energy Monitor's 2023 steel plant tracker.

## Prerequisites

- Docker
- Docker Compose (v2 should come bundled with docker CLI automatically)

## Getting Started

1. **Create a `.env` file** in the same directory as the `docker-compose.yml`.
2. **Add the following environment variables** to the `.env` file, replacing the placeholders with your actual details:

   ```plaintext
   POSTGRES_USER=<your_username>
   POSTGRES_PASSWORD=<your_password>
   POSTGRES_DB=<your_db_name>
   ```

3. **Save the .env file**. These variables will be used to configure the postgreSQL database when the container is created.

## Usage

1. Open a terminal and navigate to the directory containing `docker-compose.yml`.
2. Run `docker compose up` to build and start the container.
   - You can confirm the services are running with `docker compose ps`.
   - You can access the PostgreSQL database with `docker exec -it <container_name> psql -U <POSTGRES_USER> -d <POSTGRES_DB>`.
3. When finished, shut down with `docker compose down`.

## Tests

Unit tests can be run with `docker compose --profile test up` (this will spin up new containers).

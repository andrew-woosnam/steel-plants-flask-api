# Global Steel Plant Counts API

This project is a Flask-powered API that provides access to a PostreSQL database of global iron and steel plants by country and production method, based on data from Global Energy Monitor's 2023 steel plant tracker.

## Running with Docker Compose

To run this project using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your system.
2. Create a `.env` file at the root of the project with the following content:

   ```plaintext
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=pw
   POSTGRES_DB=iron_steel_production
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   FLASK_ENV=development
   RUN_TESTS=false
   ```

3. Run with `docker compose up`
4. Once the containers are running, the Flask API will be accessible at http://localhost:5000.
5. To stop and remove the containers, use `docker compose down`.

## Usage

- **List Countries**: GET /api/countries
  - Lists all countries with iron/steel plants.
  - e.g. `curl -X GET http://localhost:5000/api/countries`
- **Country Details**: GET /api/countries/<country_name>
  - Gets counts of each type of iron/steel plant for a specific country.
  - e.g. `curl -X GET http://localhost:5000/api/countries/Brazil`
- **List Plant Types**: GET /api/plants
  - Lists all plant types.
  - e.g. `curl -X GET http://localhost:5000/api/plants`
- **Plant Type Counts**: GET /api/plants/<plant_type>
  - Lists number of plants in each country for a specific plant type.
  - e.g. `curl -X GET http://localhost:5000/api/plants/electric`

# Data Processing and Analysis Pipeline

This repository hosts a Docker-based multi-container application designed for data processing and analytics. It integrates several key technologies: Dagster, PostgreSQL, dbt (data build tool), Jupyter Notebook, and Cube.js, providing a robust environment for data engineering and analytics tasks.

## Components
**Dagster:** A data orchestration platform for building, testing, and running data pipelines.
**PostgreSQL:** An advanced open-source relational database.
**dbt (data build tool):** A tool for transforming data in your warehouse more effectively.
**Jupyter Notebook:** A tool for creating and sharing documents with live code, visualizations, and narrative text.
**Cube.js:** A framework for building analytical web applications.

## Prerequisites
Docker and Docker Compose should be installed on your machine.
Familiarity with Docker, PostgreSQL, dbt, Jupyter Notebook, and Cube.js is beneficial.
Installation and Usage

Clone the Repository
```
git clone [repository-url]
```
Build and Run the Containers

In the cloned directory:
```
docker-compose up -d --build
```
## Accessing the Services

Dagster: Visit http://localhost:3000.

PostgreSQL: Connect at localhost:5432 (user: dagster, password: dagster).

dbt: Run commands using docker-compose exec.

Jupyter Notebook: Access at http://localhost:8888 (check logs for the token).

Cube.js: Developer playground at http://localhost:4000.

Stopping the Services
```
docker-compose down
```
## Data Persistence
**PostgreSQL data:** postgres_data Docker volume.
**Cube.js and dbt data:** stored in mounted volumes.

## Customization
Modify .env or Docker Compose file for environment variables.
Update dbt models in ./dbt.

Add Jupyter notebooks in the root directory.
##dbt Training with jaffle_shop
The jaffle_shop folder is included as a training module for dbt exercises. It contains sample models and data for users to practice and understand dbt concepts.

## Contributing
Contributions are welcome. Please adhere to this project's Code of Conduct.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


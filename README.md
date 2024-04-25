# COVID-19 Data Processing and Analysis System

This project aims to ingest, process, and analyze COVID-19 data from the Johns Hopkins University repository using modern data processing tools and Python. The system leverages PostgreSQL for data storage, mage.ai for data orchestration, dbt for data transformation, and Docker for containerization.

## Environment Setup

### Prerequisites

- Python 3.x
- PostgreSQL 16
- Visual Studio Code
- Docker

### Installation

1. **Python**: Ensure Python is installed. Check version with `python --version` or `python3 --version`.

2. **PostgreSQL**: Install PostgreSQL 16 and ensure it's running.

3. **SQLAlchemy**: Install SQLAlchemy for Python to interact with PostgreSQL.
   `pip install sqlalchemy`

5. **Pandas**: Install Pandas for data manipulation.
   `pip install pandas`
   
7. **DBeaver** (Optional): Install DBeaver or another database management tool.

8. **Docker**: Install Docker for containerization.

9. **dagster**: Install dagster for data orchestration. `pip install dagster dagit`

10. **dbt**: Install dbt for data transformation. `pip install dbt-postgres`

### Project Structure

- **data**: Directory for storing raw and processed data.
- **models**: Directory for dbt models.
- **scripts**: Directory for Python scripts.
- **docker**: Directory for Docker configuration files.

### Running the Project

1. **Data Ingestion**: Run the Python script to ingest data into PostgreSQL.
2. **Data Processing**: Use dbt to transform the data.
3. **Data Analysis**: Execute SQL queries or Python scripts to analyze the data.
4. **Orchestration**: Use mage.ai to orchestrate the data pipeline.

### Data Analysis Questions

- **Top 5 most common values**: What are the top 5 most common values in a particular column, and what is their frequency?
- **Metric change over time**: How does a particular metric change over time within the dataset?
- **Correlation between two columns**: Is there a correlation between two specific columns? Explain your findings.

### Docker Setup

- **Build**: Build the Docker image for your project.
  `docker build -t covid19-data-analysis`

- **Run**: Run the Docker container.
  `docker run -p 5432:5432 covid19-data-analysis`

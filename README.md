# NYC Taxi Data ETL Pipeline

This project is vert simple and mi first time using docker, it implements an ETL (Extract, Transform, Load) pipeline for processing NYC taxi trip data.
The pipeline extracts data from parquet files, transforms it using Pandas, and loads it into a PostgreSQL database. 

## 🏗️ Project Structure

```
etl_taxi/
│
├── data/                    # Data directory for with taxi trip parquet file
├── notebooks/              # Jupyter notebooks for EDA
│   └── taxi_analysis.ipynb
│
├── src/                    # Source code
│   ├── extract/           # Data extraction module
│   │   └── extract_data.py
│   └── database/          # Database operations
│       ├── setup.py
│       ├── connection.py
│       └── load_data.py
│
├── Dockerfile             # Dockerfile for the application
├── docker-compose.yml     # Docker Compose configuration
└── requirements.txt       # Python dependencies
```

## 🚀 Features

- Data extraction from parquet files
- Data transformation and cleaning
- PostgreSQL database integration
- Dockerized application and database
- Modular and maintainable code structure

## 📊 Data Processing

The pipeline processes the following data points:
- Pickup and dropoff timestamps
- Passenger count
- Trip distance
- Location IDs
- Payment information
- Fare details

## 🛠️ Technical Stack

- **Python 3.11**
- **Pandas** for data manipulation
- **PostgreSQL** for data storage
- **SQLAlchemy** for database operations
- **Docker** for containerization
- **Jupyter Notebooks** for analysis

## ⚙️ Setup and Installation

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd etl_taxi
   ```

2. **Set up the environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Using Docker**
   ```bash
   docker-compose up --build
   ```

## 🗄️ Database Schema

The transformed data is stored in a table with the following structure:
```sql
CREATE TABLE transformed_taxi_data (
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count FLOAT,
    trip_distance FLOAT,
    PULocationID INT,
    DOLocationID INT,
    payment_type TEXT,
    fare_amount FLOAT,
    tip_amount FLOAT,
    total_amount FLOAT
);
```

## 📝 Usage

***Using Docker**
   ```bash
   docker-compose up --build
  ```
That's it, Docker will handle all dependencies, database setup, and run the ETL pipeline

## 🔍 Data Analysis

The project includes a Jupyter notebook (`notebooks/taxi_analysis.ipynb`) that demonstrates:
- Data exploration
- Cleaning procedures
- Statistical analysis
- Data quality checks

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact
Jerson Enriquez - https://www.linkedin.com/in/jersonenriquezv/

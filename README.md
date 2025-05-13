## NYC Taxi Data ETL Pipeline

This project is very simple and it's my first time using Docker. It implements an ETL (Extract, Transform, Load) pipeline for processing NYC taxi trip data. The pipeline extracts data from Parquet files, transforms it using Pandas, and loads it into a PostgreSQL database.

---

### 🏗️ Project Structure

```text
etl_taxi/
│
├── data/                   # Data directory with taxi trip Parquet file
├── notebooks/              # Jupyter notebooks for EDA
│   └── taxi_analysis.ipynb
│
├── src/                    # Source code
│   ├── extract/            # Data extraction module
│   │   └── extract_data.py
│   └── database/           # Database operations
│       ├── setup.py
│       ├── connection.py
│       └── load_data.py
│
├── Dockerfile              # Dockerfile for the application
├── docker-compose.yml      # Docker Compose configuration
├── .env.example            # Example environment file
└── requirements.txt        # Python dependencies

### 🚀 Features
Permalink: 🚀 Features
- Data extraction from parquet files
- Data transformation and cleaning
- PostgreSQL database integration
- Dockerized application and database
- Modular and maintainable code structure
### 📊 Data Processing
Permalink: 📊 Data Processing
The pipeline processes the following data points:
- Pickup and dropoff timestamps
- Passenger count
- Trip distance
- Location IDs
- Payment information
- Fare details
### 🛠️ Technical Stack
Permalink: 🛠️ Technical Stack
- Python 3.11
- Pandas for data manipulation
- PostgreSQL for data storage
- SQLAlchemy for database operations
- Docker for containerization
- Jupyter Notebooks for analysis

### ⚙️ Setup and Installation
Permalink: ⚙️ Setup and Installation
1. Clone the repository
	```git clone https://github.com/yourusername/etl_taxi.git
cd etl_taxi
```

Permalink: Configure your environment variables
Create a .env file in the root directory (you can copy from .env.example):
```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database_name
DATABASE_URL=postgresql+psycopg2://your_username:your_password@db:5432/your_database_name
```


Permalink: Build and start with Docker
```
docker-compose up --build
```

### 🗄️ Database Schema
Permalink: 🗄️ Database Schema
The transformed data is stored in a table with the following structure:
```CREATE TABLE transformed_taxi_data (
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

### 📝 Usage
Permalink: 📝 Usage
*Using Docker
```docker-compose up --build
```
That's it, Docker will handle all dependencies, database setup, and run the ETL pipeline


### 🔍 Data Analysis
Permalink: 🔍 Data Analysis
The project includes a Jupyter notebook ( notebooks/taxi_analysis.ipynb) that demonstrates:
- Data exploration
- Cleaning procedures
- Statistical analysis
- Data quality checks
### 👥 Contributing
Permalink: 👥 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
### 📧 Contact
Permalink: 📧 Contact
Jerson Enriquez - https://www.linkedin.com/in/jersonenriquezv/

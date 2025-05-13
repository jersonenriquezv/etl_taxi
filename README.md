# NYC Taxi Data ETL Pipeline

This project implements an ETL (Extract, Transform, Load) pipeline for processing NYC taxi trip data. The pipeline extracts data from parquet files, transforms it using Pandas, and loads it into a PostgreSQL database.

## 🏗️ Project Structure

```
etl_taxi/
│
├── data/                    # Data directory with taxi trip parquet file
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

The pipeline processes the following data points from NYC taxi trips:
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

### Recommended Method: Using Docker 🐳

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd etl_taxi
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

That's it! Docker will handle all dependencies, database setup, and run the ETL pipeline automatically.

### Alternative Method: Local Setup (Optional)

If you prefer not to use Docker, you can set up the project locally, but note that you'll need to:
- Install PostgreSQL manually
- Configure the database connection
- Install Python 3.11
- Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🗄️ Database Schema

The transformed data is stored in a table with the following structure:
```sql
CREATE TABLE transformed_taxi_data (
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
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

The project comes with a sample NYC taxi trip dataset ready to use. Simply run:

```bash
# Using Docker (Recommended)
docker-compose up

# Without Docker (Not Recommended)
# Requires manual PostgreSQL setup and configuration
python src/database/load_data.py
```

The ETL pipeline will automatically:
1. Read the included parquet file
2. Transform the data
3. Load it into PostgreSQL

## 🔍 Data Analysis

The project includes a Jupyter notebook (`notebooks/taxi_analysis.ipynb`) that demonstrates:
- Data exploration
- Cleaning procedures
- Statistical analysis
- Data quality checks

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

[Your Name] - [Your Email/LinkedIn]

Project Link: [https://github.com/yourusername/etl_taxi]

## Setup Instructions

1. Clone the repository
2. Copy `.env.example` to `.env` and update with your credentials:
   ```bash
   cp .env.example .env
   ```
3. Update the `.env` file with your database credentials
4. Start the services with Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Environment Variables

The following environment variables are required:
- `POSTGRES_USER`: Database username
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `DATABASE_URL`: Full database connection string

## Project Structure

- `data/`: Contains the data files
- `src/`: Source code
- `notebooks/`: Jupyter notebooks
- `docker-compose.yml`: Docker services configuration

## Security Note

- Never commit the `.env` file
- Always use environment variables for sensitive data
- Keep credentials secure and never share them in the repository
from sqlalchemy import text
from connection import get_engine

engine = get_engine()

create_table_query = """
CREATE TABLE IF NOT EXISTS transformed_taxi_data (
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
"""

#Execute table creation 
def setup_database():
    with engine.connect() as conn:
        conn.execute(text(create_table_query))
        conn.commit()
    print("Table created successfully")

if __name__ == "__main__":
    setup_database()


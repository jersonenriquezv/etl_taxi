from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    """
    Get the SQLAlchemy engine for the database.
    """
    return create_engine(os.getenv("DATABASE_URL"))


if __name__ == "__main__":
    engine = get_engine()
    print(engine)


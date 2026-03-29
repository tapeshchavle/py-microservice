import pymysql
import os
from dotenv import load_dotenv

# Load env variables from .env File before running
load_dotenv()
from app.core.config import settings

def create_database():
    try:
        # Parse connection string manually to bypass SQLAlchemy for raw DB creation
        # format: mysql+pymysql://user:password@host:port/dbname
        db_url = settings.DATABASE_URL.replace("mysql+pymysql://", "")
        credentials, location = db_url.split("@")
        user, password = credentials.split(":")
        
        host_port, dbname = location.split("/")
        host, port = host_port.split(":")
        port = int(port)
        
        print(f"Connecting to MySQL at {host}:{port} as user '{user}'...")
        # Connect to MySQL Server (no db specified yet)
        connection = pymysql.connect(host=host, port=port, user=user, password=password)
        cursor = connection.cursor()
        
        print(f"Executing: CREATE DATABASE IF NOT EXISTS {dbname};")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname};")
        print("Database 'fastapi_db' created ensuring completed successfully!")
        
        connection.close()
    except Exception as e:
        print(f"Failed! Make sure your MySQL is running and credentials in .env are correct.\nError Details: {e}")

if __name__ == "__main__":
    create_database()

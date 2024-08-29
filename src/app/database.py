from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = "mariadb+mariadbconnector://myuser:myuserpassword@192.168.168.2:3306/mydatabase"

engine = create_engine(
    DB_URL
)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print(result.fetchone())
except Exception as e:
    print(f"Error: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
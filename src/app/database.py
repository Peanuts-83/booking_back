from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = "mariadb+mariadbconnector://myuser:myuserpassword@192.168.168.2:3306/mydatabase"

engine = create_engine(
    DB_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    """
    Function to yield a database session.

    * The function creates a new database session using SessionLocal().
    * It yields (return without terminating get_db function) the session, allowing it to be used within a context.
    * Finally, it ensures the session is closed after the context is exited.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
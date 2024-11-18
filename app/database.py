import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print(os.getenv('DB_URL'))
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DB_URL environment variable not set!")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

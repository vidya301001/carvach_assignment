from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/python_db'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Your database-related code here

# Close the connection explicitly if needed
engine.dispose()

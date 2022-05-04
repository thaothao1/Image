from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine= create_engine("postgresql://postgres:thaothao123@localhost/jobs",
    echo= True
    )
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)



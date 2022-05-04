from email.policy import default
from sqlalchemy import Integer,String,Boolean,Column,Text 
from models.database import Base

class Photo(Base):
    __tablename__= "photo"
    id = Column(Integer, primary_key = True)
    photo_name =  Column(String(255) , nullable= False , unique= True)
    photo_url = Column(String, nullable=False , unique = True)
    is_deleted = Column(Boolean , default=False) 
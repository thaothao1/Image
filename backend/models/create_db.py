from  models.database import Base,engine
from  models.Items import Item
from  models.Photo import Photo

print("Creating database .........")
Base.metadata.create_all(engine)

import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()


class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    category = Column(String, nullable=True, default="Waiting for category prediction")
    # image = image_attachment('product_image', nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    def save_to_db(self):
        sess = conn()
        sess.add(self)
        sess.commit()


def conn():
    engine = create_engine('sqlite:///db/products.sqlite3')
    Session = sessionmaker(bind=engine)
    sess = Session()
    return sess 
    
def init_db():
    sess = conn()
    product_1 = Product(name='Booda stone', description="Decor your living room with this beatiful product", image="fd75569f00649bda69d490d54e01378c.jpg", category="home decor & festive needs")
    sess.add(product_1)
    sess.commit()
    print('Produit ajouté à la bdd')


if __name__ == '__main__':
    engine = create_engine('sqlite:///db/products.sqlite3')
    Base.metadata.create_all(engine)
    init_db()
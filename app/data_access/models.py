from sqlalchemy import Column, String, DateTime, func, BigInteger, Integer, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "Product"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Numeric(10,2))
    model = Column(String)
    category = Column(String)
    stock = Column(Integer)
    image = Column(String)

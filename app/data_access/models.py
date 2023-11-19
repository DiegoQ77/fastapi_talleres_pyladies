from sqlalchemy import Column, String, DateTime, func, BigInteger, Integer
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# class Base(DeclarativeBase):
#     pass

class Test(Base):
    __tablename__ = "Test"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String)
    score = Column(Integer)
    
    # create_ts = Column("create_ts", DateTime, default=func.now())
    # update_ts = Column("update_ts", DateTime,
    #                    default=func.now(), onupdate=func.now())
   


# # Crea el motor de la base de datos
# engine = create_engine(DATABASE_URL)

# # Crea la tabla
# Base.metadata.create_all(bind=engine)

# # Crea la sesión de la base de datos
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
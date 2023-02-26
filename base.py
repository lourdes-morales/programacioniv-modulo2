from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#from sqlalchemy import create_engine
#from sqlalchemy.orm import declarative_base
#from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:UIP2023Root_@localhost/sqlalchemyDictionaryProd')
Session = sessionmaker(bind=engine)

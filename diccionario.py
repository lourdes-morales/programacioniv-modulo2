from sqlalchemy import Column, String, Integer
from base import Base

class Diccionario(Base):
    __tablename__ = 'diccionario'

    id = Column(Integer, primary_key=True)
    word = Column(String(50), unique=True)
    meaning = Column(String(200))

    def __repr__(self):
        return f"<Diccionario(word='{self.word}', meaning='{self.meaning}')>"
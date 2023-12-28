from sqlalchemy import create_engine, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column
import datetime
import os

DB = 'db04.sqlite3'
engine = create_engine('sqlite:///' + DB, echo=True)
session = Session(engine)


class Base(DeclarativeBase):
    pass


class Language(Base):
    __tablename__ = 'languages'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(32), unique=True)
    year = mapped_column(Integer)
    rating = mapped_column(Float)
    timestamp = mapped_column(DateTime, default=datetime.datetime.now)

    def __str__(self):
        return f'<{self.name} year={self.year} rating={self.rating}>'


if __name__ == '__main__':
    if os.path.exists(DB):
        os.remove(DB)
    Base.metadata.create_all(bind=engine)
    data = [
        Language(name='python', year=1991, rating=9.1),
        Language(name='java', year=1995, rating=7.8),
        Language(name='c++', year=1985, rating=7.7),
        Language(name='js', year=1995, rating=7.9),
    ]
    session.add_all(data)
    session.commit()


from sqlalchemy import create_engine, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, relationship
import datetime
import os

DB = 'db06.sqlite3'
engine = create_engine('sqlite:///' + DB, echo=True)
session = Session(engine)


class Base(DeclarativeBase):
    pass


class Pupil(Base):
    __tablename__ = 'pupils'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(32), unique=True)
    weight = mapped_column(Integer)
    mark = mapped_column(Float)
    sex = mapped_column(String(1))

    group_id = mapped_column(ForeignKey('groups.id'))
    group = relationship('Group', backref='pupils')

    def __repr__(self):
        return f'<{self.name}>'


class Group(Base):
    __tablename__ = 'groups'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(32), unique=True)
    teacher = mapped_column(String(32))
    # pupils

    def __repr__(self):
        return f'<<{self.name}>>'


if __name__ == '__main__':
    if os.path.exists(DB):
        os.remove(DB)
    Base.metadata.create_all(bind=engine)
    group1 = Group(name='1A', teacher='Mrs. Tompson')
    group2 = Group(name='1B', teacher='Mrs. Liner')
    pupils = [
        Pupil(name='John', mark=7.6, weight=51, sex='M', group=group1),
        Pupil(name='Mary', mark=11, weight=40, sex='F', group=group1),
        Pupil(name='Sam', mark=8.1, weight=55, sex='M', group=group2),
        Pupil(name='Jane', mark=10.2, weight=42, sex='F', group=group2),
    ]
    # session.add_all([group1, group2])
    session.add_all(pupils)
    session.commit()


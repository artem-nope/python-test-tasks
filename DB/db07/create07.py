from sqlalchemy import create_engine, Integer, String, Float, Text, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, relationship
import datetime
import os

DB = 'db07.sqlite3'
engine = create_engine('sqlite:///' + DB, echo=True)
session = Session(engine)


class Base(DeclarativeBase):
    pass


association_table = Table(
    'pupil_section',
    Base.metadata,
    Column('pupil_id', ForeignKey('pupils.id')),
    Column('section_id', ForeignKey('sections.id'))
)


class Pupil(Base):
    __tablename__ = 'pupils'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(32), unique=True)
    weight = mapped_column(Integer)
    mark = mapped_column(Float)
    sex = mapped_column(String(1))

    group_id = mapped_column(ForeignKey('groups.id'))
    group = relationship('Group', backref='pupils')

    # sections

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


class Section(Base):
    __tablename__ = 'sections'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(32), unique=True)
    pupils = relationship(Pupil, backref='sections', secondary=association_table)

    def __repr__(self):
        return f'<<<{self.name}>>>'

if __name__ == '__main__':
    if os.path.exists(DB):
        os.remove(DB)
    Base.metadata.create_all(bind=engine)
    group1 = Group(name='1A', teacher='Mrs. Tompson')
    group2 = Group(name='1B', teacher='Mrs. Liner')
    section1 = Section(name='football')
    section2 = Section(name='hip-hop')
    section3 = Section(name='fashion')
    pupils = [
        Pupil(name='John', mark=7.6, weight=51, sex='M', group=group1, sections=[section1, section2]),
        Pupil(name='Mary', mark=11, weight=40, sex='F', group=group1, sections=[section2, section3]),
        Pupil(name='Sam', mark=8.1, weight=55, sex='M', group=group2, sections=[section1, section2]),
        Pupil(name='Jane', mark=10.2, weight=42, sex='F', group=group2, sections=[section2, section3]),
    ]

    # session.add_all([group1, group2])
    session.add_all(pupils)
    session.commit()


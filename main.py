# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from importlib import resources

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import sqlite3

Base = declarative_base()


# https://realpython.com/python-sqlite-sqlalchemy/#the-model
vendor_resistor = Table(
    "vendor_resistor",
    Base.metadata,
    Column("vendor_id", ForeignKey("vendor.id")),
    Column("resistor_id", ForeignKey("resistor.id"))
)


class Resistor(Base):
    __tablename__ = 'resistor'
    id = Column(Integer, primary_key=True)

    # component_id: Mapped[int] = mapped_column(primary_key=False)
    vendors: Mapped[list["vendor"]] = relationship(secondary=vendor_resistor, back_populates='vendor')
    value = Column(Integer, nullable=False, default=0.0)
    cnt = Column(Integer, nullable=False, default=0)
    wattage = Column(Numeric, nullable=False, default=.25)
    tolerance = Column(Numeric, nullable=False, default=.10)  # 10 percent
    stock_number = Column(String(32), nullable=False, default='N/A')
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    __table_args__ = (
        PrimaryKeyConstraint('id', name='resistor_pk'),
    )


class Vendor(Base):
    __tablename__ = 'vendor'
    # id = Column(Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[list[Resistor]] = relationship(secondary=vendor_resistor)
    vendor_id: Mapped[int] = mapped_column(ForeignKey("resistor.id"))
    vendor_name = Column(String(64), nullable=False)
    vendor_url = Column(String(128), nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    __table_args__ = (
        PrimaryKeyConstraint('id', name='vendor_pk'),
    )



class Capacitor(Base):
    __tablename__ = 'capacitor'
    id = Column(Integer, primary_key=True)
    value = Column(Numeric, nullable=False, default=.01, comment='Capacitor in mmf or ppf')
    type = Column(String, nullable=False, default=.01, comment='Ceramic')
    volts = Column(Numeric, nullable=False, default=.01, comment='Volts')

    stock_number = Column(String(32), nullable=False, default='N/A')
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='capacitor_pk'),
    )


class Component(Base):
    __tablename__ = 'component'
    id = Column(Integer, primary_key=True)
    component_name = Column(String(128), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='component_pk'),
    )






# Press the green button in the gutter to run the script.
# https: // appdividend.com / 2020 / 10 / 14 / how - to - create - sqlite - database - in -python /
# create the database if it does not exist
# connect = sqlite3.connect('tronics.db')
# engine = db.create_engine('sqlite:///tronics.db')
# engine = db.create_engine("mysql+mysqldb://tronics:H0ppyB33r@localhost/tronics", isolation_level="READ UNCOMMITTED")
# engine = db.create_engine("mssql+pymssql://tronics:H0ppyB33r@localhost/tronics", isolation_level="AUTOCOMMIT")
# engine = db.create_engine("mssql+pymssql://tronics:H0ppyB33r@localhost")
# engine = db.create_engine("postgresql+psycopg2://postgres:TSaVDWNdRlujHXjld8A7@localhost:5432/tronics")
engine = db.create_engine("postgresql+psycopg2://tronics:tronics@localhost:5432/tronics")
connection = engine.connect()
metadata = db.MetaData()
# https: // overiq.com / sqlalchemy - 101 / defining - schema - in -sqlalchemy - orm /
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

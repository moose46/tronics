# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from importlib import resources
import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship, sessionmaker

from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import sqlite3
import models
from models import ProductType
from resistor_data import load_resistors

Base = declarative_base()


# https://realpython.com/python-sqlite-sqlalchemy/#the-model


class ProductType(Base):
    __tablename__ = 'product_type'
    id = Column(Integer, primary_key=True, nullable=False)
    # id: Mapped[int] = mapped_column(primary_key=True)
    # product_catalog_id: Mapped[int] = mapped_column(ForeignKey("product_catalog.id"))
    # product_catalog: Mapped[list["ProductCatalog"]] = relationship()
    name = Column(String(64), nullable=False, default="N/A")
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    __table_args__ = (
        PrimaryKeyConstraint('id', name='product_type_pk'),
    )


class ProductCatalog(Base):
    __tablename__ = "product_catalog"
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey("vendor.id"))
    value = Column(Integer, default=0, nullable=True)
    # product_type_id: Mapped[int] = mapped_column(primary_key=False)
    cnt = Column(Integer, nullable=False, default=0)
    wattage = Column(Numeric, nullable=True, default=.25)
    product_type = Column(String, nullable=False, default=.01, comment='Ceramic')
    volts = Column(Numeric, nullable=True, default=.01, comment='Volts')
    tolerance = Column(Numeric, nullable=True, default=.10)  # 10 percent
    stock_number = Column(String(32), nullable=True, default='N/A')
    created_on = Column(DateTime(), default=datetime.now, nullable=False)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='product_catalog_pk'),
    )


class Vendor(Base):
    __tablename__ = 'vendor'
    # id = Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True, nullable=False)
    # children: Mapped[list[Resistor]] = relationship(secondary=vendor_resistor)
    # vendor_id: Mapped[int] = mapped_column(ForeignKey("resistor.id"))
    vendor_name = Column(String(64), nullable=False)
    vendor_url = Column(String(128), nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    __table_args__ = (
        PrimaryKeyConstraint('id', name='vendor_pk'),
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
Session = sessionmaker(bind=engine)

session = Session()

# populate vendor table
tubes_and_more = Vendor(vendor_name='Tubes and More', vendor_url='https://www.tubesandmore.com/')
antique_radios = Vendor(vendor_name='Antique Radios', vendor_url='https://www.antiqueradios.com/')
hayseedhamfest = Vendor(vendor_name='Hayseed Hamfest LLC', vendor_url='https://hayseedhamfest.com/')
mouser = Vendor(vendor_name='Mouser Electronics', vendor_url='https://www.mouser.com/')
digikey = Vendor(vendor_name='Digikey Electronics', vendor_url='https://www.digikey.com/')
just_radios = Vendor(vendor_name='Just Radios', vendor_url='https://www.justradios.com/')
session.add_all([tubes_and_more, antique_radios, hayseedhamfest, mouser, digikey, just_radios])
session.commit()
# populate the product type table
load_resistors(session)

# add capacitors
capacitors = []
polypropylene_axial = ProductType(name="Capacitor Polypropylene, axial leads")
capacitors.append(polypropylene_axial)
orange_drop = ProductType(name="Capacitor Orange Drop")
capacitors.append(orange_drop)
session.add_all(capacitors)
session.commit()

# add inventory to the catalog
# catalog = []
# ra1m = ProductCatalog()
# ra1m.stock_number = "R-A1M"
# ra1m.product_type = metal_film_resistor.id
# ra1m.cnt = 5
# ra1m.tolerance = .5
# ra1m.vendor_id = tubes_and_more.id
# ra1m.value = 1e6
# ra1m.wattage = .5
# catalog.append(ra1m)
# session.add_all(catalog)
# session.commit()

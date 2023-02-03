__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, DateTime
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

#
# Author: Robert W. Curtiss
# models.py was created on January 31 2023 @ 3:01 PM
# Project: pythonTronics
#
Base = declarative_base()


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

#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    created = Column('created', String, nullable=True)
    title_size = Column('title_size', String, nullable=True)
    followers = Column('location', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    listing_text = Column('listing_text', String, nullable=True)
    shipping_price = Column('shipping_price', String, nullable=True)
    sellers_wardrobe = Column('sellers_wardrobe', String, nullable=True)
    bought_and_sold = Column('bought_and_sold', String, nullable=True)
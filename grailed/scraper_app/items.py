#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website grailed.com and
save to a database (postgres).

Scrapy item part - defines container for scraped data.
"""

from scrapy.item import Item, Field


class Grailed(Item):
    """Grailed container (dictionary-like object) for scraped data"""
    created = Field()
    title_size = Field()
    original_price = Field()
    followers = Field()
    listing_text = Field()
    shipping_price = Field()
    sellers_wardrobe = Field()
    bought_and_sold = Field()

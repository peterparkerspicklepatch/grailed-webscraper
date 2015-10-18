#! -*- coding: utf-8 -*-
"""
Web Scraper Project

Scrape data from a regularly updated website e.x. livingsocial.com and
save to a database (postgres).

Scrapy spider part - it actually performs scraping.
"""
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.loader import XPathItemLoader
from scrapy.loader.processors import Join, MapCompose

from scraper_app.items import Grailed


class GrailedSpider(Spider):
    """
    Spider for regularly updated grailed.com site.
    """
    name = "grailed"
    allowed_domains = ["grailed.com"]
    base_url = "https://www.grailed.com/listings/"
    start_urls = ["https://www.grailed.com/listings/100"]

    for url in range(100, 150):
        start_urls.append(base_url + str(i))

    item_fields = {
        'created': '//ul[@class = "horizontal-list listing-metadata-list clearfix"]/li[@class="horizontal-list-item listing-metadata-item"][1]/span[2]/text()',
        'title_size': '//h1[@class = "designer"]/div/text()',
        'original_price': '//ul[@class = "horizontal-list price-drops clearfix"]/li/text()',
        'followers': '//div[@class = "listing-followers"]/p/text()',
        #'listing_text': '//div[@class = "listing-description"]//p/text()',
        'shipping_price': '//div[@class = "listing-shipping"]/p/text()',
        'sellers_wardrobe': '//div[@class = "user-widget medium"]/a/text()',
        'bought_and_sold': '//div[@class = "user-widget-bottom"]/p[@class= "bought-and-sold"]/text()[1]',
        'feedback_score': '//div[@class = "green seller-score-top"]/text()[2]'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for url in selector.xpath(self.start_urls):
            loader = XPathItemLoader(Grailed(), selector=url)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()

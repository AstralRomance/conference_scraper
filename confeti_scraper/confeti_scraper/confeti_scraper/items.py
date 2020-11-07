# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ConferenceInfo(scrapy.Item):
    conference_name = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    logo_url = scrapy.Field()
    conference_url = scrapy.Field()
    report = scrapy.Field()

class Reports(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    complexity = scrapy.Field()
    tags = scrapy.Field()
    langugge = scrapy.Field()
    sources = scrapy.Field()
    authors = scrapy.Field()

class Speakers(scrapy.Item):
    speaker_name = scrapy.Field()
    avatar = scrapy.Field()
    bio = scrapy.Field()
    company = scrapy.Field()


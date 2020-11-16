# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ConferenceInfo(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    location = scrapy.Field()
    logo = scrapy.Field()
    url = scrapy.Field()
    report = scrapy.Field()

class Reports(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    complexity = scrapy.Field()
    tags = scrapy.Field()
    language = scrapy.Field()
    source = scrapy.Field()
    speakers = scrapy.Field()

class Speakers(scrapy.Item):
    name = scrapy.Field()
    avatar = scrapy.Field()
    bio = scrapy.Field()
    contactInfo = scrapy.Field()

class ContactInfo(scrapy.Item):
    company = scrapy.Field()
    twitterUsername = scrapy.Field()
    email = scrapy.Field()

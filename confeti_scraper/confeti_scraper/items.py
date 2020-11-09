# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ConferenceInfo(scrapy.Item):
    conferenceName = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    logoUrl = scrapy.Field()
    conferenceUrl = scrapy.Field()
    report = scrapy.Field()

class Reports(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    complexity = scrapy.Field()
    tags = scrapy.Field()
    language = scrapy.Field()
    sources = scrapy.Field()
    authors = scrapy.Field()

class Speakers(scrapy.Item):
    speakerName = scrapy.Field()
    avatar = scrapy.Field()
    bio = scrapy.Field()
    speakerContacts = scrapy.Field()

class ContactInfo(scrapy.Item):
    company = scrapy.Field()
    twitter = scrapy.Field()
    email = scrapy.Field()

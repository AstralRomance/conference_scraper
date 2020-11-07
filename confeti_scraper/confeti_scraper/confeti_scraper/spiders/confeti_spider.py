import scrapy
from confeti_scraper.items import ConferenceInfo, Reports, Speakers
from scrapy.http import Request

class ConfetiSpiderSpider(scrapy.Spider):
    name = 'confeti_spider'
    allowed_domains = ['2019.jokerconf.com']
    start_urls = ['https://2019.jokerconf.com']

    def __init__(self):
        self.conference = ConferenceInfo()
        self.next_page=''

    def parse(self, response):
        date_and_location = [i.strip() for i in response.xpath('//span[@class="hero__info "]/text()').getall()]
        self.conference['date'] = date_and_location[0]
        self.conference['location'] = date_and_location[1]
        self.conference['logo_url'] = ''.join((response.url,response.xpath('//a[@class="header__logo"]//img/@src').get()))
        self.conference['conference_url'] = response.url

        self.next_page=''.join((response.url,'/schedule/'))
        
        return Request(self.next_page, callback=self.parse_reports)

    def parse_reports(self, response):
        for frame in response.xpath('//div[@class="schedule__talk"]'):
             report_link = ''.join(('https://2019.jokerconf.com',frame.xpath('.//a[@class="link schedule__link"]/@href').get()))
             if ('bof' in report_link) or ('party' in report_link):
                 continue
             yield Request(report_link,
                           callback=self.parse_authors,
                           meta={'conference_info':response.meta.get('conference_info')})
             #for author_frame in frame.xpath('.//div[@class="schedule__talk-data"]'):
             #    speaker['speaker_name']=author_frame.xpath('.//a[@class="schedule__speaker-name"]/text()').extract()

    def parse_authors(self, response):
        speaker = Speakers()
        report = Reports()
        report['title'] = response.xpath('//h1[@class="talk_title"]/text()').get()
        report['description'] = response.xpath('//main[@class="talk-main"]//p/text()').get()
        speakers_list=[]
        for speaker_sec in response.xpath('//div[@class="talk-speaker"]'):
            speaker['speaker_name'] = speaker_sec.xpath('.//h5[@class="speaker-info_name"]/text()').get()
            speaker['avatar'] = speaker_sec.xpath('.//img[@class="img-fluid"]/@src').get()
            speaker['bio'] = speaker_sec.xpath('.//div[@class="speaker-info_bio"]//p/text()').get()
            speaker['company'] = speaker_sec.xpath('.//h6[@class="speaker-info_company"]/text()').get()
            speakers_list.append(speaker)
        report['authors'] = speakers_list
        self.conference['report'] = report
        yield self.conference

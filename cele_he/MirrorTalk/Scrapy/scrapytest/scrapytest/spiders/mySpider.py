import scrapy

class mySpider(scrapy.Spider):
    name = 'mySpider'
    start_urls = [
        # Kanye West to Joe Rogan
        'https://www.notion.so/The-Joe-Rogan-Experience-podcast-transcripts-listener-numbers-and-listener-demographics-4b2c0d5a7b0741c2b6ac5af374796f71'
    ]

    def parse(self, response, **kwargs):
        print(response.body)
# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from datetime import datetime

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    #start_urls = ['http://www.livecoin.net/en/']

    script = '''
        function main(splash , args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()
        end


    '''

    def start_requests(self):
        yield SplashRequest(url = 'https://www.livecoin.net/en/' , callback = self.parse , endpoint = "execute" , args ={
            'lua_source':self.script
        })

    def parse(self, response):
        for currency in response.xpath("//div[contains(@class , 'ReactVirtualized__Table__row tableRow___3EtiS')]"):
            yield{
                'Pair':currency.xpath('.//div[1]/div/text()').get(),
                'Date': datetime.now().strftime("/%d/%m/%Y %H:%M:%S"),
                'Volume':currency.xpath('.//div[2]/span/text()').get(),
                'Price':currency.xpath('.//div[3]/span/text()').get(),
                'Change':currency.xpath('.//div[4]/span/span/text()').get(),
                'High':currency.xpath('.//div[5]/span/text()').get(),
                'Low':currency.xpath('.//div[6]/span/text()').get()
            }

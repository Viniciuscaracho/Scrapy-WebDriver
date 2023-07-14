from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from selenium.webdriver.common.by import By
import csv
from scrapy_splash import SplashRequest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
import time

class ProcspiderSpider(scrapy.Spider):
    name = "ProcSpider"
    allowed_domains = ['app.procfy.io']
    start_urls = ['https://procfy.io/']
    
    rules = (
        Rule(LinkExtractor(allow= ''), callback='parse', follow=True),
    )
    
    def start_requests(self):
        yield SplashRequest(url='https://app.procfy.io/', callback=self.parse)
        
    def __init__(self):
        self.setup_selenium()

    def setup_selenium(self):
        s = Service('/caminho/para/o/chromedriver')
        options = {
            'proxy': {
                'http': 'http://<endereço_ip>:<porta>',
                'https': 'http://<endereço_ip>:<porta>',
                'no_proxy': 'localhost,127.0.0.1' 
            }
        }
        
        self.driver = webdriver.Chrome(service=s)

        self.driver.get('https://app.procfy.io/users/sign_in')

        email_input = self.driver.find_element('xpath', '//input[@id="user_email"]')
        email_input.send_keys('e-mail')

        time.sleep(1)

        password_input = self.driver.find_element('xpath', '//input[@id="user_password"]')
        password_input.send_keys('senha')

        time.sleep(1)
        password_input.send_keys(Keys.ENTER)
        resposta = HtmlResponse(url='https://app.procfy.io/', body= self.driver.page_source, encoding='utf-8')
        self.parse(resposta)
        time.sleep(4)

    def parse(self, response): 
        HtmlResponse(url='https://app.procfy.io/', body= self.driver.page_source, encoding='utf-8')
        bank_element = self.driver.find_element(By.XPATH, '//*[@id="bank_account_balance"]/div/button/div[1]')
        if bank_element:
            bank = bank_element.text.strip()
            data = {
                'bank': bank
            }
            yield data
            self.export_to_csv(data)

    def export_to_csv(self, data):
       
        filename = 'file.csv'
        fieldnames = ['bank']
        header = 'bank'

        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ProcspiderSpider) 
    process.start()
# libary for getting info from internet
import requests
# libary for parse html page,and work him
from bs4 import BeautifulSoup


class Convector(object):
    # create for describe user(bot-test)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}

    # Constructor
    def __init__(self, currencyFromExchange='USD', currencyToExchange='UAH'):
        self.currencyFromExchange = currencyFromExchange
        self.currencyToExchange = currencyToExchange

    def getURL(self):
        return f'https://www.google.com/search?q={self.currencyFromExchange}+TO+{self.currencyToExchange}'

    def getCurrencyPrice(self):
        try:
            # Create url for find info in Google <fromCurr> To <toCurr>
            linkInfoCurrency = f'https://www.google.com/search?q={self.currencyFromExchange}+TO+{self.currencyToExchange}'
            # GET HTML
            fullPage = requests.get(linkInfoCurrency, headers=self.headers)
            # PARSING
            parsePage = BeautifulSoup(fullPage.content, 'html.parser')
            # Find information
            findInfoCurrency = parsePage.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb'})
            # return <float> cost { <fromCurr> To <toCurr> }
            return float('.'.join((findInfoCurrency[0].text.split(','))))
        except ValueError:
            self.getCurrencyPrice()
        except IndexError:
            self.getCurrencyPrice()
        except TypeError:
            self.getCurrencyPrice()

    def convector(self,amount = 100):
        try:
            return  self.getCurrencyPrice() * amount
        except TypeError:
            self.convector()



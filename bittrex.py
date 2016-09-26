# program ini di buat oleh seorang anak muda yang sedang kesepian mencari jati dirinya
# program ini bersifat open source siapaun bisa menggunakan software ini dengan bebas
# program ini digunakan untuk trading bitcoin di market bittrex
# siapun yang menggunakan program ini , menaggung resiko sendiri
# program ini sudah di uji sendiri dengan akurasi 85 % keuntungan
# gunakan program ini pada coin yang bagus (Recommended : ETC , LSK , DASH)
# Jika program ini di rombak jangan lupakan share ya dan cantumkan nama coder awal dan yang revisi
# FIRST CODER : RAHMAT WAHYU HADI a.k.a bl4ckM4mba
# ---=== editted on september '16 by DANDY KALMA RAHMATULLAH a.k.a. bobi ===---

#!/usr/bin/env python
import urllib
import urllib2
import json
import time
import hmac
import hashlib

class apiBittrex(object):

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.public = ['getmarkets', 'getcurrencies', 'getticker', 'getmarketsummaries', 'getmarketsummary',
'getorderbook', 'getmarkethistory']
        self.market = ['buylimit', 'buymarket', 'selllimit', 'sellmarket', 'cancel', 'getopenorders']
        self.account = ['getbalances', 'getbalance', 'getdepositaddress', 'withdraw', 'getorder', 'getorderhistory',
'getwithdrawalhistory', 'getdeposithistory']


    def jsonAPI(self, method, values={}):
        if method in self.public:
            url = 'https://bittrex.com/api/v1.1/public/'
        elif method in self.market:
            url = 'https://bittrex.com/api/v1.1/market/'
        elif method in self.account:
            url = 'https://bittrex.com/api/v1.1/account/'
        else:
            return 'Something went wrong, sorry.'

        url += method + '?' + urllib.urlencode(values)

        if method not in self.public:
            url += '&apikey=' + self.key
            url += '&nonce=' + str(int(time.time()))
            signature = hmac.new(self.secret, url, hashlib.sha512).hexdigest()
            headers = {'apisign': signature}
        else:
            headers = {}

        req = urllib2.Request(url, headers=headers)
        response = json.loads(urllib2.urlopen(req).read())

        if response["result"]:
            return response["result"]
        else:
            return response["message"]


    def getmarkets(self):
        return self.jsonAPI('getmarkets')

    def getcurrencies(self):
        return self.jsonAPI('getcurrencies')

    def getticker(self, market):
        return self.jsonAPI('getticker', {'market': market})

    def getmarketsummaries(self):
        return self.jsonAPI('getmarketsummaries')

    def getmarketsummary(self, market):
        return self.jsonAPI('getmarketsummary', {'market': market})

    def getorderbook(self, market, type, depth):
        return self.jsonAPI('getorderbook', {'market': market, 'type': type, 'depth': depth})

    def getmarkethistory(self, market, count=20):
        return self.jsonAPI('getmarkethistory', {'market': market, 'count': count})

    def buylimit(self, market, quantity, rate):
        return self.jsonAPI('buylimit', {'market': market, 'quantity': quantity, 'rate': rate})

    def buymarket(self, market, quantity):
        return self.jsonAPI('buymarket', {'market': market, 'quantity': quantity})

    def selllimit(self, market, quantity, rate):
        return self.jsonAPI('selllimit', {'market': market, 'quantity': quantity, 'rate': rate})

    def sellmarket(self, market, quantity):
        return self.jsonAPI('sellmarket', {'market': market, 'quantity': quantity})

    def cancel(self, uuid):
        return self.jsonAPI('cancel', {'uuid': uuid})

    def getopenorders(self, market):
        return self.jsonAPI('getopenorders', {'market': market})

    def getbalances(self):
        return self.jsonAPI('getbalances')

    def getbalance(self, currency):
        return self.jsonAPI('getbalance', {'currency': currency})

    def getdepositaddress(self, currency):
        return self.jsonAPI('getdepositaddress', {'currency': currency})

    def withdraw(self, currency, quantity, address):
        return self.jsonAPI('withdraw', {'currency': currency, 'quantity': quantity, 'address': address})

    def getorder(self, uuid):
        return self.jsonAPI('getorder', {'uuid': uuid})

    def getorderhistory(self, market, count):
        return self.jsonAPI('getorderhistory', {'market': market, 'count': count})

    def getwithdrawalhistory(self, currency, count):
        return self.jsonAPI('getwithdrawalhistory', {'currency': currency, 'count': count})

    def getdeposithistory(self, currency, count):
        return self.jsonAPI('getdeposithistory', {'currency': currency, 'count': count})
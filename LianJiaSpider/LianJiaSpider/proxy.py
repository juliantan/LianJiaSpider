#_*_coding:utf-8_*_

import requests
import urllib2

class GetIp(object):
    """docstring for GetIp"""

    def get_proxy(self):
        return requests.get("http://101.200.39.75:5000/get/").content

    def delete_proxy(self,proxy):
        requests.get("http://101.200.39.75:5000/delete/?proxy={0}".format(proxy))

    def judge_ip(self,ip):
        proxyurl = "https://{0}".format(ip)
        testurl = "https://www.alipay.com/"
        try:
            req=urllib2.Request(url=testurl)
            req.set_proxy(proxyurl,"https")
            response=urllib2.urlopen(req,timeout=30)
        except Exception,e:
            print "Request Error:",e
            self.delete_proxy(ip)
            return False
        else:
            code=response.getcode()
            if code>=200 and code<300:
                print 'Effective proxy',ip
                return True
            else:
                print 'Invalide proxy',ip
                self.delete_proxy(ip)
                return False

    def get_UseIP(self):
        print "Proxy getip was executed."
        proxy = self.get_proxy()
        if self.judge_ip(proxy):
            return proxy
        else:
            self.get_UseIP()





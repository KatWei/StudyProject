import requests
import re
from setting import headers
from bs4 import BeautifulSoup as bs

class Parse:
    '''
    解析网页信息
    '''
    def __init__(self, htmlCode):
        self.htmlCode = htmlCode
        self.json = htmlCode.json()
        pass

    def parsePage(self):
        '''
        解析并计算页面数量
        :return: 页面数量
        '''
        totalCount = self.json['content']['positionResult']['totalCount']  # 职位总数量
        resultSize = self.json['content']['positionResult']['resultSize']  # 每一页显示的数量
        pageCount = int(totalCount) // int(resultSize) + 1  # 页面数量
        return pageCount

    def parseInfo(self):
        '''
        解析信息
        '''
        info = []
        for position in self.json['content']['positionResult']['result']:
            i = {}
            i['positionId'] = position['positionId']
            i['companyFullName'] = position['companyFullName']
            i['city'] = position['city']
            i['district'] = position['district']
            i['salary'] = position['salary']
            i['secondType'] = position['secondType']
            i['workYear'] = position['workYear']
            i['companySize'] = position['companySize']
            i['education'] = position['education']
            i['companyLabelList'] = position['companyLabelList']
            i['industryField'] = position['industryField']
            i['firstType'] = position['firstType']
            i['positionAdvantage'] = position['positionAdvantage']
            i['jobDetail'] = self.getJobDetail(position['positionId'])
            info.append(i)
        return info

    def getJobDetail(self, jobId):
        global bts
        url = 'https://www.lagou.com/jobs/%s.html' % (jobId)
        res = requests.get(url, headers=headers)
        html = res.text

        bts = ''
        soup = bs(html, 'html.parser')
        job_bt = soup.find_all('dd', class_='job_bt')
        if job_bt is not None:
            bts += ''.join([str(item.find_all('p')) for item in job_bt if item.find('p') != None])

        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filterdata = re.findall(pattern, bts)
        new_bts = ''.join(filterdata)
        return new_bts
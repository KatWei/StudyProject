from get_job_detail import getJobDetail

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
            i['jobDetail'] = getJobDetail(position['positionId'])
            info.append(i)
        return info
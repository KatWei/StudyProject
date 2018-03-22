import requests
import setting
import time
import xlwt
from parse import Parse


def getInfo(url, data):
    """
    获取信息
    """
    htmlCode = requests.post(url, data=data, headers=setting.headers)
    generalParse = Parse(htmlCode)
    pageCount = generalParse.parsePage()
    info = []
    for i in range(1, pageCount + 1):
        print("第%s页" % i)
        data['pn'] = str(i)
        htmlCode = requests.post(url, data=data, headers=setting.headers)
        generalParse = Parse(htmlCode)
        info = info + getInfoDetail(generalParse)
        time.sleep(2)
    return info

def getInfoDetail(generalParse):
    """
    页面解析
    """
    info = generalParse.parseInfo()
    return info

def processInfo(info, data, city):

    """
    信息存储:
    """
    try:
        ## 统计写入数据库
        excelTabel = xlwt.Workbook()  # 创建excel对象
        sheet1 = excelTabel.add_sheet('lagou', cell_overwrite_ok=True)
        sheet1.write(0, 0, '公司名')  # 公司名
        sheet1.write(0, 1, '城市')  # 城市
        sheet1.write(0, 2, '地区')  # 地区
        sheet1.write(0, 3, '薪资')  # 薪资
        sheet1.write(0, 4, '职位')  # 职位
        sheet1.write(0, 5, '工作年限')  # 工作年限
        sheet1.write(0, 6, '公司规模')  # 公司规模
        sheet1.write(0, 7, '学历')  # 学历
        sheet1.write(0, 8, '公司标签列表')  # 公司标签列表
        sheet1.write(0, 9, '行业领域')  # 行业领域
        sheet1.write(0, 10, '主要类型')  # 主要类型
        sheet1.write(0, 11, '职位福利')  # 职位福利
        sheet1.write(0, 12, '职位要求') #职位要求
        n = 1
        for job in info:
            sheet1.write(n, 0, job['companyFullName'])
            sheet1.write(n, 1, job['city'])
            sheet1.write(n, 2, job['district'])
            sheet1.write(n, 3, job['salary'])
            sheet1.write(n, 4, job['secondType'])
            sheet1.write(n, 5, job['workYear'])
            sheet1.write(n, 6, job['companySize'])
            sheet1.write(n, 7, job['education'])
            sheet1.write(n, 8, job['companyLabelList'])
            sheet1.write(n, 9, job['industryField'])
            sheet1.write(n, 10, job['firstType'])
            sheet1.write(n, 11, job['positionAdvantage'])
            sheet1.write(n, 12, job['jobDetail'])
            n+=1
        excelTabel.save('%s_%s.xls' % (city, data['kd']))
        return True
    except:
        return None


def main(url, data, city):
    if url:
        info = getInfo(url, data) #获取信息
        flag = processInfo(info, data, city)
        return flag
    else:
        return None

if __name__ == '__main__':
    job_name = input('请输入你要搜索的职业:\n')
    city = input('请输入城市：\n')
    isSchool = input('是否是校园招聘(1:是，0：否)：\n')
    gx_number = input('全职还是实习（1：全职，0：实习）：\n')
    if gx_number == '1':
        gx = '全职'
    else:
        gx = '实习'

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&gx=%s&city=%s&needAddtionalResult=false&isSchoolJob=%s' % (gx, city, isSchool)
    print('爬取%s_%s_%s' % (city, job_name, gx))
    data = {
        'first': 'false',
        'pn': 1,
        'kd': job_name
    }
    flag = main(url, data, city)
    if flag: print('爬取成功')
    else: print('爬取失败')
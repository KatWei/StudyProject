import requests
import re
from setting import headers
from bs4 import BeautifulSoup as bs

def getJobDetail(jobId):
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
    return  new_bts
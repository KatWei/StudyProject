import pandas as pd
import json
import numpy as np
import pymysql

def formatJobs(jobs, job_name, city):
    df = pd.read_json(json.dumps(jobs))
    df.index = df['positionId']  # 索引列用 positionId 替换
    del (df['positionId'])  # 删除原来的列
    df = df.sort_index()
    salary = df.salary.value_counts()
    salary_result = statistical(salary)

    district = df.district.value_counts()  ##区域
    district_result = statistical(district)

    education = df.education.value_counts()  ##学历
    education_result = statistical(education)

    workYear = df.workYear.value_counts()  ##工作年限
    workYear_result = statistical(workYear)


    number = df.index.value_counts().count()
    ## 写入数据库
    sql(job_name, city, district_result, salary_result, education_result, workYear_result, number)


def statistical(data):
    list = []
    for i in range(data.count()):
        list.append({data.index[i]: str(data.values[i])})
    return json.dumps(list)

def sql(job_name, city, district, salary, education, work_year, number):
    conn = pymysql.connect(
        host='localhost',
        port=33060,
        user='homestead',
        password='secret',
        db='python_job',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cur = conn.cursor()
    sql_query = '''insert into job_statistical(job_name, city, district, salary, education, work_year, number)
                            values('{job_name}', '{city}', '{district}', '{salary}', '{education}', '{work_year}', '{number}')'''
    sql = sql_query.format(
        job_name=job_name,
        city = city,
        district=pymysql.escape_string(district),
        salary=pymysql.escape_string(salary),
        education=pymysql.escape_string(education),
        work_year=pymysql.escape_string(work_year),
        number=number
    )
    state = cur.execute(sql)
    if state == 1:
        print("写入数据库完毕")
    else:
        print("写入数据库失败")

    conn.commit()
    cur.close()
    conn.close()
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


#路径
df = pd.read_excel('~/PycharmProjects/Test/job_lagou/xxx.xls')

df_sort = df.sort_index()
df = df_sort


def salaryStatistics():
    df['bottom'] = df['top'] = df['average'] = df['薪资']
    pattern = re.compile('([0-9]+)')


    for i in range(len(df['薪资'])):
        item = df['薪资'].iloc[i].strip()
        result = re.findall(pattern, item)
        try:
            df['bottom'].iloc[i], df['top'].iloc[i] = result[0], result[1]
            df['average'].iloc[i] = str((result[0] + result[1]) / 2)
        except:
            df['bottom'].iloc[i] = df['top'].iloc[i] = result[0]
            df['average'].iloc[i] = str(result[0]).strip()

    return df

def floatSalary():
    salaryStatistics
    pattern = re.compile('([0-9]+)')
    listi = []
    for i in range(len(df.average)):
        item = df.average.iloc[i].strip()
        result = re.findall(pattern, item)
        listi.append(float(result[0]))
    return listi

#绘制地区统计图
def DrawPieArea():
    area = df['地区'].value_counts()
    fig = plt.figure(1, facecolor = '#2f3542') #设置视图画布1
    ax = fig.add_subplot(3, 1, 1, facecolor = '#57606f', alpha = 0.3)
    plt.tick_params(colors='#FFFFFF')#设置轴的颜色为白色
    area.plot(kind = 'bar', rot = 0, color = '#747d8c')#画直方图

    plt.title(u'地区 ---- 职位数分布图', fontsize = 18, color = '#ff6b81')#设置标题
    plt.xlabel(u'地区', fontsize = 12, color = '#ff4757')#设置X轴
    plt.ylabel(u'职位数量', fontsize = 12, color = '#ff7f50')#设置Y轴

    ax.text(7, 600, u'地区总数: %s (个) ' % (area.count()), fontsize = 12, color = '#33CC99')
    ax.text(7, 500, u'职位总数: %s (条)' % (area.sum()), fontsize = 12, color = '#33CC99')

    list = df['地区'].value_counts().values
    # 添加每一个地区的坐标值
    for i in range(len(list)):
        ax.text(i - 0.3, list[i], str(list[i]), color='#70a1ff')

    fig.add_subplot(2, 1, 2)


    x = area.values
    label_list = []
    for i in range(5):
        t = x[i] / area.sum() * 100
        city = area.index[i]
        percent = str('%.1f%%' % t)
        label_list.append(city + percent)


    labels = label_list + [''] * int(area.count()- 5)
    explode = tuple([0.1]+ [0] * int(area.count() - 1))

    plt.pie(x,labels=labels, explode = explode, textprops={'color':'#CCCCFF'})
    plt.axis('equal')
    plt.savefig('地区职位_分布图.png', facecolor = fig.get_facecolor(), pip = 100)
    plt.close()
    print('地区职位_分布图制作成功')

#工作经验-职位数量及分布
def DrawWorkYear():
    work_year = df['工作年限'].value_counts()
    fig = plt.figure(2, facecolor= '#2F3542')
    ax = fig.add_subplot(3, 1, 1, facecolor = '#57606f', alpha = 0.3)
    plt.tick_params(colors = '#FFFFFF')
    work_year.plot(kind = 'bar', rot = 0, color = '#747D8C')
    plt.title('工作年限----职业分布图', fontsize = 18, color = '#FF6681')
    plt.xlabel('工作经验', fontsize = 12, color = '#FF4757')
    plt.ylabel('职业数量', fontsize = 12, color = '#FF7F50')

    ax.text(3, 600, '职位总数: %s (个) ' % (work_year.sum()), fontsize=12, color='#70A1FF')
    # 添加每一个地区的坐标值
    label_list = work_year.values
    for i in range(len(label_list)):
        ax.text(i - 0.1, label_list[i], str(label_list[i]), color='#33CC99')


    ax2 = fig.add_subplot(2, 1, 2)

    labels = list(work_year.index[:5]) + [''] * int(work_year.count() - 5)
    explode = tuple([0.1] * int(work_year.count()))
    plt.pie(label_list, labels = labels, explode = explode, autopct = '%1.1f%%', textprops= {'color':'#70A1FF'})
    plt.axis('equal')
    ax2.legend(loc='lower right', shadow = True, fontsize = 10, edgecolor = '#33CC99')
    plt.savefig('工作经验_分布图.png', facecolor=fig.get_facecolor(), pip=100)
    plt.close()
    print('工作经验_分布图制作成功')


#工作经验-平均月薪
def DrawAverageWorkYear():
    salaryStatistics()
    newDf = pd.DataFrame(data={'工作经验': df['工作年限'], '平均月薪': df['average']})
    newDf['平均月薪'] = floatSalary()

    grouped = newDf['平均月薪'].groupby(newDf['工作经验'])

    s3 = pd.Series(data = {'平均值': newDf['平均月薪'].mean()})

    result = grouped.mean().append(s3)

    matplotlib.style.use('ggplot')
    fig = plt.figure(3, facecolor= '#2F3542')
    ax = fig.add_subplot(1, 1, 1, facecolor = '#57606f', alpha = 0.3)
    result.sort_values(ascending= False).round(1).plot(kind = 'barh', rot = 0, color = '#ff6b81')

    plt.title('工作经验 ---- 平均月薪分布图', fontsize = 18, color = '#FF6681')
    plt.xlabel('平均月薪', fontsize = 12, color = '#FF4757')
    plt.ylabel('工作经验', fontsize = 12, color = '#FF7F50')

    salary_list = result.sort_values(ascending= False).values
    for i in range(len(salary_list)):
        ax.text(salary_list[i], i, str(int(salary_list[i])), color = '#33CC99')

    ax.text(20, 5, '月薪样本数: %s (个) ' % (df['薪资'].value_counts().count()), fontsize=12, color='#000000')
    plt.tick_params(colors = '#70A1FF')
    plt.savefig('工作经验_平均月薪_统计图.png', facecolor=fig.get_facecolor(), pip=100)
    plt.close()
    print('工作经验_平均月薪_统计图制作成功')

#工作地区-平均月薪
def DrawAveragArea():
    salaryStatistics()

    newDf = pd.DataFrame(data={'地区':df['地区'], '平均月薪': df['average']})
    newDf['平均月薪'] = floatSalary()

    grouped = newDf['平均月薪'].groupby(df['地区'])

    s4 = pd.Series(data = {'平均值':newDf['平均月薪'].mean()})

    result = grouped.mean().append(s4)

    matplotlib.style.use('ggplot')
    fig = plt.figure(4, facecolor='#2F3542')
    ax = fig.add_subplot(1, 1, 1, facecolor = '#57606f', alpha = 0.3)
    result.sort_values(ascending= False).round(1).plot(kind = 'bar', rot = 30, color = '#eccc68')

    plt.title(u'地区 ---- 平均月薪分布图', fontsize = 18, color = '#FF6681')
    plt.xlabel(u'地区', fontsize = 12, color = '#FF4757')
    plt.ylabel(u'平均月薪(K)', fontsize = 12, color = '#FF7F50')

    list_ = result.sort_values(ascending= False).values
    for i in range(len(list_)):
        ax.text(i-0.1, list_[i], int(list_[i]), color = '#33CC99')

    plt.tick_params(colors = '#70A1FF')
    plt.savefig('工作地区_平均月薪_统计图.png', facecolor=fig.get_facecolor(), pip=100)
    plt.close()
    print('工作经验_分布图制作成功')

#学历-职位数量
def Draweducation():
    education = df['学历'].value_counts()
    fig = plt.figure(5, facecolor= '#2F3542')
    ax = fig.add_subplot(2, 1, 1, facecolor = '#57606f', alpha = 0.3)
    education.plot(kind = 'bar', rot = 0)

    plt.title(u'最低学历 ---- 职位数分布图', fontsize = 18, color = '#FF6681')
    plt.xlabel(u'最低学历', fontsize = 12, color = '#FF4757')
    plt.ylabel(u'职位数量', fontsize = 12, color = '#FF7F50')

    plt.tick_params(colors = '#70A1FF', labelsize = 13)

    list_ = education.values
    for i in range(len(list_)):
        ax.text(i-0.1, list_[i], int(list_[i]), color = '#33CC99')

    ax2 = fig.add_subplot(2, 1, 2)
    xl = education.values
    labels = list(education.index)

    plt.pie(xl, labels= labels, autopct='%1.1f%%', textprops = {'color': '#eccc68'})
    plt.axis('equal')
    ax2.legend(loc = 'lower right', shadow = True, fontsize = 12, edgecolor = '#eccc68')
    plt.tick_params(colors='#70A1FF',labelsize=13)
    plt.savefig('学历_职位数量_统计图.png', facecolor=fig.get_facecolor(), pip=100)
    plt.close()
    print('学历_职位数量_统计图制作成功')

# 最低学历 - 平均月薪
def DrawMinEducationSalary():
    salaryStatistics()
    newDf = pd.DataFrame(data={'最低学历': df['学历'], '平均月薪': df['average']})

    newDf['平均月薪'] = floatSalary()

    grouped = newDf['平均月薪'].groupby(newDf['最低学历'])

    matplotlib.style.use('ggplot')

    fig = plt.figure(6, facecolor= '#2F3542')

    ax = fig.add_subplot(1, 1, 1, facecolor = '#57606f', alpha = 0.3)

    grouped.mean().round(1).sort_values().plot(color = '#33CC99')
    grouped.mean().round(1).sort_values().plot(kind = 'bar', rot = 0)

    plt.title(u'最低学历 ---- 平均月薪分布图', fontsize = 18, color = '#FF6681')
    plt.xlabel(u'最低学历', fontsize = 12, color = '#FF4757')
    plt.ylabel(u'平均月薪', fontsize = 12, color = '#FF7F50')

    list_ = grouped.mean().round(1).sort_values().values
    for i in range(len(list_)):
        ax.text(i-0.1, list_[i], str(list_[i]), color = '#1e90ff')


    plt.tick_params(colors = '#70A1FF')
    plt.savefig('最低学历_平均月薪_统计图.png', facecolor=fig.get_facecolor(), pip=100)
    plt.close()
    print('最低学历_平均月薪_统计图制作成功')

#最低学历 - 工作经验 - 平均月薪
def DrawMinEducationWorkSalary():
    salaryStatistics()

    newDf = pd.DataFrame(data={'平均月薪': df['average'], '最低学历': df['学历'], '工作经验': df['工作年限']})

    newDf['平均月薪'] = floatSalary()

    grouped = newDf['平均月薪'].groupby([newDf['最低学历'], newDf['工作经验']])

    matplotlib.style.use('dark_background')
    fig = plt.figure(7, facecolor= '#2F3542')
    ax = fig.add_subplot(1, 1, 1, facecolor = '#4f4f4f', alpha = 0.3)
    plt.title(u'最低学历 ---- 工作经验 ---- 平均月薪分布图', fontsize = 18, color = '#FF6681')
    plt.xlabel(u'最低学历', fontsize = 12, color = '#FF4757')
    plt.ylabel(u'平均月薪', fontsize = 12, color = '#FF7F50')
    plt.tick_params(colors = '#1e90ff')


    ind = np.arange(df['学历'].value_counts().count())
    width = 0.1
    label = []
    work_year =  list(df['工作年限'].value_counts().index)
    education_list = list(df['学历'].value_counts().index)
    for i in range(df['工作年限'].value_counts().count()):
        ylist = grouped.mean().round(1)[:, work_year[i]].reindex(education_list).values
        ax.bar(ind + width*(i-1) , ylist, width)
        label.append(ax.bar(ind + width*(i-1) , ylist, width)[0])

    ax.bar(ind, ylist, width)
    ax.set_xticklabels(education_list)
    ax.set_xticks(ind + width / 2)
    ax.legend(label, work_year, shadow=True,fontsize=12, facecolor = '#70A1FF')

    plt.grid(True)
    plt.savefig('最低学历_工作月薪_平均月薪_统计图.png', facecolor=fig.get_facecolor(), pip=100)
    plt.close()
    print('最低学历_工作月薪_平均月薪_统计图制作成功')


DrawPieArea()
DrawWorkYear()
DrawAverageWorkYear()
DrawAveragArea()
Draweducation()
DrawMinEducationSalary()
DrawMinEducationWorkSalary()


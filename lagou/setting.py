import random

ua_list=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
  ]


def get_headers():
    user_agent = random.choice(ua_list)
    temp_headers = {
        'Referer': 'https://www.lagou.com/jobs/list_%E4%BC%9A%E8%AE%A1?labelWords=&fromSearch=true&suginput=',
        'Cookie': '_ga=GA1.2.1497917413.1520233974; user_trace_token=20180305151254-9f87734b-2044-11e8-b126-5254005c3644; LGUID=20180305151254-9f8776ca-2044-11e8-b126-5254005c3644; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAGGABCB0DAEF31012FDB2FC8B20539796889518; hideSliderBanner20180305WithTopBannerC=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520233974,1520673101; _gid=GA1.2.1748260864.1520673101; LGSID=20180310171141-0b92aa2f-2443-11e8-a891-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DYc67njpS4ILoy2Qe5tvVPj1iVo-kaBcMeEKyEMb_rZC%26ck%3D5280.1.90.311.179.309.185.145%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3D87c27c8d000141e9000000065aa3a101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; X_HTTP_TOKEN=b5ee3320be04ee178d4b1fa6093de078; TG-TRACK-CODE=index_search; LGRID=20180310172811-5a1b3ffe-2445-11e8-a894-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520674092; SEARCH_ID=d1ef6d58ee864102ad5d20e3503fa641',
        'User-Agent':user_agent
    }
    return temp_headers

headers = get_headers()
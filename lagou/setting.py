import random

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
  ]


def get_headers():
    user_agent = random.choice(ua_list)
    temp_headers = {
        'Referer': 'https://www.lagou.com/jobs/list_%E4%BC%9A%E8%AE%A1?labelWords=&fromSearch=true&suginput=',
        'Cookie': 'JSESSIONID=ABAAABAAAFCAAEGF818C945EDE081E6A3AB87F911411ADC; _ga=GA1.2.949504101.1521722160; _gid=GA1.2.1425196686.1521722160; user_trace_token=20180322203600-93e76431-2dcd-11e8-b592-5254005c3644; LGSID=20180322203600-93e765ae-2dcd-11e8-b592-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DNLv2Eu-NXDQHmeGW4mMvQ2MeLhrf6flFEFAs6N-IM-3%26ck%3D5888.2.104.334.267.321.257.64%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3Df4ef57950009bc3b000000035ab3a328; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180322203600-93e76718-2dcd-11e8-b592-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521722163; TG-TRACK-CODE=index_search; _gat=1; index_location_city=%E6%B7%B1%E5%9C%B3; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521722704; LGRID=20180322204504-d7c1771d-2dce-11e8-b592-5254005c3644; SEARCH_ID=05121c7a60214bfaa2d06ea60fd75d57',
        'User-Agent':user_agent
    }
    return temp_headers

headers = get_headers()
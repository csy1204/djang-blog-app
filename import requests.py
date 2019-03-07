import requests
from bs4 import BeautifulSoup

def get_table_data_list(table_id):
    url = "https://everytime.kr/find/timetable/table/friend"
    payload = "identifier={}&friendInfo=true".format(table_id)
    headers = {
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en,ko;q=0.9,ja;q=0.8",
        'Connection': "keep-alive",
        'Content-Length': "47",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': "everytime.kr",
        'Origin': "https://everytime.kr",
        'Referer': "https://everytime.kr/",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
        'cache-control': "no-cache"}
    response = requests.request("POST", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    all_data_list = soup.find_all('data')
    return all_data_list

def extract_time_data(data_list):
    return [(eval(x['day']), eval(x['starttime']), eval(x['endtime'])) for x in data_list]

def create_table_array():
    return [[0 for _ in range(0,288)] for _ in range(0,5)]

def get_empty_array(table_arr, daynum=0):
    return [min_index for min_index, value in enumerate(table_arr[daynum]) if value < 1]

if __name__ == '__main__': 
    time_list = extract_time_data(get_table_data_list('9UEnRteJbEnSBzZDVoe7'))
    TABLE_ARRAY = create_table_array()
    
    for time in time_list:
        # 각 과목 시간을 불러와 TABLE_ARRAY에 1씩 더함
        for min_index in range(time[1], time[2]):
            TABLE_ARRAY[time[0]][min_index] += 1
            
    mon_empty_array = get_empty_array(TABLE_ARRAY, 0) # 0 == Monday, 4 == Friday
    print(mon_empty_array[108:]) #[108:] == After 9:00 A.M
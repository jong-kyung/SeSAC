from crawler.crawler import crawl_browser
from trans_file.trans_to_csv import SaveToCSV

# MelonChart = crawl_browser(
#     'https://www.melon.com/chart/index.htm',
#     '.wrap_song_info .rank01 a',
#     '.wrap_song_info .rank02',
#     '.wrap_song_info .rank03 a'
# )

GenieChart = crawl_browser(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20230711&hh=20&rtm=Y&pg=1',
    '.list .info .title',
    '.list .info .artist',
    '.list .info .albumtitle'
)
if __name__ == '__main__':
    print(GenieChart)
    SaveToCSV('genie', GenieChart)

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import re
import pandas as pd

delay = 3
browser = Chrome('/Users/janet/Desktop/youtube/chromedriver')
browser.implicitly_wait(delay)

#유튜브 top100인기 동영상 리스트 추출코드
url = 'https://www.youtube.com/feed/trending'
browser.get(url)
browser.maximize_window()

html_first = browser.page_source
html = BeautifulSoup(html_first, 'html.parser')
video_list = html.find_all('ytd-expanded-shelf-contents-renderer', {'class':'style-scope ytd-shelf-renderer'})
video = html.find('div', {'id':'grid-container', 'class':'style-scope ytd-expanded-shelf-contents-renderer'})
list_video = video.find_all('ytd-video-renderer', {'class':'style-scope ytd-expanded-shelf-contents-renderer'}) # youtube top 100개의 리스트수집

tester_url = [] #youtube top100 url 모아져 있는 list
for i in range(len(list_video)):
    youtube_url = 'www.youtube.com'
    each_url = youtube_url+list_video[i].find('a',{'id':'video-title'})['href']
    tester_url.append(each_url)

browser.quit()

'''

def get_information(url0):
    #각 동영상 별 정보 추출
    example_url = url0
    driver = Chrome('/Users/janet/Desktop/youtube/chromedriver')
    driver.get(example_url)
    html1 = browser.page_source
    soup = BeautifulSoup(html1, 'html.parser')
    video_info = soup.find('div', {'id': 'info-contents'})
    try:
        comment = soup.find('yt-formatted-string', {'class': 'count-text style-scope ytd-comments-header-renderer'}).text
    except:
        comment = '댓글없음'

    title = video_info.find('h1', {'class': 'title style-scope ytd-video-primary-info-renderer'}).text
    view = video_info.find('yt-view-count-renderer', {'class': 'style-scope ytd-video-primary-info-renderer'}).find('span').text
    like = video_info.find('div', {'id': 'top-level-buttons'}).find_all('yt-formatted-string')[0].text
    unlike = video_info.find('div', {'id': 'top-level-buttons'}).find_all('yt-formatted-string')[1].text
    tags1 = video_info.find('yt-formatted-string', {'class': 'super-title style-scope ytd-video-primary-info-renderer'}).find_all(text=re.compile('#+'))
    date0 = soup.find('div', {'id': 'date'})
    date = date0.find('yt-formatted-string', {'class': 'style-scope ytd-video-primary-info-renderer'}).text
    description = soup.find('div', {'id': 'description'})
    tags2 = description.find_all(text=re.compile('#+'))

    channel_info = soup.find('div', {'id': 'upload-info', 'class': 'style-scope ytd-video-owner-renderer'})
    channel_name = channel_info.find('yt-formatted-string', {'class': 'style-scope ytd-channel-name'}).find('a').text
    channel_count = channel_info.find('yt-formatted-string', {'class': 'style-scope ytd-video-owner-renderer'}).text

    df.loc[len(df)] = [title, view, like, unlike, date, tags1, tags2, channel_name, channel_count]

    driver.close()


df = pd.DataFrame(columns=("title", "view", "like", "unlike", "date", "tags1", "tags2", "채널명", "구독자수"))
get_information('https://www.youtube.com/watch?v=PV1gCvzpSy0')
print(df)
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

example_url = 'https://www.youtube.com/watch?v=PV1gCvzpSy0'
driver = webdriver.Chrome('/Users/janet/Desktop/youtube/chromedriver')
driver.get(example_url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

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
channel_count = channel_info.find('yt-formatted-string', {'class':'style-scope ytd-video-owner-renderer'}).text
df = pd.DataFrame(columns=("title", "view", "like", "unlike", "date", "tags1", "tags2", "채널명", "구독자수"))
df.loc[0]=[title, view, like, unlike, date, tags1, tags2, channel_name, channel_count]

print(df)
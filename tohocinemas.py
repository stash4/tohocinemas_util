'''
Utilities for TOHO Cinemas website
'''

import requests
from datetime import datetime
from bs4 import BeautifulSoup

BASE_URL = 'https://hlo.tohotheater.jp/'


def showing_list():
    '''
    Get a list of movies now showing.
    '''
    unix_time = datetime.now().strftime('%s')
    url = f'{BASE_URL}data_net/json/movie/TNPI3090.JSON?_dc={unix_time}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()


def movie_desc(mcode):
    '''
    Get a description of a movie specified by mcode.
    '''
    url = f'{BASE_URL}net/movie/TNPI3060J01.do?sakuhin_cd={mcode}'
    detail = requests.get(url)
    detail.encoding = detail.apparent_encoding

    detail_soup = BeautifulSoup(detail.text, 'html.parser')
    desc = detail_soup.find(property='og:description').get('content')
    return desc

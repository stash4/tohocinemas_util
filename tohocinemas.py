'''
Utilities for TOHO Cinemas website
'''

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import urllib

BASE_URL = 'https://hlo.tohotheater.jp'


def showing_list():
    '''
    Get a list of movies now showing.
    '''
    unix_time = datetime.now().strftime('%s')
    url = f'{BASE_URL}/data_net/json/movie/TNPI3090.JSON?_dc={unix_time}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()


def movie_desc(mcode):
    '''
    Get a description of a movie specified by mcode.
    '''
    url = f'{BASE_URL}/net/movie/TNPI3060J01.do?sakuhin_cd={mcode}'
    detail = requests.get(url)
    detail.encoding = detail.apparent_encoding

    detail_soup = BeautifulSoup(detail.text, 'html.parser')
    desc = detail_soup.find(property='og:description').get('content')
    return desc


def theater_list():
    '''
    Get a list of theaters.
    Retern json.
    '''
    unix_time = datetime.now().strftime('%s')
    url = f'{BASE_URL}/responsive/json/theater_list.json?_dc={unix_time}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()


def theater_schedule(vg_cd, show_day, term=99, isMember='', enter_kbn=''):
    '''
    Get a schedule of a theater specified by vitCD.
    '''
    type_ = 'json'
    unix_time = datetime.now().strftime('%s')

    query = urllib.parse.urlencode({
        '__type__': type_,
        'vg_cd': str(vg_cd),
        'show_day': str(show_day),
        'term': str(term),
        'isMember': isMember,
        'enter_kbn': enter_kbn,
        '_dc': unix_time
    })
    url = f'{BASE_URL}/net/schedule/TNPI3050J02.do?{query}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()

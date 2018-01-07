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


def theater_calender(
        vg_cd,
        show_day,
        term=99,
        seq_disp_term=7,
        isMember='',
        enter_kbn=''):
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
        'seq_disp_term': seq_disp_term,
        'isMember': isMember,
        'enter_kbn': enter_kbn,
        '_dc': unix_time
    })
    url = f'{BASE_URL}/net/schedule/TNPI3050J03.do?{query}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()


def showing_theater(mcode):
    '''
    Get theaters showing a specified movie.
    reference: /images_net/movie/:sakuhin_code/TNPI3060_2_:sakuhin_code.JSON
            ?_dc=:unix_time
    '''
    unix_time = datetime.now().strftime('%s')
    url = f'/images_net/movie/{mcode}/TNPI3060_2_{mcode}.JSON?_dc={unix_time}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()


def movie_schedule(
        mcode,
        vg_cd,
        show_day,
        term=99,
        isMember='',
        site_cd,
        enter_kbn=''):
    '''
    Get schedule of a specified movie in a specified theater.
    reference: /net/schedule/TNPI3070J01.do
            ?__type__=json&movie_cd=:sakuhin_code&vg_cd=:vit_group_code&show_day=:show_date&term=99&isMember=&site_cd=:site_id&enter_kbn=&_dc=:unix_time
    '''
    type_ = 'json'
    unix_time = datetime.now().strftime('%s')

    query = urllib.parse.urlencode({
        '__type__': type_,
        'movie_cd': mcode,
        'vg_cd': str(vg_cd),
        'show_day': str(show_day),
        'term': str(term),
        'isMember': isMember,
        'site_cd': site_cd,
        'enter_kbn': enter_kbn,
        '_dc': unix_time
    })
    url = f'{BASE_URL}/net/schedule/TNPI3070J01.do?{query}'

    res = requests.get(url)
    res.encoding = res.apparent_encoding
    return res.json()


def get_purchase_url(
        site_cd,
        show_day,
        theater_cd,
        screen_cd,
        pf_no,
        fnc=1,
        page_id='2000J01',
        enrter_kbn=''):
    '''
    Get url for reserving seats.
    reference: /net/ticket/:site_cd/TNPI2040J03.do
    '''

    query = urllib.parse.urlencode({
        'site_cd': site_cd,
        'jyoei_date': show_day,
        'gekijyo_cd': theater_cd,
        'screen_cd': screen_cd,
        'sakuhin_cd': moviecd,
        'pf_no': pf_no,
        'fnc': fnc,
        'pageid': page_id,
        'enter_kbn': enrter_kbn
    })
    url = f'{BASE_URL}/net/ticket/{site_cd}/TNPI2040J03.do?{query}'

    return url

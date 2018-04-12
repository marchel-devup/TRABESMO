#!/usr/bin/python3.4
# -- coding: utf-8 --

import requests
import bs4

def get_indicators(pair):
    url = 'https://www.investing.com/currencies/' + pair + '-technical'
    headers = {'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'}
    result = requests.get(url, headers=headers)

    parsed = bs4.BeautifulSoup(result.text, "html.parser")
    course = parsed.select('#last_last')
    if len(course) == 0:
        return 'Incorrect pair!\n'
    course = course[0].getText()
    names = parsed.select('.technicalIndicatorsTbl .symbol')
    values = parsed.select('.technicalIndicatorsTbl .right')
    decisions = parsed.select('.technicalIndicatorsTbl .textNum')
    decisions = decisions[1:]
    total = zip(list(map(lambda x: x.getText(), names)), list(map(lambda x: x.getText(), values)), list(map(lambda x: x.getText().strip(), decisions)))
    ret = '\n'.join(map(lambda x: ' '.join(x), total))
    ret = pair + ' ' + course + '\n' + ret
    return ret


def get_candels(pair):
    url = 'https://www.investing.com/currencies/' + pair + '-candlestick'
    headers = {'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'}
    result = requests.get(url, headers=headers)

    parsed = bs4.BeautifulSoup(result.text, "html.parser")
    course = parsed.select('.noHover ~ tr')
    print(course)
    return
    if len(course) == 0:
        return 'Incorrect pair!\n'
    course = course[0].getText()
    names = parsed.select('.technicalIndicatorsTbl .symbol')
    values = parsed.select('.technicalIndicatorsTbl .right')
    decisions = parsed.select('.technicalIndicatorsTbl .textNum')
    decisions = decisions[1:]
    total = zip(list(map(lambda x: x.getText(), names)), list(map(lambda x: x.getText(), values)), list(map(lambda x: x.getText().strip(), decisions)))
    ret = '\n'.join(map(lambda x: ' '.join(x), total))
    ret = pair + ' ' + course + '\n' + ret
    return ret
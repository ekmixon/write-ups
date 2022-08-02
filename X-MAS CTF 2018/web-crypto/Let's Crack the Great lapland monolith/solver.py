#!/usr/bin/python3

import re
import requests


def extract_number(html):
    number = re.search('<br>(\d+)<br>', html)[1]
    return int(number)


def detect_period(url, session):
    numbers = []
    while True:
        html = session.get(url).text
        number = extract_number(html)
        if number in numbers:
            print(f'FOUND PERIOD: {len(numbers)}')
            break
        numbers.append(number)
    index = numbers.index(number)
    return numbers[index:]


if __name__ == '__main__':
    numbers_count = 20
    url = 'http://199.247.6.180:12000/?guess=12345'
    session = requests.session()
    numbers = detect_period(url, session)
    print('PHPSESSID=' + session.cookies['PHPSESSID'])
    print(f'NEXT {numbers_count} NUMBERS ARE:')
    for i in range(numbers_count):
        print(numbers[i]) 

"""
Mission 1: get data from internet and save as csv file.
"""

import urllib.request as req
import json
import csv
import bs4
import re


def public_api_access(src):
    with req.urlopen(src) as response:
        data = json.load(response)
        attractions_lst = data['result']['results']

    with open('data.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)  # writer object

        for attraction in attractions_lst:
            year = int(attraction['xpostDate'].split('/')[0])
            if year >= 2015:
                spot_name = attraction['stitle']
                district = attraction['address'].split('  ')[1][:3]
                longitude = attraction['longitude']
                latitude = attraction['latitude']
                # img = re.findall('(.*)https', attraction["file"])
                img = attraction['file'].split('http')[1]
                img = 'http' + img
                csv_writer.writerow([spot_name, district, longitude, latitude, img])


"""
Mission 2: get data from ptt movie forum and save as txt file.
"""


def ptt_crawler(url, title_lst, pages):

    while pages > 0:
        request = req.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                          ' Version/15.4 Safari/605.1.15'
        })

        # get PTT HTML
        with req.urlopen(request) as response:
            html_file = response.read().decode('utf-8')
        root = bs4.BeautifulSoup(html_file, 'html.parser')  # parse HTML format

        # get some particular titles
        title_lst.extend(ptt_title(root))

        # get next page's url
        url = ptt_next_page(root)
        pages -= 1

    return title_lst


def ptt_title(root):
    lst = []
    titles = root.select('.title')  # select all class='title'
    for title in titles:
        if title.a is not None:
            if re.search('^\[好雷\]', title.a.text) or re.search('^\[普雷\]', title.a.text) or re.search('^\[負雷\]', title.a.text):
                lst.append(title.a.text)
    return lst


def ptt_next_page(root):
    next_page = root.find('a', string='‹ 上頁')  # get next page link by anchoring <a>'s  inner text "< 上頁"
    return 'https://www.ptt.cc' + next_page['href']


def main():
    """
    to run mission 1 & 2's functions
    """
    # for public API access
    attractions_src = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
    public_api_access(attractions_src)

    # for ptt movie crawler
    movie_url = 'https://www.ptt.cc/bbs/movie/index.html'
    title_lst = []
    title_lst = sorted(ptt_crawler(movie_url, title_lst, 10))
    with open('movie.txt', 'w', encoding='utf-8') as file:
        for t in title_lst:
            file.write(t + '\n')


if __name__ == "__main__":
    main()

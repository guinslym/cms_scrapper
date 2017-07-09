import re
import urllib2
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True


def get_cmss():

    page = urllib2.urlopen("https://github.com/postlight/awesome-cms")
    soup = BeautifulSoup(page.read(), "html.parser")

    p = re.compile('\x85[[0-9,]+')

    cmss = {}
    sorted_cms_list = []
    for cms in soup.find_all('b'):
        title = cms.text
        parent = cms.parent.parent
        try:
            stars = p.findall(str(parent))[0][1:]
        except IndexError:
            pass
        cmss[title] = int(stars.replace(',', ''))

    for key, value in sorted(cmss.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        sorted_cms_list.append([key, value])

    return sorted_cms_list


@app.route('/', cors=True)
def index():
    return {'cmss': get_cmss()}
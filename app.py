import re
from urllib.request import urlopen
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True


def get_cmss():

    page = urlopen("https://github.com/postlight/awesome-cms")
    soup = BeautifulSoup(page.read(), "html.parser")

    p = re.compile('\x85[[0-9,]+')

    cmss = {}
    sorted_cms_list = []
    for cms in soup.find_all('b'):
        title = cms.text
        cmss[title] = title
    return cmss

   
 
@app.route('/')
def home():
  return render_template('ranking.html', cmss=get_cmss())
import re
 
if __name__ == '__main__':
  app.run(debug=True)
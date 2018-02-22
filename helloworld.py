from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import bs4

app = Flask(__name__)

@app.route('/')
def work():
	return render_template("main.html")

@app.route('/xidian')
def xidian():
	try:
		r = requests.get("http://yz.xidian.edu.cn/list-16.html", timeout=10)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		demo = r.text
		soup = BeautifulSoup(demo, "html.parser")
		mylist = []
		for t in soup.find('div', id='content2').children:
			if isinstance(t, bs4.element.Tag):
				t1 = t.find('a')
				t2 = t.find('div', id='lright')
				if isinstance(t2, bs4.element.Tag):
					mylist.append([t1.get('href'), t1.string, t2.string])
		return render_template("xidian.html", content=mylist[0:5])
	except:
		return 'failed!'

@app.route('/hrbeu')
def hrbeu():
	try:
		r = requests.get("http://yzb.hrbeu.edu.cn/3279/list.htm", timeout=10)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		demo = r.text
		soup = BeautifulSoup(demo, "html.parser")
		mylist = []
		for t in soup.find('ul','wp_article_list').children:
			if isinstance(t, bs4.element.Tag):
				t1 = t.find('a')
				t2 = t.find('span', 'Article_PublishDate')
				mylist.append([t1.get('href'), t1.get('title'), t2.string])
		return render_template("hrbeu.html", content=mylist[0:5])
	except:
		return 'failed!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

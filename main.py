import sys
import urllib.request
import re
import requests

page = urllib.request.urlopen(sys.argv[1])
html_page = page.read().decode("utf-8")

pattern = "<Key.*?>.*?</Key.*?>"
match_results = re.findall(pattern, html_page)
url_list = []
for x in match_results:
	x = re.sub("<.*?>", "", x)
	x = sys.argv[1] + x
	if requests.get(x).status_code == 200:
		url = x
		r = requests.get(x, allow_redirects=True)
		if url.find('/'):
			filename = (url.rsplit('/', 1)[1])
			open(filename, 'wb').write(r.content)

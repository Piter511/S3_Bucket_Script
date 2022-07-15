## https://dsecure.s3-ap-southeast-1.amazonaws.com/
#!/usr/bin/python

import sys
import urllib.request
import re
import requests

page = urllib.request.urlopen('https://dsecure.s3-ap-southeast-1.amazonaws.com/')
html_page = page.read().decode("utf-8")

pattern = "<Key.*?>.*?</Key.*?>"
match_results = re.findall(pattern, html_page)
main_url = 'https://dsecure.s3-ap-southeast-1.amazonaws.com/'
url_list = []
for x in match_results:
	x = re.sub("<.*?>","", x )
	x = main_url + x
	if requests.get(x).status_code == 200:
		url = x
		r = requests.get(x, allow_redirects=True)
		if url.find('/'):
			filename=(url.rsplit('/', 1)[1])
			open(filename, 'wb').write(r.content)
import requests
import re

link = input()
r = requests.get(link)

links = re.findall('((\w+:\/\/){0,1}[\w\-]+\.[\w\-\.]+)', r.text)

for i in range(len(links)):
	link, waste = links[i]
	links[i] = re.sub('["|\'](\w+:\/\/){0,1}', "", link)

for link in sorted(set(links)):
	print(link)
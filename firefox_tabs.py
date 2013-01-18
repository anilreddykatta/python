import json
f = open("sessionstore.js", "r")
jdata = json.loads(f.read())
f.close()
for win in jdata.get("windows"):
	for tab in win.get("tabs"):
		i = tab.get("index") - 1
		print tab.get("entries")[i].get("url")


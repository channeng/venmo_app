import urllib, json

key = "75d5e8fb7f47e2adcf71c9b86c5abd59327fe4fb88e4fd74e093b6d661115c07"
# raw_input("What is your access token?")
# 
key_param = "access_token="+str(key)
domain = "https://api.venmo.com/v1/payments?"

def returnJson(url):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return data

def returnData(returnJson_object):
	return returnJson_object["data"]

def pagination(returnJson_object):
	url = returnJson_object["pagination"]["next"]
	return url
print

def transactions(domain,key_param):
	url = domain + key_param
	response = returnJson(url)
	dump = returnData(response)
	if len(dump) == 20:
		next_page = pagination(response)
		domain = next_page+"&"
		dump.append(transactions(domain,key_param))
	else:
		return dump

print len(transactions(url))
# print 

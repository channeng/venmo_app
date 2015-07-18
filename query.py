import urllib, json

key = ""
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
	data = returnData(response)
	next_page_url = pagination(response)
	dump = [data,next_page_url]
	return dump

def all_transactions(domain,key_param):
	all_data = []
	page_counter = 1
	response = transactions(domain,key_param)
	response_data = response[0]
	response_nxtpg = response[1]+"&"
	for i in response_data:
		all_data.append(i)
	print str(page_counter) + "..."

	while len(response_data) == 20:
		page_counter += 1
		print str(page_counter) + "..."
		response = transactions(response_nxtpg,key_param)
		response_data = response[0]
		for i in response_data:
			all_data.append(i)
		try:
			response_nxtpg = response[1]+"&"
		except TypeError:
			break
	else:
		print "dumped!"
		return dump

	return all_data

# print 

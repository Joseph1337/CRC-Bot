import requests
from selenium import webdriver
from datetime import date
import json

s = requests.Session()

def login(username, password):
	url = "https://mycrc.gatech.edu/Account/Login"
	payload = {
		# "__RequestVerificationToken": "C1RfKJv7kUwkNkQiwXXI3kt2cfF155kKj0fAKiwHakPhzG-g1Iyy0aj_Gmw_OdZJK0GLWD3pbrYVM0pF7P1reYzTSoRss_aa2hvZuLzWNzo1",
		"UserName": username,
		"Password": password,
		"returnUrl": "/booking"
	}
	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'ASP.NET_SessionId=cshknxzcoqotozcpxnaque4e; _ga=GA1.2.923792453.1611208685; _gid=GA1.2.819544617.1611208685; __RequestVerificationToken=zUrmxehmINZwqu65YzKkCpfwufkEmbwzK465nseORCf8bpcY_ixEjtOcrX5i9KcjmvEObov_LRZGAokD-q72-CJf4fawIjx7-17M-zBhsZU1; .AspNet.Correlation.JasigCas=vMrewS9eZnoX1tWAoBfPRySS6hLK2Cb72lnW4sGOCY4',
		'origin': 'https://mycrc.gatech.edu',
		'referer': 'https://mycrc.gatech.edu/booking',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}
	# s.get(url)
	response = s.post(url, data=payload, headers=headers)
	cookie = response.headers
	# print(s.cookies)
	return cookie
	# return response.status_code


def getTimeSlotId():
	url = "https://mycrc.gatech.edu/booking/9cefff00-4032-42bc-b803-faaf360551b1/slots/db2dba86-c38a-4836-9b48-739f448bd01a/" + date.today().strftime("%Y/%m/%d")
	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"origin": "https://mycrc.gatech.edu",
		"cookie": cookie,
		# "cookie": ".AspNet.ApplicationCookie=jiEfCQXHN6weST_-bmE6B1sVweNLfQVaaxczwQ_1My0YOZc5TfXm2xY2B5GKQIbBCVJLn7VVqtbvtpYkl6XsFZG4CfpOrbWXPyqSUb0lo9jW8EoPNGiHgwlQu7DpLZ4PsxqqbNRkwJuLUdGokdcT1GG4kdyRcCyCwwvgkEuwSzcnL4xeqxUXm-N4mTHpdltP3qySg0dFDrRormXvkDA8MfyXEvWbj6i5vqQqtIoqUWkNnztbDfA_lZswEoPm5SFUlMutJTm3VsuQZqQaEVCwwnn4nbXLPrYp-t1IQmwnf3unqO1BT6sx7rnq7ZpGm4XZCINwRKq3_eNeXgKt5xH8HEdzOPWwk9I10YJITocoTTgq6RyNn6R1oO8p2hwqiO3U",
		"referer": "https://mycrc.gatech.edu/booking/9cefff00-4032-42bc-b803-faaf360551b1",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
		
	}
	response = s.get(url, headers=headers).content
	return response







# def reserveSlot():
# 	login("jguo345", "562dfc11!")
# 	url = "https://mycrc.gatech.edu/booking/reserve"
# 	headers = {
# 		"accept": "*/*",
# 		"accept-encoding": "gzip, deflate, br",
# 		"cookie": "cookieControl=true; cookieControlPrefs=[]; _gid=GA1.2.231961476.1611030909; IDMSESSID=BBF0340607F09D79300F85EA44D39ECEDE0A8BC763FAC01D1B5F088E67F7230D3F533252BC5018C558E1B30F1F4F7F7039429CEA2837F8A8D0E3FFDDEBEC4F4B; _ga_H8D0W56W45=GS1.1.1611188387.7.1.1611188977.0; _ga=GA1.2.1435811860.1589061223; ASP.NET_SessionId=npsgwngakufr43okfwwaujzd; __RequestVerificationToken=u1lTNpN41IbJ0JoKVzwDgjgQU_Avbvro2-dOv7BOsdRoLR-UqnN8Cx5oTOAEBiawsE0BzEswiKPerxmOS83LbZBo4a93h2OoFKfZP0gszRI1; _gat=1",
# 		"origin": "https://mycrc.gatech.edu",
# 		"referer": "https://mycrc.gatech.edu/booking/9cefff00-4032-42bc-b803-faaf360551b1",
# 		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# 	}
# 	form_data = {
# 		"bookingId": "9cefff00-4032-42bc-b803-faaf360551b1",
# 		"facilityId": "db2dba86-c38a-4836-9b48-739f448bd01a",
# 		"appointmentId": "846bae04-de9a-44cf-b0f1-bffeff2e7a1e",
# 		"timeSlotId": "c025beca-125c-4a01-9531-54539cd0fe61",
# 		"timeSlotInstanceId": "afa5ea0c-9bfb-4555-a770-5b1694debcbc",
# 		"year": 2021,
# 		"month": 1,
# 		"day": 22
# 	}
# 	response = requests.post(url, headers=headers, data=json.dumps(form_data))
# 	return response


# login("jguo345", "562dfc11!")




# bookingId: 9cefff00-4032-42bc-b803-faaf360551b1
# facilityId: db2dba86-c38a-4836-9b48-739f448bd01a
# appointmentId: 846bae04-de9a-44cf-b0f1-bffeff2e7a1e
# timeSlotId: c025beca-125c-4a01-9531-54539cd0fe61
# timeSlotInstanceId: afa5ea0c-9bfb-4555-a770-5b1694debcbc
# year: 2021
# month: 1
# day: 22


# Reserve(appointmentId, timeSlotId, timeSlotInstanceId)
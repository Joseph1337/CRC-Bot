import requests
from datetime import datetime, timedelta
from lxml import html
from bs4 import BeautifulSoup as bs
import json

s = requests.Session()



def login(username, password):
	url = "https://mycrc.gatech.edu/Account/Login"
	# tokenUrl = 'https://mycrc.gatech.edu/Account/GetLoginOptions'
	
	# query_params = {
	# 	'returnURL': '/',
	# 	'isAdmin': 'false'
	# }
	
	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'cookieControl=true; cookieControlPrefs=[]; _gid=GA1.2.231961476.1611030909; ASP.NET_SessionId=npsgwngakufr43okfwwaujzd; __RequestVerificationToken=u1lTNpN41IbJ0JoKVzwDgjgQU_Avbvro2-dOv7BOsdRoLR-UqnN8Cx5oTOAEBiawsE0BzEswiKPerxmOS83LbZBo4a93h2OoFKfZP0gszRI1; IDMSESSID=5565B3C00B3C85EF6F34FE911EA06AF14C7CF7386891229FD7D882612BE7F086B6144B08A0E9E5E27749BB612C41898C991710B52A881CFE2D11DFD0C74CBFA7; _ga_H8D0W56W45=GS1.1.1611354723.13.0.1611354723.0; _ga=GA1.2.1435811860.1589061223',
		# 'origin': 'https://mycrc.gatech.edu',
		# 'referer': 'https://mycrc.gatech.edu/booking',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}
	# result = s.get(tokenUrl, headers=headers, params=query_params)
	# tree = html.fromstring(result.text)
	# veriToken = tree.xpath('//*[@id="__LocalAntiForgeryForm"]/input/@value')

	payload = {
		"__RequestVerificationToken": getToken(),
		"UserName": username,
		"Password": password,
		"returnUrl": "/booking"
	}

	response = s.post(url, data=payload, headers=headers, allow_redirects = True)
	# cookie = response.headers
	return response.text

def getCookies():
	return s.cookies['.AspNet.ApplicationCookie']

def getToken():
	tokenUrl = 'https://mycrc.gatech.edu/Account/GetLoginOptions'
	query_params = {
		'returnURL': '/',
		'isAdmin': 'false'
	}
	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'cookieControl=true; cookieControlPrefs=[]; _gid=GA1.2.231961476.1611030909; ASP.NET_SessionId=npsgwngakufr43okfwwaujzd; __RequestVerificationToken=u1lTNpN41IbJ0JoKVzwDgjgQU_Avbvro2-dOv7BOsdRoLR-UqnN8Cx5oTOAEBiawsE0BzEswiKPerxmOS83LbZBo4a93h2OoFKfZP0gszRI1; IDMSESSID=5565B3C00B3C85EF6F34FE911EA06AF14C7CF7386891229FD7D882612BE7F086B6144B08A0E9E5E27749BB612C41898C991710B52A881CFE2D11DFD0C74CBFA7; _ga_H8D0W56W45=GS1.1.1611354723.13.0.1611354723.0; _ga=GA1.2.1435811860.1589061223',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}
	result = s.get(tokenUrl, headers=headers, params=query_params)
	tree = html.fromstring(result.text)
	veriToken = tree.xpath('//*[@id="__LocalAntiForgeryForm"]/input/@value')
	return veriToken

def getTimeSlotId(time):
	tomorrowsDate = datetime.now() + timedelta(1)
	url = 'https://mycrc.gatech.edu/booking/9cefff00-4032-42bc-b803-faaf360551b1/slots/db2dba86-c38a-4836-9b48-739f448bd01a/' + tomorrowsDate.strftime("%Y/%m/%d")
	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'cookieControl=true; cookieControlPrefs=[]; _gid=GA1.2.231961476.1611030909; ASP.NET_SessionId=npsgwngakufr43okfwwaujzd; __RequestVerificationToken=u1lTNpN41IbJ0JoKVzwDgjgQU_Avbvro2-dOv7BOsdRoLR-UqnN8Cx5oTOAEBiawsE0BzEswiKPerxmOS83LbZBo4a93h2OoFKfZP0gszRI1; IDMSESSID=5565B3C00B3C85EF6F34FE911EA06AF14C7CF7386891229FD7D882612BE7F086B6144B08A0E9E5E27749BB612C41898C991710B52A881CFE2D11DFD0C74CBFA7; _ga_H8D0W56W45=GS1.1.1611354723.13.0.1611354723.0; _ga=GA1.2.1435811860.1589061223; .AspNet.ApplicationCookie=' + getCookies(),
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}
	response = s.get(url, headers=headers)
	soup = bs(response.text, "html.parser")
	for paragraph in soup.find_all("p"):
		if paragraph.text == time:
			appointmentId = paragraph.find_previous_sibling().find('button')['onclick'][9:45]
			timeSlotId = paragraph.find_previous_sibling().find('button')['onclick'][49:85]
			timeSlotInstanceId = paragraph.find_previous_sibling().find('button')['onclick'][89:125]
			idArr = [appointmentId, timeSlotId, timeSlotInstanceId]
			break

	return idArr

def test(time):
	return str(getTimeSlotId(time)[0])



def reserveSlot(time):
	tomorrowsDate = datetime.now() + timedelta(1)
	url = "https://mycrc.gatech.edu/booking/reserve"
	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'cookieControl=true; cookieControlPrefs=[]; _gid=GA1.2.231961476.1611030909; ASP.NET_SessionId=npsgwngakufr43okfwwaujzd; __RequestVerificationToken=u1lTNpN41IbJ0JoKVzwDgjgQU_Avbvro2-dOv7BOsdRoLR-UqnN8Cx5oTOAEBiawsE0BzEswiKPerxmOS83LbZBo4a93h2OoFKfZP0gszRI1; IDMSESSID=5565B3C00B3C85EF6F34FE911EA06AF14C7CF7386891229FD7D882612BE7F086B6144B08A0E9E5E27749BB612C41898C991710B52A881CFE2D11DFD0C74CBFA7; _ga_H8D0W56W45=GS1.1.1611354723.13.0.1611354723.0; _ga=GA1.2.1435811860.1589061223; .AspNet.ApplicationCookie=' + getCookies() + '; _gat=1',
		'origin': 'https://mycrc.gatech.edu',
		'referer': 'https://mycrc.gatech.edu/booking/9cefff00-4032-42bc-b803-faaf360551b1',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}
	form_data = {
		"bookingId": "9cefff00-4032-42bc-b803-faaf360551b1",
		"facilityId": "db2dba86-c38a-4836-9b48-739f448bd01a",
		"appointmentId": str(getTimeSlotId(time)[0]),
		"timeSlotId": str(getTimeSlotId(time)[1]),
		"timeSlotInstanceId": str(getTimeSlotId(time)[2]),
		"year": tomorrowsDate.strftime("%Y"),
		"month": tomorrowsDate.strftime("%m"),
		"day": tomorrowsDate.strftime("%d")
	}

	response = s.post(url, headers=headers, data=form_data)
	return response.text

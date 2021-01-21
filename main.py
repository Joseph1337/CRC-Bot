# import func

# print(func.login("jguo345", "562dfc11!"))


# # times = func.getTimeSlotId()
# # print(times)
# # print(func.getCookies())


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
start_url = "https://mycrc.gatech.edu/booking"
driver.get(start_url)


driver.find_element_by_id('loginLink').click() #click login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divLoginOptions"]/div[2]/div[3]/div/button'))).click() #select to login via MyCRC account
driver.find_element_by_id('txtUsername').send_keys("jguo345") #username
driver.find_element_by_id('txtPassword').send_keys("562dfc11!") #password
driver.find_element_by_id('btnLogin').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/booking/9cefff00-4032-42bc-b803-faaf360551b1']"))).click() #click booking
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[2]'))).click() #view the times for the following day


slots = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'booking-slot-item')))
bookComplete = False
for slot in slots:
	time = slot.find_element_by_tag_name('p')
	availability = slot.find_element_by_tag_name('span')
	if "5:30 - 6 PM" in time.text and availability.text[:1] > "0": #first option
		slot.find_element_by_tag_name('button').click()
		bookComplete = True
		break
	elif "6:30 - 7 PM" in time.text and availability.text[:1] > "0": #second option
		slot.find_element_by_tag_name('button').click()
		bookComplete = True
		break

driver.quit()
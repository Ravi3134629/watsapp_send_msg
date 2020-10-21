from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
print("Scan the QR Code!")
name = input('Enter Friend or Group Name')
msg = input('Enter the Message to send Repeatedly!')
count = int(input('Enter How Many Time This Message need to send!'))


#user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    message_box.send_keys(msg+Keys.ENTER)
print("message delivered")
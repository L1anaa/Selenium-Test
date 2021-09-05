import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select 

driver = webdriver.Chrome(executable_path="C:\\Work\\chromedriver.exe")
driver.maximize_window()
driver.get("https://youhack.xyz/")

driver.find_element_by_xpath("//*[@id='navigation']/div/nav/div/ul[2]/li[1]").click()

time.sleep(2)
name_field = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[2]/dd/input")
name_field.send_keys("Лианна")

time.sleep(2)
email_field = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[3]/dd/input")
email_field.send_keys("testliana@mail.ru")

time.sleep(2)
pass_field = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/fieldset[1]/dl[1]/dd/input")
pass_field.send_keys("123456")

time.sleep(2)
pass_field = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/fieldset[1]/dl[2]/dd/input")
pass_field.send_keys("123456")

sex = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[4]/dd/ul/li[1]/label").click()

time.sleep(2)
dropdown = Select(driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[5]/dd/ul/li[1]/select"))
dropdown.select_by_index(3)

time.sleep(2)
day = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[5]/dd/ul/li[2]/input")
day.send_keys("22") 

year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[5]/dd/ul/li[3]/input")
year.send_keys("1996")

time.sleep(2)
secret_word = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/dl[7]/dd/input")
secret_word.send_keys("vitalja")

time.sleep(2)
captcha = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()


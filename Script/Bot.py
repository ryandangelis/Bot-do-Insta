from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Page1:
    
    def __init__(self):
        
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.maximize_window()
        
        self.urlogin = 'https://www.instagram.com/?hl=pt-br'
    
    def loginConta(self):
        
        self.driver.get(self.urlogin)
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('lucasoleoncio807@gmail.com')
        self.driver.find_element_by_name('password').send_keys('allox2020')
        n1 = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        n1.click()
        time.sleep(2)
        n2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        n2.click()
        time.sleep(2)
        n3 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        n3.click()
        
    def clickfollows(self):    
        while True:
            k1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div')
            k2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button/div')
            k3 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button/div')
            k4 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[4]/div[3]/button/div')
            k5 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[5]/div[3]/button/div')
            k1.click()
            time.sleep(1)
            k2.click()
            time.sleep(1)
            k3.click()
            time.sleep(1)
            k4.click()
            time.sleep(1)
            k5.click()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(3600)

p = Page1()
p.loginConta()
p.clickfollows()
del p 
input('ok')

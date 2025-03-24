import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




class AlertPagesTest:
    def __init__(self, driver,wait):
        
        self.driver = driver
        self.wait = wait
        
        self.allertButton = (By.XPATH,"//h5[normalize-space()='Alerts, Frame & Windows']")
        self.ButtonAlert = (By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-1']")
        self.Button1 = (By.ID,"alertButton")
        self.Button2 = (By.ID,"timerAlertButton")
        # self.Button3 = (By.ID,"confirmButton")
        
      
    def go_alert(self):
         self.driver.find_element(*self.allertButton).click()  
         self.driver.find_element(*self.ButtonAlert).click() 
         
         self.driver.find_element(*self.Button1).click()
    
         alert = self.driver.switch_to.alert
         alert.accept() 
         
         self.driver.find_element(*self.Button2).click()
        
        #  self.driver.find_element(*self.Button3).click()


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select



class WidgetsPagesTest:
    def __init__(self, driver,wait):
        
        self.driver = driver
        self.wait = wait
        
        self.widgetsButton = (By.XPATH,"//h5[normalize-space()='Widgets']")
        self.datepickerButton = (By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-2']")
        self.date = (By.XPATH,"//input[@id='dateAndTimePickerInput']")
        self.years = (By.XPATH,"//span[@class='react-datepicker__year-read-view--down-arrow']")
    

    def click_widgets(self):
         self.driver.find_element(*self.widgetsButton).click()
      
    
    def click_datepicker(self):
       self.driver.find_element(*self.datepickerButton).click()

    def click_date(self):
        self.driver.find_element(*self.date).click()
        self.driver.find_element(By.XPATH,"//div//span[@class='react-datepicker__month-read-view--down-arrow']").click()
        self.driver.find_element(By.XPATH,"//div[normalize-space()='November']").click()
        
        self.driver.find_element(*self.years).click()
        
        # self.driver.find_element(By.XPATH,"//div[@class='react-datepicker__year-dropdown']//div[1]").click()
      
                
        
    
   
        
        
        
        
        
        
   
        



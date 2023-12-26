# test_login.py
import time
from checkTask import checkTask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class TestLogin():
    def __init__(self) -> None:
       
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
       
        self.driver.get("https://app.asana.com/-/login")
    
        
    def test_successful_login(self):
        time.sleep(10)
        email_input = self.driver.find_element('xpath',"//input[@type='text']")
      
        email_input.send_keys("usmanrasheed802@gmail.com")
        time.sleep(1)
        self.driver.find_elements('xpath',"//div[@role='button']")[1].click()
        time.sleep(6)
        password_input = self.driver.find_element('xpath',"//input[@type='password']")
        password_input.send_keys("Rosepetal514@")
        time.sleep(2)
        previous=self.driver.current_url.strip()
        login_button = self.driver.find_element('xpath',"//div[@class='ThemeableRectangularButtonPresentation--isEnabled ThemeableRectangularButtonPresentation ThemeableRectangularButtonPresentation--large NuxButton LoginPasswordForm-loginButton']")
        login_button.click()
        time.sleep(5)
        curr=self.driver.current_url.strip()
        print(previous,curr)

        assert previous != curr, "Login test case failed."
        if(previous!=curr):
            print("Passed: Login test")
        time.sleep(5)
        self.runNext()
    def runNext(self):
        checktask=checkTask(self.driver)
        checktask.runTestCase()
        
        
        


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testLogin=TestLogin()
    testLogin.test_successful_login()

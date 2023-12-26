import time
import logging
from selenium import webdriver
from createTask import createTask


class TestLogin:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://app.asana.com/-/login")

        # Configure the logging
        self.log_file = "test_log.txt"
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s: %(message)s')

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)

    def test_successful_login(self):
        try:
            time.sleep(10)
            email_input = self.driver.find_element('xpath', "//input[@type='text']")
            email_input.send_keys("aimanoor514@gmail.com")
            time.sleep(1)
            self.driver.find_elements('xpath', "//div[@role='button']")[1].click()
            time.sleep(6)
            password_input = self.driver.find_element('xpath', "//input[@type='password']")
            password_input.send_keys("Rosepetal514@")
            time.sleep(2)
            previous = self.driver.current_url.strip()
            login_button = self.driver.find_element('xpath',
                                                    "//div[@class='ThemeableRectangularButtonPresentation--isEnabled ThemeableRectangularButtonPresentation ThemeableRectangularButtonPresentation--large NuxButton LoginPasswordForm-loginButton']")
            login_button.click()
            time.sleep(5)
            curr = self.driver.current_url.strip()
            self.log_info(f"Previous URL: {previous}, Current URL: {curr}")

            assert previous != curr, "Login test case failed."
            if previous != curr:
                self.log_info("Passed: Login test")
            time.sleep(5)
            self.runCreateTask()
        except Exception as e:
            self.log_error(f"An error occurred during login: {str(e)}")

    def runCreateTask(self):
        create = createTask(self.driver)
        create.runcreateTask("TASK 1")

    def tearDown(self):
        self.driver.quit()
        self.log_info("Driver quit successfully")


if __name__ == '__main__':
    testLogin = TestLogin()
    try:
        testLogin.test_successful_login()
    finally:
        testLogin.tearDown()

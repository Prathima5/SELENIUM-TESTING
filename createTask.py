import time
class createTask():
    def __init__(self,driver) -> None:
        self.driver=driver
        self.report_file = "report_file.txt"

    def clear_report_file(self):
        with open(self.report_file, 'w') as f:
            f.write("Test Report:\n")

    def log_test_result(self, test_case, status, error=None):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.report_file, 'a') as f:
            f.write(f"\n\n{current_time} \nTEST CASE:  '{test_case}' \nTEST CASE STATUS:  {status}")
            if error:
                f.write(f" - {error}")
            f.write("\n")

    def runcreateTask(self,task):
        time.sleep(2)
        try:
            self.log_test_result(f"\Create Task: '{task}'", "Running")
            time.sleep(6)
            self.driver.find_elements('xpath', "//div[@role='button']")[2].click()
            time.sleep(4)
            self.driver.find_element('xpath',
                                     "//div[@class='LeftIconItemStructure--isHighlighted LeftIconItemStructure LeftIconItemStructure--alignCenter MenuItemA11y-content']").click()
            time.sleep(3)
            taskName = self.driver.find_element('xpath', "//input[@type='text']")

            if (task is not None):
                taskName.send_keys(task)
                time.sleep(2)
                self.driver.find_element('xpath',
                                         "//div[@class='ThemeableRectangularButtonPresentation--isEnabled ThemeableRectangularButtonPresentation ThemeableRectangularButtonPresentation--large PrimaryButton--standardTheme PrimaryButton QuickAddTaskToolbar-createButton']").click()
                time.sleep(3)
                self.log_test_result(f"Create Task: '{task}'", "Passed")
            else:
                self.log_test_result(f"Create Task: '{task}'", "Failed", "Null Values not accepted")


        except Exception as e:
            x = {str(e)}
            self.log_test_result(f"Create Task: '{task}'", "Failed", str(e))






        
        
        
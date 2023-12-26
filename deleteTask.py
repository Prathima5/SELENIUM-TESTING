import time
class deleteTask():
    def __init__(self,driver) -> None:
        self.driver=driver
    def runDeleteTask(self):
        time.sleep(2)
        try:
            self.driver.get("https://app.asana.com/0/1205798506066986/list")

            time.sleep(11)
            self.driver.find_element('xpath',"//div[@class='SpreadsheetGridTaskNameAndDetailsCellGroup-detailsButtonClickArea']").click()
            
            time.sleep(4)
            self.driver.find_element('xpath',"//div[@aria-label='More actions for this task']").click()
            
            time.sleep(3)

            taskName=self.driver.find_elements('xpath',"//div[@class='ExtraActionsMenuItemLabel']")[6].click()
            time.sleep(3)
            print(f"DeleteTask :Passed test case !")
        except Exception as e:
            print(f"DeleteTask :Failed test case !")

        finally:
            self.driver.quit()






        
        
        
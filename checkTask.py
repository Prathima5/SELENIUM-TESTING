import time
class checkTask():
    def __init__(self,driver) -> None:
        self.driver=driver
    def runTestCase(self):
        time.sleep(2)
        
        self.driver.get("https://app.asana.com/0/1205798506066986/list")

        
        time.sleep(5)
        curr=self.driver.current_url.strip().split('/')
        assert curr[len(curr)-1]=="list","Test Check Failed"
        if(curr[len(curr)-1]=="list"):
            print("Check Tasks: Test case passed!")
        
        
        
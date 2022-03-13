import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//DELL//Downloads//chromedriver_win32//chromedriver.exe")


def lecture1():
    driver.implicitly_wait(10)
    driver.get("https://medium.com/p/c552674a4621")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

def lecture2():
    driver.implicitly_wait(10)
    driver.get("https://medium.com/p/89dd0af257b9")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

def portfolio():
    driver.get("https://www.mrayush.com/resume")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.refresh()
start = time.time()
for i in range(150):
    lecture1()
    lecture2()
    #portfolio()
end = time.time()

print("Totsl time took : ", end-start)
driver.quit()



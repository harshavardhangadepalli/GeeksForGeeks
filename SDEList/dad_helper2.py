from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://autoshares.in/scripts/backtest.php")
count = 0
while True:
    if count == 184:
        break
    print("hello")
    driver.refresh()
    count+=1
print("done")
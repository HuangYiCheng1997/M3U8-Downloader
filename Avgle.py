import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://127.0.0.1:1080')
driver = webdriver.Chrome(executable_path="./chromedriver",
chrome_options=options)

url = "https://avgle.com/video/104733/natr-571-%E8%BF%91%E8%A6%AA%E7%9B%B8%E5%A7%A6-%E4%B8%8D%E8%A8%80-%E9%9A%A3%E3%81%AB%E3%81%8A%E7%88%B6%E3%81%95%E3%82%93%E3%81%8C%E3%81%84%E3%82%8B%E3%81%AE%E3%82%88-%E4%BD%90%E3%80%85%E6%9C%A8%E3%81%82%E3%81%8D"

driver.get(url)


# time.sleep(10)

scriptToExecute = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"

network = driver.execute_script(scriptToExecute)

for item in network:
    url = item["name"]
    if ".m3u8" in url:
        print(url)


# s = driver.execute_script(scriptToExecute)

# print(s)


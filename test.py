from selenium import webdriver

from wxpy import *
bot = Bot(
    cache_path=True
)

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://127.0.0.1:1080')
options.add_argument("--headless")
options.add_argument("window-size=1024,768", )
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)

from wxpy import *


def log_in():
    bot = Bot(cache_path=True, console_qr=2)

    @bot.register()
    def process_msg(msg):
        # 打印消息
        if "avgle.com" in msg.text:
            print(msg.text)
            m3u8 = get_m3u8(msg)
            return m3u8


def get_m3u8(url):
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=socks5://127.0.0.1:1080')

    driver = webdriver.Chrome(executable_path="./chromedriver",
                              chrome_options=options)
    driver.get(url)

    scriptToExecute = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"

    network = driver.execute_script(scriptToExecute)

    for item in network:
        m3u8 = item["name"]
        if ".m3u8" in m3u8:
            driver.quit()
            return m3u8


if __name__ == '__main__':
    log_in()
    embed()

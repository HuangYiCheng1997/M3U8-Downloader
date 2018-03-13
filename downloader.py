import asyncio
import aiohttp
import requests
import time

class Spider(object):
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.videos = None
        self.index = 0
        self.proxy = 'http://127.0.0.1:8123'

    async def download(self, video):
        name = video[0]
        url = video[1]
        print('start download {}'.format(name))
        try:
            async with self.session.get(url, timeout=20) as r:
                content = await r.read()
                with open('./test/{}.ts'.format(name), 'wb') as f:
                    f.write(content)
            print('download done {}'.format(name))
            self.index += 1

        except Exception as e:
            print('出现异常{},重新下载'.format(e))
            await asyncio.sleep(5)
            await self.download(video)

        try:
            next_video = next(self.videos)
            await asyncio.gather(self.download(next_video))
        except StopIteration:
            return

    def prepare_download(self):
        videos = [next(self.videos) for _ in range(5)]
        try:
            tasks = asyncio.gather(*[self.download(video) for video in videos])
            loop.run_until_complete(tasks)
        except Exception as e:
            print(e)
            print('出错')

    def main(self, m3u8):
        r = requests.get(m3u8)
        text = r.text.split('\n')
        url_list = (url.strip('\r') for url in text if 'http' in url)
        videos = ((name, url) for name, url in enumerate(url_list))
        if videos:
            self.videos = videos
            self.prepare_download()
        else:
            print('m3u8网址过期.....')


if __name__ == '__main__':
    start = time.time()
    s = Spider()
    loop = asyncio.get_event_loop()
    m3u8 = 'https://ip62819793.ahcdn.com/key=hsNrIICPCGF4u6mEEL-DBw,s=,end=1520865713,limit=2/data=1520865713/state=Q9jY/reftag=56109644/media=hlsA/7/177/2/65761742.m3u8'
    s.main(m3u8)
    s.session.close()
    print('done')
    print(time.time()-start)
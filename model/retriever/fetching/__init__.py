import requests
#
# from .playwright_based_crawl_new import get_raw_pages
# from .import playwright_based_crawl_new
#
# import asyncio
    

class Fetcher:
    def __init__(self) -> None:
        pass
        # self.loop = asyncio.get_event_loop()
        # TODO delete loop -> loop.close()

    
    def _pre_handle_urls(self, urls: list[str]) -> list[str]:
        urls_new = []
        for url in urls:
            if url in urls_new or "http://%s"%url in urls_new or "https://%s"%url in urls_new:
                continue
            if not url.startswith("http"):
                url = "http://%s" % url
            urls_new.append(url)
        return urls_new

    def fetch(self, urls: list[str]) -> dict[str, list[str]]:
        
        urls = self._pre_handle_urls(urls)
        print('看看如何处理网页的')
        for url in urls:
            print(url)
        print('看完了')


        # self.loop.run_until_complete(get_raw_pages(urls, close_browser=True))
        # responses = [playwright_based_crawl_new.results[url] for url in urls]
        responses = []
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }
        for url in urls:
            page = requests.get(url, verify=False,headers = header)
            responses.append(page.text)

        ret = dict()
        for url, resp in zip(urls, responses):
            ret[url] = resp
            # if not resp[1]:
            #     pass
            # else:
            #     ret[url] = resp[1]
        # print('看看返回结果呢')
        # for k,v in ret.items():
        #     print(k)
        #     print(v)
        #     print()
        # print('看完了')
        return ret

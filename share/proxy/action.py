import os
import re
import urllib.request
import random
import time
from lxml import etree
from multiprocessing import Pool
from datetime import datetime
from main.models import Proxy
from public.serialization import ProxySerializer
from tools import Tools
from variable import AGENT_LIST


class FreeProxyHandler:
    def __init__(self, request):
        self.request = request

    def get_handler(self):
        post_type = self.request.POST.get('post_type')
        free_proxy_cool = FreeProxyCool(self.request)
        handle = None
        if post_type and hasattr(free_proxy_cool, post_type):
            handle = getattr(free_proxy_cool, post_type)
        return handle


class FreeProxyCool:
    def __init__(self, request):
        self.request = request

    def get_table_data(self):
        ret_dict = {'ret': 0, 'data': []}
        try:
            flag = self.request.POST.get('flag')
            filter_condition = self.request.POST.get('filter_condition')
            start = int(self.request.POST.get('start', 0))
            length = int(self.request.POST.get('length', 0))
            if not length:
                length = 10
            end = start + length
            proxy_objs = Proxy.objects.filter(is_delete=0).order_by('-score')
            if filter_condition:
                pass
            total = len(proxy_objs)
            configs = proxy_objs[start:end]
            datas = ProxySerializer(configs, many=True).data
            ret_dict['data'] = datas
            ret_dict['draw'] = int(self.request.POST.get('draw', 1))
            ret_dict['recordsTotal'] = total
            ret_dict['recordsFiltered'] = total
        except Exception as e:
            print(e)
        print(ret_dict)
        return ret_dict


class GetFreeProxy(object):
    def __init__(self):
        self.base_url = 'https://www.kuaidaili.com/free/inha'
        self.begin_page = None
        self.end_page = None
        self.detail_url_list = []
        self.get_begin_end_page()
        self.get_all_detail_url()

    @staticmethod
    def get_random_sleep_time():
        time.sleep(random.randint(1, 6))

    @staticmethod
    def get_page_html_second(url, retry_count=10, timeout=15):
        headers = random.choice(AGENT_LIST)
        req = urllib.request.Request(url, headers=headers)
        html, response = None, None
        while True:
            if retry_count <= 0:
                print('GetFreeProxy: get_page_html > fail(url: %s)' % url)
                return html
            try:
                response = urllib.request.urlopen(req, timeout=timeout)
                if response:
                    break
            except Exception as e:
                print('GetFreeProxy: get_page_html > error(url: %s, retry_count: %s, err: %s)' % (url, retry_count, e))
                # 递归调用
                retry_count -= 1
                print("当前: %s" % retry_count)
                GetFreeProxy.get_random_sleep_time()
                continue
        html = response.read().decode('utf-8')
        return html

    @staticmethod
    def get_page_html(url, retry_count=10, timeout=15):
        # 1.use proxy
        # proxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:8080'})
        # opener = urllib.request.build_opener(proxy_handler)
        # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        # opener.open(self.base_url, timeout=self.timeout)
        # 2.use proxy
        # headers = random.choice(AGENT_LIST)
        # req = urllib.request.Request(self.base_url, headers=headers)
        # proxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:8080'})
        # opener = urllib.request.build_opener(proxy_handler)
        # opener.open(req, timeout=self.timeout)
        GetFreeProxy.get_random_sleep_time()
        headers = random.choice(AGENT_LIST)
        req = urllib.request.Request(url, headers=headers)
        html = None
        while True:
            if retry_count <= 0:
                print('GetFreeProxy: get_page_html > fail(url: %s)' % url)
                return html
            try:
                response = urllib.request.urlopen(req, timeout=timeout)
                if response:
                    break
            except Exception as e:
                print('GetFreeProxy: get_page_html > error(url: %s, retry_count: %s, err: %s)' % (url, retry_count, e))
                # 递归调用
                retry_count -= 1
                GetFreeProxy.get_page_html(url, retry_count=retry_count, timeout=15)
        html = response.read().decode('utf-8')
        return html

    def get_index_page(self):
        html = self.get_page_html(self.base_url)
        return html

    def get_begin_end_page(self):
        html = self.get_index_page()
        html = etree.HTML(html)
        begin_page = html.xpath('//*[@id="listnav"]/ul/li[2]/a/text()')
        end_page = html.xpath('//*[@id="listnav"]/ul/li[9]/a/text()')
        self.begin_page = int(begin_page[0])
        self.end_page = int(end_page[0])
        print("begin_page: %s, end_page: %s" % (self.begin_page, self.end_page))

    def get_all_detail_url(self):
        self.detail_url_list = [self.base_url + '/' + str(i) for i in range(self.begin_page, self.end_page)]

    def pool_task(self):
        pool = Pool(processes=6)
        for i in self.detail_url_list:
            pool.apply_async(func=self.get_page_html, args=(i,), callback=self.get_detail_info)
        pool.close()
        pool.join()

    @staticmethod
    def get_detail_info(html):
        if html:
            result_list = re.findall('<tr>.*?<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>.*?\
                    <td data-title="匿名度">(.*?)</td>.*?<td data-title="类型">(.*?)</td>.*?<td data-title="位置">(.*?)</td>.*?\
                    <td data-title="响应速度">(.*?)</td>.*?<td data-title="最后验证时间">(.*?)</td>.*?</tr>', html, re.S)
            print(result_list)
            GetFreeProxy.write2mysql(result_list)
        else:
            print("some page get fail")

    @staticmethod
    def write2mysql(result_list):
        for result in result_list:
            Proxy(ip=result[0], port=result[1], anonymous=result[2], type=result[3], location=result[4], response_speed\
                =result[5], last_validation_time=Tools.format_s2p_time1(result[-1])).save()








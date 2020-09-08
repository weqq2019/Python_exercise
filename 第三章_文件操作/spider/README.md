## **scrapy框架**

- **定义**

  ```python
  异步处理框架,可配置和可扩展程度非常高,Python中使用最广泛的爬虫框架
  ```

- **安装**

  ```python
  【1】Ubuntu安装
      1.1) 安装依赖包
          a> sudo apt-get install libffi-dev
          b> sudo apt-get install libssl-dev
          c> sudo apt-get install libxml2-dev
          d> sudo apt-get install python3-dev
          e> sudo apt-get install libxslt1-dev
          f> sudo apt-get install zlib1g-dev
          g> sudo pip3 install -I -U service_identity
          
      1.2) 安装scrapy框架
          a> sudo pip3 install Scrapy
          
  【2】Windows安装
      2.1) cmd命令行(管理员): python -m pip install Scrapy
     【注意】: 如果安装过程中报如下错误
              'Error: Microsoft Vistual C++ 14.0 is required xxx'
              则安装Windows下的Microsoft Vistual C++ 14.0 即可（笔记spiderfiles中有）
  ```

- **Scrapy框架五大组件**

  ```python
  【1】引擎(Engine)      ：整个框架核心
  【2】调度器(Scheduler) ：维护请求队列
  【3】下载器(Downloader)：获取响应对象
  【4】爬虫文件(Spider)  ：数据解析提取
  【5】项目管道(Pipeline)：数据入库处理
  **********************************
  【中间件1】: 下载器中间件(Downloader Middlewares) : 引擎->下载器,包装请求(随机代理等)
  【中间件2】: 蜘蛛中间件(Spider Middlewares) : 引擎->爬虫文件,可修改响应对象属性
  ```

- **scrapy爬虫工作流程**

  ```python
  【1】爬虫项目启动,由引擎向爬虫程序索要第一批要爬取的URL,交给调度器去入队列
  【2】调度器处理请求后出队列,通过下载器中间件交给下载器去下载
  【3】下载器得到响应对象后,通过蜘蛛中间件交给爬虫程序
  【4】爬虫程序进行数据提取：
      4.1) 数据交给管道文件去入库处理
      4.2) 对于需要继续跟进的URL,再次交给调度器入队列，依次循环
  ```

- **scrapy常用命令**

  ```python
  【1】创建爬虫项目
      scrapy startproject 项目名
      
  【2】创建爬虫文件
      scrapy genspider 爬虫名 域名
      
  【3】运行爬虫
      scrapy crawl 爬虫名
  ```

- **scrapy项目目录结构**

  ```python
  Baidu                   # 项目文件夹
  ├── Baidu               # 项目目录
  │   ├── items.py        # 定义数据结构
  │   ├── middlewares.py  # 中间件
  │   ├── pipelines.py    # 数据处理
  │   ├── settings.py     # 全局配置
  │   └── spiders
  │       ├── baidu.py    # 爬虫文件
  └── scrapy.cfg          # 项目基本配置文件
  ```

- **settings.py常用变量**

  ```python
  【1】USER_AGENT = 'Mozilla/5.0'
  
  【2】ROBOTSTXT_OBEY = False
      是否遵循robots协议,一般我们一定要设置为False
  
  【3】CONCURRENT_REQUESTS = 32
      最大并发量,默认为16
      
  【4】DOWNLOAD_DELAY = 0.5
      下载延迟时间: 访问相邻页面的间隔时间,降低数据抓取的频率
  
  【5】COOKIES_ENABLED = False | True
      Cookie默认是禁用的，取消注释则 启用Cookie，即：True和False都是启用Cookie
      
  【6】DEFAULT_REQUEST_HEADERS = {}
      请求头,相当于requests.get(headers=headers)
  ```

- **安装scrapy出现问题**

  ```python
  xxx has requirement 模块>=4.4.2 but you'll have 模块 4.3.2
  升级模块: sudo pip3 install 模块 --upgrade
  ```

## **小试牛刀**

```python
【1】执行3条命令,创建项目基本结构
    scrapy startproject Baidu
    cd Baidu
    scrapy genspider baidu www.baidu.com
    
【2】完成爬虫文件: spiders/baidu.py
    import scrapy
    class BaiduSpider(scrapy.Spider):
        name = 'baidu'
        allowed_domains = ['www.baidu.com']
        start_urls = ['http://www.baidu.com/']
        
        def parse(self,response):
            r_list = response.xpath('/html/head/title/text()').extract()[0]
            print(r_list)
  
【3】完成settings.py配置
    3.1) ROBOTSTXT_OBEY = False
    3.2) DEFAULT_REQUEST_HEADERS = {
        'User-Agent' : 'Mozilla/5.0'
    }
    
【4】运行爬虫
    4.1) 创建run.py(和scrapy.cfg同路径)
    4.2) run.py
         from scrapy import cmdline
         cmdline.execute('scrapy crawl baidu'.split())
            
【5】执行 run.py 运行爬虫
```

![Image text](https://raw.githubusercontent.com/weqq2019/Python_exercise/master/img/03-05-05x.png)



## **完成scrapy Tencent项目完整流程**

- **完整流程**

  ```python
  【1】scrapy startproject Tencent
  【2】cd Tencent
  【3】scrapy genspider tencent tencent.com
  【4】items.py(定义爬取数据结构)
      import scrapy
      class TencentItem(scrapy.Item):
          name = scrapy.Field()
          address = scrapy.Field()
      
  【5】tencent.py（写爬虫文件）
      import scrapy
      from ..items import TencentItem
      class TencentSpider(scrapy.Spider):
          name = 'tencent'
          allowed_domains = ['tencent.com']
          start_urls = ['']
          def parse(self, response):
              item = TencentItem()
              item['name'] = xxxx
              yield item
  
  【6】pipelines.py(数据处理)
      class TencentPipeline(object):
          def process_item(self, item, spider):
              return item
      
  【7】settings.py(全局配置)
      LOG_LEVEL = ''  # DEBUG < INFO < WARNING < ERROR < CRITICAL
      LOG_FILE = ''
      FEED_EXPORT_ENCODING = ''
      
  【8】run.py 
      from scrapy import cmdline
      cmdline.execute('scrapy crawl tencent'.split())
  ```



腾讯招聘具体职位信息抓取

![Image text](https://raw.githubusercontent.com/weqq2019/Python_exercise/master/img/03-05-06.png)



猿急送爬虫单子数据

![Image text](https://raw.githubusercontent.com/weqq2019/Python_exercise/master/img/03-05-07.png)
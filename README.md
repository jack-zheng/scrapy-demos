# scrapy demos

* [参考视屏](https://www.bilibili.com/video/BV1yf4y1B7S8)

## 基础用法

1. scrapy startproject tiobeSpider
2. cd tiobeSpider; scrapy genspider tiobe tiobe.com
3. 在 tiobeSpider > tiobeSpider > tiobe.py 中写入解析 response 的代码
4. cd 到 .cfg 文件同级目录下执行 scrapy crawl tiobe 运行爬虫, 查看结果
5. tiobe 中通过 yield 传给 pipeline
6. settings.py 中启动 pipeline
7. 在 pipelines.py 中添加 item 的处理逻辑
8. piplines.py 中可以定义新的 pipeline，需要在 settings.py 中添加额外配置

PS: settings.py 中可以指定 log 等级

### Issues

`poetry add scrapy` 抛错 `[RecursionError] maximum recursion depth exceeded while calling a Python object`, 1.1.0b2 之后的版本可以，我当前版本是 1.0.10

## logging 设置

scrapy 项目

* 运行 crawl 的时候会输出很多日志，settings 中设置 LOG_LEVEL="WARNING" 设置只输出 warning 以上等级的日志
* `logger = logging.getLogger(__name__)` 指定 log 路径
* settings 中设置 LOG_FILE="./a.log" ，指定 log 文件位置，生成位置和 .cfg 文件平级

普通项目

* 新建一个 logger 配置类，import loggin
* logging.basicConfig(...) 设置格式
* logger = logging.getLogger(__name__)
* 其他文件中通过 from xx import xxLogger 进行统一调用

## 爬去 Boss 直聘前十页信息

爬取失败，稍微搜了一下，要设置 cookie 的，暂时还没学到，后面会了再回来做

## sun0769 测试

* item
* meta
* 基本结构

## scrapy shell

用法很简单，直接输入 `scrapy shell url_addr` 就可以动态 debug 某一个页面了，很赞

## Settings 使用

在 spider 文件中可以通过 `self.settings['MONGO_HOST']` 或者 `self.settings("MONGO_HOST", "")` 拿到。其他文件中，比如 pipeline 中可以通过 spider.settings.get("") 拿到

pipeline 中的 open_spider/close_spider 可以在爬虫开始/结束的时候执行一次

## 书城目录抓去

仿照 suning 的原理爬了一下 孔夫子旧书网 感觉良好

## crawl spider

scrapy 更模式话的使用方式，只需要指定 rule 就能模式化抓去。当网页 URL 不全的时候他还会**自动补全**

保监会地址变了，不过搜索引擎搜一下关键字还是能找到官网的，不过新网站已经达不到练习目的了，前段用了某个UI框架，通过 jason 交互了。直接能拿到所有 list 的结果，就不用解析了。像练习上的这种网站都是很老的网站，才会采用的架构了。挑了半天，选中了一个元器件参数列表做练习 `http://datasheet.eeworld.com.cn/manufacturer/texas-instruments.html`

上面的网站还是失败了，试一下用美剧网站做练习 `cn163.net`, 这个网站没有反爬措施，简简单单就拿到了数据

唯一的区别是通过 `scrapy genspider -t crawl xxx xxx` 的方式生成 spider 模版文件

CrawlSpider 优点：

* 更加结构化
* 代码更少
* 略微缺少灵活度

### Issues

抛错 

```txt
2022-01-21 17:17:31 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <403 http://datasheet.eeworld.com.cn/manufacturer/texas-instruments.html>: HTTP status code is not handled or not allowed
```

添加 agent 之后可以了，不过，只有几个出来了，后面的都失败了，怀疑是 user-agent 有问题，看看后面课程有没有相关的介绍，回头再修

## Cookies 实验

视频中用的账号已经改了，想了一下，同样的原理应该可以用来访问类似的网站，比如我用这种套路访问一下小破站，拿到我关注的 up 主列表，应该是可行的。

Bingo, 实验成功 ╮(￣▽￣"")╭

* spider 文件中重写 `start_requests` 方法的方式定制请求
* settings 文件中，添加 `COOKIES_DEBUG` 开启调试信息

## 下载中间件

下载中间件是位于 engine 和下载器之间的模块，可以用来对 request 和 response 做一些操作

* 修改 user-agent
* 修改 proxy

随机 agent 使用方式:

1. settings 中添加 agent list
2. 自定义 middle ware 类
3. settings 中开启 middle ware
4. 测试

正好用之前 datasheet 的例子测试一下是不是由于 agent 导致下载失败。网上随便找了一个 agent list, 筛选之后成功了，才想成立，666

PS: 搜索的时候发现有现成的包提供模拟 agent 的，有机会可以试试

## 模拟登陆

三种模拟登陆的方式

1. 使用 cookies，前面实验用过了
2. 使用 post 模拟
3. 使用 FormRequest.from_response

2020-01-21，新版的 chrome 把 form 相关的数据放到了 Payload 这个 tab 下了，而且看了一下 github 的格式，和之前也不一样了，utf-8 没了，多了很多其他的比如 日期 之类的 field. 先用原先的 3 个看着比较重要的属性模拟一下登陆试试能不能成功先。

github 访问有问题，实验不能进行，而且短时间内我竟然找不到其他类似登陆的网站。。。。弃了, 以后有机会在试试
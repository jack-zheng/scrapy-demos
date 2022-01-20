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
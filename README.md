# scrapy demos

* [参考视屏](https://www.bilibili.com/video/BV1yf4y1B7S8)

## 步骤

1. scrapy startproject tiobeSpider
2. cd tiobeSpider; scrapy genspider tiobe tiobe.com
3. 在 tiobeSpider > tiobeSpider > tiobe.py 中写入解析 response 的代码
4. cd 到 .cfg 文件同级目录下执行 scrapy crawl tiobe 运行爬虫, 查看结果
5. tiobe 中通过 yield 传给 pipeline
6. settings.py 中启动 pipeline
7. 在 pipelines.py 中添加 item 的处理逻辑
8. piplines.py 中可以定义新的 pipeline，需要在 settings.py 中添加额外配置

PS: settings.py 中可以指定 log 等级

## Issues

`poetry add scrapy` 抛错 `[RecursionError] maximum recursion depth exceeded while calling a Python object`, 1.1.0b2 之后的版本可以，我当前版本是 1.0.10
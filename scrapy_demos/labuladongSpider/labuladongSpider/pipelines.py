import re
import html2text
from urllib.parse import unquote


class FilterUnnecessaryElementPipeline:
    # def func(matched):
    #     return unquote(matched.group(0))

    def process_item(self, item, spider):
        handler = html2text.HTML2Text()
        convert_body = handler.handle(item['body'])

        # delete souyisou
        convert_body = re.sub(r'!\[\]\(..\/..\/images\/souyisou\w\.png\)', '', convert_body)

        # 删除打卡
        convert_body = convert_body.replace('**[第二期 21 天刷题打卡活动](https://mp.weixin.qq.com/s/eUG2OOzY3k_ZTz-CFvtv5Q)', '')
        convert_body = convert_body.replace('即将截至，今天最后一天报名**~', '')
        convert_body = convert_body.replace('**———–**', '')
        convert_body = convert_body.replace('**＿＿＿＿＿＿＿＿＿＿＿＿＿**', '')
        convert_body = convert_body.replace('**《labuladong 的算法小抄》已经出版，关注公众号查看详情；后台回复关键词「进群」可加入算法群；回复「PDF」可获取精华文章 PDF** ：', '')

        # for other images, decode them
        convert_body = re.sub(r'!\[\]\(..\/..\/images\/.+\)', lambda m: unquote(m.group(0)), convert_body)

        with open(spider.book_root + item['title'] + ".md", "w+") as file:
            file.write(convert_body)
        return item

class CreateFolderPipeline:
    def process_item(self, item, spider):
        # path_list = item['id'].split('/')
        # path_list = list(filter(None, path_list))
        # for sub in 
        # 算了，创建目录啥的有点繁琐，还是手动吗，可以但是没必要
        return item
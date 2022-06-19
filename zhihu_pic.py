# 必须手动打开Chrome浏览器，再运行此程序。此举是为了接管电脑自己的浏览器，绕过知乎的对selenium的检测，打开浏览器方法参见readme文档。
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import requests
import time

# 配置下selenium的Options,9527端口是任意的，与我们打开浏览器时的设置有关，前后需要对应，请参见readme文档。
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

# url是你想爬取的答案
url = "https://www.zhihu.com/question/266772222"
driver.get(url)

# 打开网站后，利用js控制滑块，先滚动100下，爬这些图。需要注意的是，ajax加载的时候，滑轮需要往上滑一点才能继续往下滑。
for i in range(1, 100):
    driver.execute_script("window.scrollBy(0,100000)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,-500)")

# 获取加载后网页的代码，利用xpath定位
response = driver.page_source
tree = etree.HTML(response)
answer_list = tree.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[@class="List-item"]')

# 定位每张图片的时候，发现图片路径可以找data-original这一属性，可以爬到高清点的图。requests加一个UA伪装，请求爬图时不会失败。
num = 0
for answer in answer_list:
    pic_url_list = answer.xpath('.//span/figure[@data-size="normal"]')
    for pic_url in pic_url_list:

        url = pic_url.xpath('./img/@data-original')
        if url:
            url_right = url[0]
            pic_data = requests.get(url_right, headers=headers).content
            pic_path = './sese/' + str(num) + '.jpg'
            with open(pic_path, 'wb') as fp:
                fp.write(pic_data)
                print("第%d张图片下载成功" % num)
                num += 1

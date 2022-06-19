<p>该程序更新于2022.6.19号。<p>
<p>这是我学习python以来写的第一个完整的程序，因为是知乎的重度用户，一直想做一个爬取知乎图片的程序。但是从开始学习以来，知乎加强了反爬手段，导致之前的程序都无法正常使用。<p>
<p>于是我就想了一个，让selenium接管现有浏览器躲避检测，配合js代码，用xpath实现一个爬取的功能。<p>
<p>此程序有几个好处:免登录，可以躲避selenium检测，并且可以防止post请求加密。
运行python程序前，需要手动打开Chrome，再运行程序。<p>
<p>具体方法如下：
            1.打开Chrome的安装目录。
            2.运行cmd.
            3.输入指令：chrome.exe --remote-debugging-port=9527 --user-data-dir="C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
              端口9527需要和python程序相对应，双引号内的路径是chrome的用户数据（浏览器输入chrome://version/，复制用户数据），可以保证打开现有的浏览器，实现免登录功能。<p>
 <p>最后，程序的遗憾就是没有使用线程池，或是把函数拆解优化一下，需要手动修改。反正程序的奥义，能跑就行。。。<p>

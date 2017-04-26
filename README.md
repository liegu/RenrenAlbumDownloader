#RenrenAlbumDownloader 2017

### 功能

自动下载全部人人好友的相册

已经更新至2017年4月26日

### 使用

1、登录renren.com获取 cookie

   (1) 打开chrome,进入www.renren.com并登录
   (2) 在网页任意位置点击鼠标右键,点击'检查'
   (3) 网页显示'开发者工具栏',在'开发者工具栏'中选中'Console'选项卡
   (4) 在下方空白处输入'copy(document.cookie)'回车
   (5) 此时cookie信息已经copy到剪贴板

2、修改user.txt中配置信息,将刚得到的cookie信息copy至cookie=后面,threadnumber=10此处为线程数,按自己的情况进行调整默认10
[conf]
cookie=
threadnumber=

2、（确保安装了Python解释器）运行/RenrenDownloader.py，保持网络通畅，然后泡一杯咖啡

3、在当前目录下的albums目录里可以看到所有好友的相册都被下载完成，并且自动按照姓名归档了。

注：单个相册最大下载照片数已固定设为100




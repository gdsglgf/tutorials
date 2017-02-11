## Android镜像设置, 加速下载
```
在Android SDK Manager Setting 窗口设置HTTP Proxy server和HTTP Proxy Port这个2个参数，分别设置为： 

HTTP Proxy server：mirrors.neusoft.edu.cn
HTTP Proxy Port：80

然后把下面的Force ..http://...sources to be fetched using http://..选项打钩，
close Android SDK Manager Setting，然后在重新启动Android SDK Manager Setting
```
## 开发指南
- Android权限标签uses-permission的书写位置 http://hyz301.iteye.com/blog/2211950
- Android实现下载图片并保存到SD卡中 http://www.cnblogs.com/gzggyy/archive/2013/05/18/3085552.html
- listview与adapter用法 http://l62s.iteye.com/blog/1675509
- android ListView详解 http://www.cnblogs.com/allin/archive/2010/05/11/1732200.html
- Activity跳转的几种方式 http://www.cnblogs.com/khazmodan/p/3876376.html

## sqlite
- http://www.cnblogs.com/kgb250/archive/2012/08/28/sqlitedatabase.html
- http://www.runoob.com/sqlite/sqlite-functions.html
- http://blog.csdn.net/eastman520/article/details/19161917
- query 模糊查询使用 https://zhidao.baidu.com/question/873504253486088932.html

## you must restart adb and eclipse
1. 关闭eclipse并在进程中杀掉adb.exe，然后重启。

2. 如有真机连接，拔掉真机，重复1的步骤，

3. 关掉eclipse,然后在命令行运行如下命令
	adb kill-server
	adb start-server
	然后重启eclipse


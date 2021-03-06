# Eclipse

## Eclipse导出JavaDoc中文乱码

在Eclipse里 export 选 JavaDoc，在向导的最后一页的Extra JavaDoc Options 里填上参数即可

比如项目采用的是UTF－8的编码就填：-encoding UTF-8 -charset UTF-8


### Make Eclipse Faster
```
For cleaning up indexes
{workspace path}\.metadata\.plugins\org.eclipse.jdt.core

For cleaning up history
{workspace path}\.metadata\.plugins\org.eclipse.core.resources\.history
```

### Eclipse: failed to create the java virtual machine
```
Method 1: modify eclipse.ini file
1.Open folder with Eclipse.exe and find eclipse.ini file
2.Replace -vmargs by your current real path of javaw.exe, like:
-vm "c:\Program Files\Java\jdk1.7.0_07\bin\javaw.exe"

Method 2: if you do not want to modify the eclipse.ini file, do as follow:
delete the three files: java.exe, javaw.exe, javaws.exe in diretory C:\Windows\System32

learn eclipse and JVM arguments
http://wiki.eclipse.org/Eclipse.ini
```

### Set Eclipse workspace directory
```
open file org.eclipse.ui.ide.prefs in path ECLIPSE_HOME/configuration/.settings
Modify like:
RECENT_WORKSPACES=workspace_path_1\nworkspace_path_2
```

## 工作空间编码相关配置文件
```
workspace\.metadata\.plugins\org.eclipse.core.runtime\.settings\org.eclipse.core.runtime.prefs:
content-types/org.eclipse.jdt.core.javaProperties/charset=UTF-8
content-types/org.eclipse.jst.jsp.core.jspfragmentsource/charset=UTF-8
content-types/org.eclipse.jst.jsp.core.jspsource/charset=UTF-8
content-types/org.eclipse.jst.jsp.core.tagsource/charset=UTF-8
content-types/org.eclipse.jst.jsp.core.tagxsource/charset=UTF-8
eclipse.preferences.version=1

workspace\.metadata\.plugins\org.eclipse.core.runtime\.settings\org.eclipse.core.resources.prefs:
eclipse.preferences.version=1
encoding=UTF-8
version=1
```

## 修改工作空间默认编码
Window-->Preferences-->General-->Workspace-->Text file encoding

## 修改文件的编码
选择文件-->点击鼠标右键-->Properties-->Resource-->Text file encoding

## 修改某文件类型的编码, 如:\*.jsp、\*.java
Window-->Preferences-->General-->Content Types-->Default encoding

## 设置JSP文件的编码方式
Window-->Preferences-->Web-->JSP Files-->Encoding


## eclipse 开启断言
```
assert bool-expression
assert bool-expression : error-message-string

java -ea

run configurations-->arguments-->vm arguments中添加 -ea 参数
```

## set tab size
```
window->preferences->General->Editor->Text Editor->Display Tab Width
window->preferences->Java->Code Style->Formatter设置页面，Edit，在弹出的Editor profile窗口中，Indentation卡片，设置Indentation Size和Tab Size。

eclipse console tab size
window->preferences->Run/Debug->Console->Displayed tab width
```

## editor does not contain a main type
java maven project
delete the project and import it again then it is ok.


## 快捷键失效
按 ctrl + alt + 向上箭头 向下复制一行代码时, windows的整个屏幕都倒转过来.

原因: 这是与英特尔图形和媒体控制面板中的系统快捷键冲突.
解决方法: 使用不同的快捷键解决冲突或者禁用英特尔图形和媒体的快捷键.

禁用英特尔图形和媒体的快捷键方法:
- 桌面鼠标右键->图形选项->快捷键->禁用
- 控制面板->英特尔图形和媒体控制面板->选项和支持->快捷键管理器->启用. 把启用的勾去掉, 保存.


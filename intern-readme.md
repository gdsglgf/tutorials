## CSS
```css
textarea {
    resize: none;    /* resize: both */
}

textarea { resize: vertical; }

textarea { resize: horizontal; }
```


## HTML

打开新的tab
```html
<a href="" target="_blank"></a>
```


## Javascript

alert("")
var status = confirm("");	// true or false


--- jquery

version 1.0+
.attr( attributeName )


version 1.6+
.prop( propertyName )
.removeProp( propertyName )


.focus()
.select()

$(markup).text('');
$(markup).html('');

// for button
$('#migrateBtn').attr('disabled','disabled');
$('#migrateBtn').removeAttr('disabled');

$(this).prop("disabled", true);
$(this).prop("disabled", false);

// for checkbox or radio
$('input[name="subBox"]').prop("checked", true);
$("#checkAll").prop("checked", $("input[name='subBox']").length == $("input[name='subBox']:checked").length ? true : false);

--- Programmatically change the src of an img tag
```html
<img class="image1" src="image1.jpg" alt="image">
<img class="image2" src="image2.jpg" alt="image">
```
1)Jquery Method->
$(".image2").attr("src","image1.jpg");

2)Javascript Method->
var image = document.getElementsByClassName("image2");
image.src = "image1.jpg"


javascript比较运算符

==	检查是否两边的数值或字符串 相等
!=	检查是否两边的数值或字符串 不相等

===	用于检查是否两边的值和类型 严格相等
!==	用于检查是否两边的值和类型 严格不相等
https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Equality_comparisons_and_sameness

JSON.stringify(jsonObject);

--- jsviews

API: template.link(container[, data])

Parameters
container (HTML element or jQuery selector):
- The target element, under which to render and data-link the content
data (object or array – optional):
- The data to render. This can be any JavaScript type, including Array or Object.

API: template.link(container[, data][, helpersOrContext])

Parameters
container (HTML element or jQuery selector):
- The target element, under which to render and data-link the content
data (object or array – optional):
- The data to render. This can be any JavaScript type, including Array or Object.
helpersOrContext (object – optional):
- Contextual helper methods or properties -- available to template as ~keyName



$.templates(markupOrSelector)
Parameters
markupOrSelector (string):
- A markup string or a selector for a template declaration script block

$.templates([name], markupOrSelector)
Parameters
name (string – optional):
- Name for the registered template
markupOrSelector (string):
- A markup string or a selector for a template declaration script block


API: $.templates(namedTemplates)
Parameters
namedTemplates (object):
- Object (hash) of keys (name of template) and values (markup string, selector, or templateOptions object)



$.templates("myTmpl", "#personTmpl");
$.link.myTmpl(container[, data][, helpersOrContext])


jsviews的特殊字符
```
~	取context数据
~root.xxx	 在for标签里面取context数据xxx, root表示根对象
\data        API: template.link(container, data)的第二个参数
\index      for遍历的数组小标
\parent     
```


## Linux
```
~/.bash_profile设置环境变量// 用户级的设置，只对当前用户有效。
1、打开Terminal（终端）
2、输入：vi ~/.bash_profile
3、设置PATH：export PATH=/usr/local/mysql/bin:$PATH
4、输入：:wq    //保存并退出vi
5、修改立即生效：source ~/.bash_profile
6、查看环境变量的值：echo $PATH
```

复制文件内容到剪切板
pbcopy < data.txt

find . -name ".DS*"
find . -name ".DS*" -delete

grep -c ^processor /proc/cpuinfo

## Mac OS X
sysctl -a | grep core_count

sudo scutil --set HostName newName   # 修改用户名

Mac上创建多个桌面

调出Mission Control界面: 键盘Control＋向上键

各桌面切换方法：
1.使用4指左右扫能够切换桌面。
2.Control + 左/右 也能切换。



批量重命名文件
# 将.txt文件后缀改成.md
for old in *.txt; do mv $old `basename $old .txt`.md; done


## 12 Command Line Keyboard Shortcuts
```
Ctrl + A	Go to the beginning of the line you are currently typing on
Ctrl + E	Go to the end of the line you are currently typing on
Ctrl + L	Clears the Screen, similar to the clear command
Ctrl + U	Clears the line before the cursor position. 
			If you are at the end of the line, clears the entire line.
Ctrl + H	Same as backspace
Ctrl + R	Let’s you search through previously used commands
Ctrl + C	Kill whatever you are running
Ctrl + D	Exit the current shell
Ctrl + Z	Puts whatever you are running into a suspended background process. fg restores it.
Ctrl + W	Delete the word before the cursor
Ctrl + K	Clear the line after the cursor
Ctrl + T	Swap the last two characters before the cursor
Esc + T 	Swap the last two words before the cursor
```


## Database

更改MySQL表列类型
```sql
ALTER TABLE tablename MODIFY columnname column_definition;
ALTER TABLE tablename CHANGE [COLUMN] old_col_name new_col_name column_definition;
alter table t_history modify content text not null;
```


## Spring
```
@Resource(name="person")

@Autowired
@Qualifier("person")

@Inject
@Qualifier("person")

Spring injection with @Resource, @Autowired and @Inject

Below is a summary of their execution paths.
@Autowired and @Inject
	1. Matches by Type
	2. Restricts by Qualifiers
	3. Matches by Name


@Resource
	1. Matches by Name
	2. Matches by Type
	3. Restricts by Qualifiers (ignored if match is found by name)


Spring Annotation Style Best Practices
	1. Explicitly name your component [@Component(“beanName”)]
	2. Use ‘@Resource’ with the ‘name’ attribute [@Resource(name=”beanName”)]
	3. Avoid ‘@Qualifier’ annotations unless you want to create a list of similar beans. 
	For example you may want to mark a set of rules with a specific ‘@Qualifier’ annotation. 
	This approach makes it simple to inject a group of rule classes into a list that can be 
	used for processing data.
	4. Scan specific packages for components 
		[context:component-scan base-package=”com.sourceallies.person”]. 
	While this will result in more component-scan configurations it reduces the chance 
	that you’ll add unnecessary components to your Spring context.
```

## Sublime Text 2

Sublime Text->Preferences->Setting-User
```javascript
{
	"ignored_packages": [],
	"create_window_at_startup": false,
	"open_files_in_new_window": false,
	"highlight_line": true,
	"highlight_modified_tabs": true,
	"bold_folder_labels": true,
	"translate_tabs_to_spaces": false,
	"hot_exit": true,
	"remember_open_files": true
}
```

mac sublime text2 记住上次打开的文件和文件夹
mac 按关闭按钮是关闭文件, 不能记住。按cmd+q, 直接退出, 可以记住。 
window 下关闭按钮就是直接退出了。 


## python
```
sudo pip install -U pip setuptools
sudo pip install numpy --upgrade
sudo pip install scipy --upgrade
sudo pip install matplotlib --upgrade
```

Python clear the screen in shell
```python
# Windows
import os
tmp = os.system('cls')

# Linux / Mac OS
import os
tmp = os.system('clear')
```

Get python version
```python
import sys
print(sys.version_info)
version = sys.version_info[0]
```
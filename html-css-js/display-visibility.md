## display:none与visible:hidden的区别
- http://www.cnblogs.com/nicholas_f/archive/2009/03/27/1423207.html
- http://www.w3school.com.cn/cssref/pr_class_visibility.asp
- http://www.w3school.com.cn/cssref/pr_class_display.asp
```
display:none与visible:hidden的区别
display:none和visible:hidden都能把网页上某个元素隐藏起来，但两者有区别:

display:none ---不为被隐藏的对象保留其物理空间，即该对象在页面上彻底消失，通俗来说就是看不见也摸不到。

visible:hidden--- 使对象在网页上不可见，但该对象在网页上所占的空间没有改变，通俗来说就是看不见但摸得到。

例子：

<html>
<head>
<title>display:none和visible:hidden的区别</title>
</head>
<body >
<span style="display:none; background-color:Blue">隐藏区域</span>
<span style="display:block; background-color:Green">显示区域</span><br />
<span style="visibility:hidden; background-color:Blue">隐藏区域</span>
<span style="visibility:visible; background-color:Green">显示区域</span>
</body>
</html>
```

## jquery控制css的display
http://iblike.iteye.com/blog/1123206
```
$("#id").show()表示display:block,
$("#id").hide()表示display:none;
$("#id").toggle()切换元素的可见状态。如果元素是可见的，切换为隐藏的；如果元素是隐藏的，切换为可见的。

# 设置display属性
$("#id").css('display', 'none');
$("#id").css('display', 'block');
或
$("#id")[0].style.display = 'none';

# 获取display属性
$("#id").css('display');
document.getElementById('id').style.display

$("#id")返回的是JQuery, 它是个集合肯定没有display属性
```

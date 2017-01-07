## Markdown guide links
```
http://www.markdown.cn/
http://www.tuicool.com/articles/fmeMbqR
```

This is an H1
=============

This is an H2
-------------

# 这是 H1

## 这是 H2

###### 这是 H6

# 这是 H1 #

## 这是 H2 ##

### 这是 H3 ######

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

> 这是一级引用
>>这是二级引用
>>> 这是三级引用

>这是一级引用


> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.


> ## 这是一个标题。
> 
> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
> 
> 给出一些例子代码：
> 
>     return shell_exec("echo $input | $markdown_script");


## \*
*   Red
*   Green
*   Blue

## \+
+   Red
+   Green
+   Blue

## \-
-   Red
-   Green
-   Blue

## order
1.  Bird
2.  McHale
3.  Parish


*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.


*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.

*   A list item with a blockquote:
> This is a blockquote
>> inside a list item.

~~这是一条删除线~~

这是一个注脚测试[^footnote]。

[^footnote]: 这是一个测试，用来阐释注脚。

* * *

***

*****

- - -

---------------------------------------

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

See my [About](/about/) page for details.

This is [an example][id] reference-style link.

[id]: http://example.com/  "Optional Title Here"


*single asterisks*

_single underscores_

**double asterisks**

__double underscores__


![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")
![Alt text][id]
[id]: url/to/image  "Optional title attribute"
![Markdown](http://images.cnitblog.com/blog/404392/201501/122257231047591.jpg)


```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<div>hello world</div>
</body>
</html>>
```

```javascript
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
```
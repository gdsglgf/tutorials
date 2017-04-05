
org.codehaus.jackson.map.JsonMappingException: No serializer found for class
通常这个异常是没有给属性添加setter/getter
方法1
加上get/set

方法2
修改属性可见性
2.1  mapper级别
objectMapper.setVisibility(PropertyAccessor.FIELD, Visibility.ANY);
2.2 class 级别
@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class MyDtoNoAccessors { ... }


## python3 list sort
data.sort(lambda a,b : cmp(a[1], b[1]))
TypeError: must use keyword argument for key function

python3
>>help(list.sort)
>>L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

>>help(sorted)
>>sorted(iterable, key=None, reverse=False) --> new sorted list

fix it:
data.sort(key=lamdda a : a[1])


## Jsoup URL 403 Forbidden
解决网站反爬虫问题，添加请求信息header
```
# http://blog.csdn.net/huaishuming/article/details/41042403

String url = "http://cn.xxxx.com/xx/xx/";
doc = Jsoup.connect(url).header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0").get();

Document doc = Jsoup.connect("http://example.com")
  .data("query", "Java")
  .userAgent("Mozilla")
  .cookie("auth", "token")
  .timeout(3000)
  .post();
```
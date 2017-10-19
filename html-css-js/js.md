## get value by key in json
```
getJson('age');

function getJson(key){
    var jsonObj={"name":"傅红雪","age":"24","profession":"刺客"};
    //1、使用eval方法    
    var eValue=eval('jsonObj.'+key);
    alert(eValue);
    //2、遍历Json串获取其属性
    for(var item in jsonObj){
        if(item==key){  //item 表示Json串中的属性，如'name'
            var jValue=jsonObj[item];//key所对应的value
            alert(jValue);
        }
    }
    //3、直接获取
    alert(jsonObj[key]);
}
```

## json parse and stringify
```
text = '{"name":"tom", "age":20}'
# string to json
eval('('+text+')')
JSON.parse(text)

# json to string
stu = {"name":"tom", "age":20}
JSON.stringify(stu)
```

## IIFE (immediately-invoked function expression) 执行一次的函数表达式
- https://toddmotto.com/what-function-window-document-undefined-iife-really-means/
```
(function(){})();

(function (window, document, undefined) {})(window, document);
```

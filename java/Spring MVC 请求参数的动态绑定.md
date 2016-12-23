# Spring MVC 请求参数的动态绑定

## Links
SpringMVC强大的数据绑定（1）
http://jinnianshilongnian.iteye.com/blog/1698916

SpringMVC强大的数据绑定（2）
http://jinnianshilongnian.iteye.com/blog/1705701

数据绑定
http://blog.sina.com.cn/s/blog_a85398ce0101feek.html


## Spring MVC 请求参数的动态绑定注解
```
1、@RequestParam绑定单个请求参数值；
2、@PathVariable绑定URI模板变量值；
3、@CookieValue绑定Cookie数据值
4、@RequestHeader绑定请求头数据；
5、@ModelValue绑定参数到命令对象；
6、@SessionAttributes绑定命令对象到session；
7、@RequestBody绑定请求的内容区数据并能进行自动类型转换等。
8、@RequestPart绑定“multipart/data”数据，除了能绑定@RequestParam能做到的请求参数外，还能绑定上传的文件等。

除了上边提到的注解，还可以通过如HttpServletRequest等API得到请求数据，但推荐使用注解方式，因为使用起来更简单
request.getParameter("username");
```

## @RequestParam
```
功能：用于将请求参数区数据映射到功能处理方法的参数上。
例子：
@RequestMapping(value="/requestparam1", method = { RequestMethod.GET, RequestMethod.POST })
public String requestparam1(@RequestParam String username)
1：如果请求中包含username参数（如/requestparam1?username=zhang），则自动传入。
2：也可以使用@RequestParam("username")明确告诉Spring Web MVC使用username进行入参

@RequestParam的主要参数
value：参数名字，即入参的请求参数名字，如username表示请求的参数区中的名字为username的参数的值将传入；
required：是否必须，默认是true，表示请求中一定要有相应的参数，否则将报400错误码；
defaultValue：默认值，表示如果请求中没有同名参数时的默认值，默认值可以是SpEL表达式，
如“#{systemProperties[‘java.vm.version’]}”。

例子1：public String test(@RequestParam(value="username",required=false) String username)
表示请求中可以没有名字为username的参数，如果没有默认为null，需注意如下几点：
（1）：原子类型：必须有值，否则抛出异常，如果允许空值请使用包装类代替。
（2）：Boolean包装类型类型：默认Boolean.FALSE，其他引用类型默认为null。

例子2：public String requestparam5(
	@RequestParam(value="username", required=true, defaultValue="zhang") String username) 
表示如果请求中没有名字为username的参数，默认值为“zhang”。
如果请求中有多个同名的应该如何接收呢？如给用户授权时，可能授予多个权限，先看如下代码：
public String test(@RequestParam(value="role") String roleList)
如果请求参数类似于url?role=admin&role=user，则实际roleList参数入参的数据为“admin，user”，即多个数据之间使用“，”分割；
我们应该使用如下方式来接收多个请求参数：
public String test(@RequestParam(value="role") String[] roleList)
或
public String test(@RequestParam(value="list") List list)
```


## @PathVariable
```
功能：用于将请求URL中的模板变量映射到功能处理方法的参数上
例子：
@RequestMapping(value="/users/{userId}/topics/{topicId}")
public String test(
       @PathVariable(value="userId") int userId,
       @PathVariable(value="topicId") int topicId)

如请求的URL为“控制器URL/users/123/topics/456”，则自动将URL中模板变量{userId}和{topicId}绑定到通过
@PathVariable注解的同名参数上，即入参后userId=123、topicId=456
```


## @CookieValue
```
功能：用于将请求的Cookie数据映射到功能处理方法的参数上
例子1：
public String test(@CookieValue(value="JSESSIONID", defaultValue="") String sessionId)

如上配置将自动将JSESSIONID值入参到sessionId参数上，defaultValue表示Cookie中没有JSESSIONID时默认为空。
例子2：
public String test2(@CookieValue(value="JSESSIONID", defaultValue="") Cookie sessionId)

传入参数类型也可以是javax.servlet.http.Cookie类型。

@CookieValue也拥有和@RequestParam相同的三个参数，含义一样。
```


## @RequestHeader
```
功能：用于将请求的头信息区数据映射到功能处理方法的参数上
例子：
@RequestMapping(value="/header")
public String test(
       @RequestHeader("User-Agent") String userAgent,
       @RequestHeader(value="Accept") String[] accepts)
     

如上配置将自动将请求头“User-Agent”值入参到userAgent参数上，并将“Accept”请求头值入参到accepts参数上。

@RequestHeader也拥有和@RequestParam相同的三个参数，含义一样。
```



## @ModelAttribute
```
@ModelAttribute一般具有如下三个作用：
1：绑定请求参数到命令对象：放在功能处理方法的入参上时，用于将多个请求参数绑定到一个命令对象，
从而简化绑定流程，而且自动暴露为模型数据用于视图页面展示时使用；
2：暴露表单引用对象为模型数据：放在处理器的一般方法（非功能处理方法）上时，是为表单准备要展示的表单引用对象，
如注册时需要选择的所在城市等，而且在执行功能处理方法（@RequestMapping注解的方法）之前，
自动添加到模型对象中，用于视图页面展示时使用；
3：暴露@RequestMapping方法返回值为模型数据：放在功能处理方法的返回值上时，是暴露功能处理方法的返回值为模型数据，
用于视图页面展示时使用。

一、绑定请求参数到命令对象
如实现用户登录，需要捕获用户登录的请求参数（用户名、密码）并封装为用户对象，此时可以使用@ModelAttribute
绑定多个请求参数到我们的命令对象。
例子：public String test1(@ModelAttribute("user") UserModel user)
说明：1：和前面命令/表单对象一样，只是此处多了一个注解@ModelAttribute(“user”)
，它的作用是将该绑定的命令对象以“user”为名称添加到模型对象中供视图页面展示使用。我们此时可以在视图页面使用
${user.username}来获取绑定的命令对象的属性。
2：绑定请求参数到命令对象支持对象图导航式的绑定，如请求参数包含
“?username=zhang&password=123&workInfo.city=bj”自动绑定到user中的workInfo属性的city属性中。
3：@RequestMapping(value="/model2/{username}")
public String test2(@ModelAttribute("model") UserModel model) {
URI模板变量也能自动绑定到命令对象中，当你请求的URL中包含“&username=zhang”会自动绑定到命令对象上。
当URI模板变量和请求参数同名时， 请求参数具有高优先权。


二、暴露表单引用对象为模型数据
例子1：
@ModelAttribute("cityList")
public List cityList() {
    return Arrays. asList("北京", "山东");
}
 
如上代码会在执行功能处理方法之前执行，并将其自动添加到模型对象中，在功能处理方法中可以使用Model入参，
则可以在处理方法中使用citylist了，如：
public ModelAndView handleRequest(Model m) {
List list = (List)m.asMap().get("cityList");
for(String s : list){
System.out.println("s==="+s);
}
......
}
 
例子2：
@ModelAttribute("user")  //①
public UserModel getUser(@RequestParam(value=“username", defaultValue="") String username) {
  //TODO 去数据库根据用户名查找用户对象
    } 
如你要修改用户资料时一般需要根据用户的编号/用户名查找用户来进行编辑，此时可以通过如上代码查找要编辑的用户。
也可以进行一些默认值的处理。
@RequestMapping(value="/model1") //②
public String test1(@ModelAttribute("user") UserModel user, Model model)
说明： 
此处我们看到①和②有同名的命令对象，那Spring Web MVC内部如何处理的呢：
1、首先执行@ModelAttribute注解的方法，准备视图展示时所需要的模型数据；@ModelAttribute注解方法形式参数规则
和@RequestMapping规则一样，如可以有@RequestParam等；
2、执行@RequestMapping注解方法，进行模型绑定时首先查找模型数据中是否含有同名对象，如果有直接使用，
如果没有通过反射创建一个，因此②处的user将使用①处返回的命令对象。即②处的user等于①处的user。


三、暴露@RequestMapping方法返回值为模型数据
例子：
public @ModelAttribute("user2") UserModel test3(@ModelAttribute("user2") UserModel user)

大家可以看到返回值类型是命令对象类型，而且通过@ModelAttribute(“user2”)注解，
此时会暴露返回值到模型数据（名字为user2）中供视图展示使用。
 
可能有同学会注意到，此时@RequestMapping注解方法的入参user暴露到模型数据中的名字也是user2，那么到底user2代表哪一个呢？
 
规则是：@ModelAttribute注解的返回值会覆盖@RequestMapping注解方法中的@ModelAttribute注解的同名命令对象


四、匿名绑定命令参数
例子1：
    public String test4(@ModelAttribute UserModel user, Model model)
    或   public String test5(UserModel user, Model model)
说明： 
    此时我们没有为命令对象提供暴露到模型数据中的名字，此时的名字是什么呢？
    Spring Web MVC自动将简单类名（首字母小写）作为名字暴露，
    如“cn.javass.springmvc.model.UserModel”暴露的名字为“userModel”。
例子2：
    public @ModelAttribute List test6()
    或   public @ModelAttribute List test7()
说明： 
    对于集合类型（Collection接口的实现者们，包括数组），生成的模型对象属性名为“简单类名（首字母小写）”+“List”，
    如List生成的模型对象属性名为“stringList”，List生成的模型对象属性名为“userModelList”。
其他情况一律都是使用简单类名（首字母小写）作为模型对象属性名，如Map类型的模型对象属性名为“map”。
```

## @SessionAttributes
```
功能 ：绑定命令对象到session
//1、在控制器类头上添加@SessionAttributes注解
@SessionAttributes(value = {"user"})    //①
public class SessionAttributeController
 
//2、@ModelAttribute注解的方法进行表单引用对象的创建
@ModelAttribute("user")    //②
public UserModel initUser()
 
//3、@RequestMapping注解方法的@ModelAttribute注解的参数进行命令对象的绑定
@RequestMapping("/session1")   //③
public String session1(@ModelAttribute("user") UserModel user)
 
//4、通过SessionStatus的setComplete()方法清除@SessionAttributes指定的会话数据
@RequestMapping("/session2")   //③
public String session(@ModelAttribute("user") UserModel user, SessionStatus status) {
    if(true) { //④
        status.setComplete();   }
    return "success";
}   
 
 
@SessionAttributes(value = {“user”})含义：
@SessionAttributes(value = {“user”}) 标识将模型数据中的名字为“user” 的对象存储到会话中（默认HttpSession），
此处value指定将模型数据中的哪些数据（名字进行匹配）存储到会话中，此外还有一个types属性表示模型数据中的哪些类
型的对象存储到会话范围内，如果同时指定value和types属性则那些名字和类型都匹配的对象才能存储到会话范围内。
n包含@SessionAttributes的执行流程如下所示：
① 首先根据类上的@SessionAttributes注解信息，查找会话内的对象放入到模型数据中；
② 执行@ModelAttribute注解的方法：如果模型数据中包含同名的数据，则不执行@ModelAttribute注解方法进行准备表单引用数据，
而是使用①步骤中的会话数据；如果模型数据中不包含同名的数据，执行@ModelAttribute注解的方法并将返回值添加到模型数据中；
 
③ 执行@RequestMapping方法，绑定@ModelAttribute注解的参数：查找模型数据中是否有@ModelAttribute注解的同名对象，
如果有直接使用，否则通过反射创建一个；并将请求参数绑定到该命令对象；
此处需要注意：如果使用@SessionAttributes注解控制器类之后，③步骤一定是从模型对象中取得同名的命令对象，
如果模型数据中不存在将抛出HttpSessionRequiredException Expected session attribute ‘user’(Spring3.1)
或HttpSessionRequiredException Session attribute ‘user’ required - not found in session(Spring3.0)异常。
 
④ 如果会话可以销毁了，如多步骤提交表单的最后一步，此时可以调用SessionStatus对象的setComplete()
标识当前会话的@SessionAttributes指定的数据可以清理了，此时当@RequestMapping功能处理方法执行完毕会进行清理会话数据。
```

## @Value
```
功能：用于将一个SpEL表达式结果映射到到功能处理方法的参数上
例子：
public String test(@Value("#{systemProperties['java.vm.version']}") String jvmVersion)
```

## @MatrixVariable
```
功能：用于接收URL的path中的矩阵参数
语法格式：XXX/XXX/path;name=value;name=value
开启功能：
（1）如果是xml配置的RequestMappingHandlerMapping，那么需要设置removeSemicolonContent属性为false
（2）如果是注解的方式，直接设置<mvc:annotation-driven enable-matrix-variables="true"/>就可以了
 

测试的URL为
http://localhost:9080/mvcexample/users/42;q=11;r=12/others/21;q=22;s=23
 
 
@RequestMapping(value = "/users/{userId}/others/{otherUserId}",method = RequestMethod.GET)
public void hello(
//如果只有一个地方有q，也可以这么取，但如果有多个q，这样就错了，必须像第二个那样去指定取谁的q值
// @MatrixVariable int q,
@MatrixVariable(value="q", pathVar="userId") int q1,
@MatrixVariable(value="q", pathVar="otherUserId") int q2,
@MatrixVariable Map matrixVars,
@MatrixVariable(pathVar="userId") Map userIdMatrixVars
) {
// System.out.println("q=="+q);
System.out.println("q1="+q1+",q2="+q2+",matrixVars="+matrixVars+",userIdMatrixVars="+userIdMatrixVars);
}
n 运行结果为：
q1=11,q2=22,matrixVars={q=[11, 22], r=[12], s=[23]},userIdMatrixVars={q=[11], r=[12]}
```

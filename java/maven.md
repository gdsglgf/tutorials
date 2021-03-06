# 清理target目录
mvn clean

# 运行测试
mvn test

# 打包时跳过测试
```
mvn package -DskipTests
mvn package -Dmaven.test.skip=true

使用打包命令可以检查出maven仓库中的jar包是否下载成功.
如果出现如下警告信息，说明jar有错。
[WARNING] 读取***.jar时出错; invalid LOC header (bad signature)
删除出错jar包，重新更新一下maven
```

# 导出runnable jar
在pom.xml里面添加如下配置(注意指定自己的mainClass)
```xml
<plugin>
	<artifactId>maven-assembly-plugin</artifactId>
	<configuration>
	    <archive>
	        <manifest>
	            <mainClass>org.smart.App</mainClass>
			</manifest>
		</archive>
		<descriptorRefs>
			<descriptorRef>jar-with-dependencies</descriptorRef>
		</descriptorRefs>
	</configuration>
</plugin>
```
命令行执行: mvn clean compile assembly:single
- http://www.jianshu.com/p/b6946b104b8e
- http://www.cnblogs.com/highriver/archive/2012/03/28/2421917.html

# eclipse maven建立多模块工程
- http://juvenshun.iteye.com/blog/305865
- http://www.tuicool.com/articles/RzyuAj

# jetty
- http://www.eclipse.org/jetty/documentation/current/jetty-maven-plugin.html
- http://www.blogjava.net/fancydeepin/archive/2012/06/23/maven-jetty-plugin.html


mvn exec:java -Dexec.mainClass="com.module.Main"
mvn exec:java -Dexec.mainClass="com.module.Main" -Dexec.args="arg0 arg1 arg2"
mvn exec:java -Dexec.mainClass="com.module.Main" -Dexec.classpathScope=test
mvn exec:java -Dexec.mainClass="com.module.Main" -Dexec.classpathScope=runtime
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


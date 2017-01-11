
## hadoop wordcount demo
1. 在HDFS上创建输入文件夹
hadoop fs -mkdir input

2. 上传本地文件到集群的input目录下
hadoop fs -put data/file*.txt input

3. 在集群上运行程序
hadoop jar %HADOOP_HOME%/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount input output

4. 查看HDFS上output目录内容
hadoop fs -ls output

5. 查看结果输出文件内容
hadoop fs -cat output/part-m-00000



## error and solution

http://stackoverflow.com/questions/31621032/hadoop-on-windows-error-java-home-is-incorrectly-set

Hadoop on Windows - "Error JAVA_HOME is incorrectly set."

If your JAVA_HOME path contains spaces, such as "C:\Program Files\Java\jdk1.8.0_xxx", you must use the Windows 8.3 Pathname.

Set the JAVA_HOME to something like "C:\Progra~1\Java\jdk1.8.0_xxx"


hadoop2.7.3 部署和eclipse环境搭建遇到的问题及解决方案
http://blog.csdn.net/zhply/article/details/52523229


## links
WordCount运行详解
http://www.cnblogs.com/xia520pi/archive/2012/05/16/2504205.html

hadoop2.7之Mapper/reducer源码分析
http://www.cnblogs.com/davidwang456/p/4816336.html

hadoop 代码中获取文件名
http://blog.csdn.net/bitcarmanlee/article/details/51735053
```java
((FileSplit) context.getInputSplit()).getPath().getName();
String filepath = ((FileSplit)context.getInputSplit()).getPath().toString();
```

多个Mapper和Reducer的Job
http://www.cnblogs.com/jchubby/p/5449349.html

Hadoop编码解码【压缩解压缩】机制详解
http://www.cnblogs.com/mrcharles/p/5070949.html

Hadoop中的DBInputFormat
http://blog.csdn.net/lzm1340458776/article/details/42739713

Hadoop中的DBOutputFormat
http://blog.csdn.net/lzm1340458776/article/details/42742237

http://stackoverflow.com/questions/16614029/hadoop-output-key-value-separator
```java
Configuration conf = new Configuration();
conf.set("mapred.textoutputformat.separator", ";");
```

hadoop2.x 完全分布式详细集群搭建(图文：4台机器)
http://www.cnblogs.com/781811964-Fighter/p/4930067.html

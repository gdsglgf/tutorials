
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

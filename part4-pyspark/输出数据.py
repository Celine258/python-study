from pyspark import SparkConf,SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
os.environ['HADOOP_HOME'] = "D:/hadoop-3.3.6"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
conf.set("spark.default.parallelism","1") #rdd.parallelize([    ].numSlices="1") 修改rdd分区
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1,2,3,4,5,6])
rdd2 = sc.parallelize([("张三",20),("李四",19),("王五",24)])
rdd3 = sc.parallelize([[1,2,3,4],[1,2],[5,6,7]])

#rdd.saveAsTextFile("PATH")输出的是文件夹
rdd1.saveAsTextFile("D:/Python学习/part4/output1")
rdd2.saveAsTextFile("D:/Python学习/part4/output2")
rdd3.saveAsTextFile("D:/Python学习/part4/output3")

sc.stop()
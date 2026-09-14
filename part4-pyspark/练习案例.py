from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
rdd1 = sc.textFile("D:/Python学习/part4/hello.txt")
rdd2 = rdd1.flatMap(lambda x: x.split(" "))
rdd3 = rdd2.map(lambda x: (x,1))
# print(rdd2.collect())
# print(rdd3.collect())
rdd4 = rdd3.reduceByKey(lambda a,b: a + b)
print(rdd4.collect())
sc.stop()
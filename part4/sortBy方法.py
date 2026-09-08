from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
#对RDD类型进行排序，可以自定义排序方式
#sortBy(func,ascending=False,numPartitions=1)
#函数返回排序依据的数据   True升序，False降序   使用单个分区进行排序
rdd1 = sc.textFile("D:/Python学习/part4/hello.txt")
rdd2 = rdd1.flatMap(lambda x: x.split(" "))
rdd3 = rdd2.map(lambda x: (x,1))
rdd4 = rdd3.reduceByKey(lambda a,b:a+b)
rdd5 = rdd4.sortBy(lambda x: x[1],ascending=False,numPartitions=1)
print(rdd5.collect())
sc.stop()

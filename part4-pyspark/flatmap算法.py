from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)#创建spark对象
rdd = sc.parallelize(["world 777","wdnmd dsb", "itheima 666"])
rdd2 = rdd.flatMap(lambda x: x.split(" "))#解除一层嵌套的功能
print(rdd2.collect())
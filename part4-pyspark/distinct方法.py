from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
#对RDD进行去除重复操作
rdd = sc.parallelize([1,2,3,4,5,5,3,4,5])
rdd1 = rdd.distinct()
print(rdd1.collect())
sc.stop()

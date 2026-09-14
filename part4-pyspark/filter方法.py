from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
#对rdd数据进行过滤，留下需要的数据
rdd = sc.parallelize([1,2,3,4,5])
rdd1 = rdd.filter(lambda x: x % 2 ==0)#True留下,False去除
print(rdd1.collect())
sc.stop()
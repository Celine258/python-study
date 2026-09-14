from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)#创建spark对象
rdd = sc.parallelize([1,2,3,4,5])

def func(data):
    return data*10

rdd1 = rdd.map(func)
print(rdd1.collect())
sc.stop()




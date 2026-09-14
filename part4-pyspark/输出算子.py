from pyspark import SparkConf,SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1,2,3,4,5])

#collect算子
rdd2 = rdd1.collect()#把rdd类型转化为python的对象list
print(rdd2)
print(type(rdd2))

#reduce算子
rdd3 = rdd1.reduce(lambda a,b: a+b)#按照要求的逻辑把所有数据进行两两聚合组成list返回
print(rdd3)

#take算子
rdd4 = rdd1.take(5)#取前n个数据，组成list然后返回
print(rdd4)

#count算子
rdd5 = rdd1.count()#统计rdd1内的元素个数
print(rdd5)
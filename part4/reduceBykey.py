#二元元组为kv型的RDD，如('a',1)
#根据所需逻辑进行聚合
from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)#创建spark对象
rdd1 = sc.parallelize([("man",99),("woman",90),("man",89),("woman",97)])
rdd2 = rdd1.reduceByKey(lambda a,b: a + b)
print(rdd2.collect())
sc.stop()
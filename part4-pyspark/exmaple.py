from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)#创建spark对象

print(sc.version)

sc.stop()

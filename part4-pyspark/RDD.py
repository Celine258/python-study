from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)#创建spark对象

# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((1,2,3,4,5))
# rdd3 = sc.parallelize("Celine")
# rdd4 = sc.parallelize({"key1":"value1","key2":"value2"})
# rdd5 = sc.parallelize({1,2,3,4,5})

# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())
rdd = sc.textFile("D:/Python学习/part4/test.txt")

print(rdd.collect())

sc.stop()
#数据输入本质上是为了得到rdd，一种数据集，是个数据的载体
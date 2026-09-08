from pyspark import SparkConf,SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)
rdd = sc.textFile("D:/Python学习/part4/search_data.txt")

#task1
rdd_file = rdd.map(lambda x: x.split(" "))
rdd1 = rdd_file.map(lambda x: x[0][:2]).map(lambda x: (x,1)).reduceByKey(lambda a,b: a + b).sortBy(lambda x: x[1],ascending=False,numPartitions=1)
print(rdd1.collect())
rdd1.saveAsTextFile("D:/python学习/part4/search1")

#task2
rdd2 = rdd_file.map(lambda x: x[2]).map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b).sortBy(lambda x: x[1],ascending=False,numPartitions=1).take(3)
rdd2_json = json.dumps(rdd2)
with open("D:/python学习/part4/search2.txt","w",encoding="utf-8") as f:
    f.write(rdd2_json)

#task3
rdd3 = rdd_file.filter(lambda x: x[2] == "黑马程序员").map(lambda x: (x[0][:2],1)).reduceByKey(lambda a,b: a+b).sortBy(lambda x: x[1],ascending=False,numPartitions=1).take(1)
rdd4 = rdd3[0]
rdd3_json = json.dumps(rdd4)
with open("D:/python学习/part4/search3.txt","w",encoding="utf-8") as f:
    f.write(rdd3_json)

sc.stop()
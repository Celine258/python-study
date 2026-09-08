from pyspark import SparkConf,SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
rdd1 = sc.textFile("D:/Python学习/part4/data.txt")
rdd2 = rdd1.flatMap(lambda x: x.split("|"))#注意
def fun1(data):
    return (data["areaName"],int(data["money"]))#注意把money改为int类型
rdd_json = rdd2.map(lambda x: json.loads(x))#得到字典


rdd3 = rdd_json.map(fun1)
rdd_money = rdd3.reduceByKey(lambda a,b: a + b)
#print(rdd3.collect())
rdd_sort_money = rdd_money.sortBy(lambda x: x[1],ascending=False,numPartitions=1)


rdd_types = rdd_json.map(lambda x:x["category"])
rdd_diferent_types = rdd_types.distinct()


rdd_beijin = rdd_json.filter(lambda x: x["areaName"] == "北京")
rdd_beijin_types = rdd_beijin.map(lambda x: x["category"])
rdd_beijin_diferent_types = rdd_beijin_types.distinct()
print("各地区销售额排名\n")
print(rdd_sort_money.collect())#collect()把RDD输出为python的list
print("\n")
print("销售的商品种类\n")
print(rdd_diferent_types.collect())
print("\n")
print("北京市售卖的商品有\n")
print(rdd_beijin_diferent_types.collect())


sc.stop()
import collections
from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster("local").setAppName("CustomerAmount")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    customer_id = int(fields[0])
    amount = float(fields[2])

    return (customer_id, amount)

lines = sc.textFile("/Users/kimiza/Desktop/Desktop/Python_Projects/SparkCourse/customer-orders.csv")
rdd = lines.map(parseLine)
amountsByCustomer = rdd.reduceByKey(lambda x, y: x + y)
amountsByCustomerSorted = amountsByCustomer.map(lambda x: (x[1], x[0])).sortByKey()

results = amountsByCustomerSorted.collect()

for result in results:
    print("({}, {:.2f})".format(result[1], result[0]))


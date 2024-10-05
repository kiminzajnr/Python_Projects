from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType


spark = SparkSession.builder.appName("CustomerSpendings").getOrCreate()

schema = StructType([
    StructField("customerID", IntegerType(), True),
    StructField("ItemsNo", IntegerType(), True),
    StructField("Amount", FloatType(), True),
])

df = spark.read.schema(schema).csv("customer-orders.csv")
df.printSchema()

customerByAmount = df.select("customerID", "Amount")

customerByAmountT = customerByAmount.groupBy("customerID").agg(func.round(func.sum("Amount"), 2).alias("total_spent"))

customerByAmountTsorted = customerByAmountT.sort("total_spent")

customerByAmountTsorted.show(customerByAmountTsorted.count())

spark.stop()

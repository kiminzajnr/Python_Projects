from pyspark.sql import SparkSession, functions as func


spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
people = spark.read.option("header", "true").option("inferSchema", "true").csv("fakefriends-header.csv")

friendsByAge = people.select("age", "friends")

friendsByAge.groupBy("age").avg("friends").show()

friendsByAge.groupBy("age").avg("friends").sort("age").show()

friendsByAge.groupBy("age").agg(func.round(func.avg("friends"), 2).alias("friends_avg")).sort("age").show()


spark.stop()
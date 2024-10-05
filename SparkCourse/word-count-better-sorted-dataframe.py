from pyspark.sql import SparkSession, functions as func


spark = SparkSession.builder.appName("WordCount").getOrCreate()


inputDF = spark.read.text("book.txt")


words = inputDF.select(func.explode(func.split(inputDF.value, "\\W+")).alias("word"))
wordsWithoutEmptyString = words.filter(words.word != "")

lowercaseWords = wordsWithoutEmptyString.select(func.lower(wordsWithoutEmptyString.word).alias("word"))

wordCounts = lowercaseWords.groupBy("word").count()

wordCountsSorted = wordCounts.sort("count")

wordCountsSorted.show(wordCountsSorted.count())
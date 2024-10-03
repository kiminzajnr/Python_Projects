from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("/Users/kimiza/Desktop/Desktop/Python_Projects/SparkCourse/Book")
words = input.flatMap(lambda x: x.split())
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore').decode('ascii')
    if cleanWord:
        print(cleanWord, count)
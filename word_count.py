from pyspark import SparkContext, SparkConf


sparkConf = SparkConf().setAppName("WordCounts").setMaster("local")
sc = SparkContext(conf = sparkConf)

if __name__== '__main__':

    File = sc.textFile("sample.txt")
    
    wordCounts = File.flatMap(lambda line: line.split(" ")) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a+b)
          
    for i in wordCounts.collect():
        print(i)

    wordCounts.coalesce(1).saveAsTextFile("Resultat.txt")

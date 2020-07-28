from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

# Spark session
spark = SparkSession.builder.master('yarn').getOrCreate()
sc = spark.sparkContext

# Sum of the first 100 whole numbers
rdd = sc.parallelize(range(100 + 1))
result = rdd.sum()
print(result)

# write in hadoop
spark.createDataFrame(spark.sparkContext.parallelize([result]), StringType())\
    .coalesce(1)\
        .write.\
            format("text").\
                mode("overwrite").\
                    save("hdfs://hdp-name1-esxi12.sdb247.com:8020/processed/bluebank/test")

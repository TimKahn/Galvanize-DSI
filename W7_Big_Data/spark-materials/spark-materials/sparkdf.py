# run this script like so: bash ~/scripts/localsparksubmit.sh sparkdf.py

import pyspark as ps    # for the pyspark suite

spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("df lecture") \
            .getOrCreate()

# link to the S3 repository
link = 's3a://dsi-spark-day/airline_data.csv'

# creating an RDD...
df = spark.read.csv(link, header=True, inferSchema=True)


print(df.show())
print(df.count())

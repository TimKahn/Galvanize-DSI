# run this script like so: bash ~/scripts/localsparksubmit.sh sparkrdd.py

import pyspark as ps    # for the pyspark suite


spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("df lecture") \
            .getOrCreate()


sc = spark.sparkContext

# link to the S3 repository
link = 's3a://dsi-spark-day/airline_data.csv'

# creating an RDD...
rdd = sc.textFile(link)

print('{}{}{}'.format('-'*500, rdd.count(), '-'*500))

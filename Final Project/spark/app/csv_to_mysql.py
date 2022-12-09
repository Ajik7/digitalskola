import pyspark
from pyspark.sql import SparkSession

# Create spark session
if __name__ == "__main__":
    spark = SparkSession.builder\
    .appname("mysql")\
    .getOrCreate()

#Parameter
application_train = "/usr/local/spark/resources/application_train.csv"
application_test = "/usr/local/spark/resources/application_test.csv"
mysql_driver = "com.mysql.jdbc.Driver"
mysql_url = f"jdbc:mysql://localhost:3306/mysql"
mysql_user = "root"
mysql_password="anypassword"


#Read CSV
df_train = (
    spark.read
    .format("csv")
    .option("header", True)
    .load(application_train)
)

df_test = (
    spark.read
    .format("csv")
    .option("header", True)
    .load(application_test)
)

# Load data to Mysql
(
    df_train.write
    .format("jdbc")
    .option("driver", mysql_driver)
    .option("url", mysql_url)
    .option("dbtable", "application_train")
    .option("user", mysql_user)
    .option("password", mysql_password)
    .save()
)
(
    df_test.write
    .format("jdbc")
    .option("driver", mysql_driver)
    .option("url", mysql_url)
    .option("dbtable", "application_test")
    .option("user", mysql_user)
    .option("password", mysql_password)
    .save()
)

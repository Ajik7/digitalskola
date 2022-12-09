import pyspark
from pyspark.sql import SparkSession

# Create spark session
if __name__ == "__main__":
    spark = SparkSession.builder\
    .appname("postgre")\
    .getOrCreate()

#Parameter mysql
mysql_driver = "com.mysql.jdbc.Driver"
mysql_url = f"jdbc:mysql://localhost:3306/mysql"
mysql_user = "root"
mysql_password="anypassword"

#Parameter postgre
postgre_server = "localhost"
postgre_port = "5432"
postgre_user = "postgres"
postgre_password = "postgres"
postgre_url = f"jdbc:postgresql://localhost:5432/postgres"

#Read Mysql db
df_train = (
    spark.read
    .format("jdbc")
    .option("driver", mysql_driver)
    .option("url", mysql_url)
    .option("dbtable", "application_train")
    .option("user", mysql_user)
    .option("password", mysql_password)
    .load()
)

df_test = (
     spark.read
    .format("jdbc")
    .option("driver", mysql_driver)
    .option("url", mysql_url)
    .option("dbtable", "application_test")
    .option("user", mysql_user)
    .option("password", mysql_password)
    .load()
)

# Load data to postgre
(
    df_train.write
    .format("jdbc")
    .option("server", postgre_server)
    .option("url", postgre_url)
    .option("dbtable", "application_train")
    .option("user", postgre_user)
    .option("password", postgre_password)
    .save()
)
(
    df_test.write
    .format("jdbc")
    .option("server", postgre_server)
    .option("url", postgre_url)
    .option("dbtable", "application_test")
    .option("user", postgre_user)
    .option("password", postgre_password)
    .save()
)

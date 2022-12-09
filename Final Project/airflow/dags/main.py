import airflow
from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 
from airflow.utils.dates import days_ago

#parameter
spark_master = "spark://spark:8081"

default_args = {
    'owner': 'airflow',    
    #'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(),
    # 'depends_on_past': False,
    # 'email': ['airflow@example.com'],
    # 'email_on_failure': False,
    #'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    #'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag1 = DAG(
        dag_id="csv_to_mysql", 
        schedule_interval=None
    )
dag2 = DAG(
        dag_id="mysql_to_postgre", 
        schedule_interval=None
    )

dag3 = DAG(
        dag_id="mongodb", 
        schedule_interval=None
    )


start = DummyOperator(task_id="start", dag1=dag1, dag2=dag2, dag3=dag3, dag4=dag4)

#csv to mysql
csv_to_mysql = SparkSubmitOperator(
    task_id="csv_to_mysql",
    application="/usr/local/spark/app/csv_to_mysql.py", 
    conn_id="spark_default",
    conf={"spark.master":spark_master},
    dag1=dag1)

#mysql to postgre
mysql_to_postgre = SparkSubmitOperator(
    task_id="mysql_to_postgre",
    application="/usr/local/spark/app/mysql_to_postgre.py", 
    conn_id="spark_default",
    conf={"spark.master":spark_master},
    dag2=dag2)

#mongodb
mongodb = SparkSubmitOperator(
    task_id="mongodb",
    application="/usr/local/spark/app/mongodb.py", 
    conn_id="spark_default",
    conf={"spark.master":spark_master},
    dag3=dag3)

#kafka


import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from varadharajan_gmail_com_team_bh_test_pipeline3.tasks import (
    EMRClusterSensor_1,
    EMRCreateCluster_1,
    EMRPipelineSensor_1,
    EMRPipeline_1,
    Email_1,
    HTTPSensor1,
    S3FileSensor2,
    SFTPSensor_1,
    SFTPToS3_1,
    SFTPToSnowflake_1,
    Slack_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "varadharajan_gmail_com_team_BH_TEST_pipeline3", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    SFTPSensor_1_op = SFTPSensor_1()
    EMRPipeline_1_op = EMRPipeline_1()
    HTTPSensor1_op = HTTPSensor1()
    S3FileSensor2_op = S3FileSensor2()
    EMRPipelineSensor_1_op = EMRPipelineSensor_1()
    EMRClusterSensor_1_op = EMRClusterSensor_1()
    SFTPToS3_1_op = SFTPToS3_1()
    SFTPToSnowflake_1_op = SFTPToSnowflake_1()
    Email_1_op = Email_1()
    Slack_1_op = Slack_1()
    EMRCreateCluster_1_op = EMRCreateCluster_1()
    SFTPToS3_1_op >> SFTPToSnowflake_1_op
    EMRPipelineSensor_1_op >> EMRClusterSensor_1_op
    EMRPipeline_1_op >> EMRCreateCluster_1_op
    SFTPSensor_1_op >> [EMRPipeline_1_op, SFTPToS3_1_op]
    S3FileSensor2_op >> EMRPipelineSensor_1_op
    SFTPToSnowflake_1_op >> Email_1_op
    HTTPSensor1_op >> S3FileSensor2_op
    Email_1_op >> Slack_1_op

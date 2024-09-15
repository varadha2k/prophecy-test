from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def EMRCreateCluster_1():
    from airflow.providers.amazon.aws.operators.emr import (EmrCreateJobFlowOperator, )
    from datetime import timedelta

    return EmrCreateJobFlowOperator(
        task_id = "EMRCreateCluster_1",
        aws_conn_id = "BH-Dev-AWS",
        emr_conn_id = None,
        region_name = None,
    )

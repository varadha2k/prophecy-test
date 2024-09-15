from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def EMRClusterSensor_1():
    from airflow.providers.amazon.aws.sensors.emr import (EmrJobFlowSensor, ) # noqa
    from datetime import timedelta

    return EmrJobFlowSensor(
        task_id = "EMRClusterSensor_1",
        job_flow_id = "cluster2",
        aws_conn_id = "aws_default",
        target_states = [],
        failed_states = ["STARTING"],
        # max_attempts=self.props.maxAttempts, Only supported in Airflow 2.7.0+
        timeout = 600,
    )

from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def EMRPipelineSensor_1():
    from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor # noqa
    from datetime import timedelta

    return EmrStepSensor(
        task_id = "EMRPipelineSensor_1",
        job_flow_id = "j-11FIPPFJGAJE9",
        aws_conn_id = "aws_default",
        step_id = "{step1}",
        # max_attempts=self.props.maxAttempts, Only supported in Airflow 2.7.0+
        timeout = 600,
    )

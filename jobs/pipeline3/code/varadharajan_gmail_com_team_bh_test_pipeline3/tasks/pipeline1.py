from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

@task_wrapper(task_id = "pipeline1")
def pipeline1(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "pipeline1",
        json = {"task_key" : "pipeline1"},
        databricks_conn_id = "BH-Dev-AWS",
    )

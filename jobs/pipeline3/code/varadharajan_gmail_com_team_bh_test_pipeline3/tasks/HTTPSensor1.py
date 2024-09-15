from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def HTTPSensor1():
    from airflow.providers.http.sensors.http import HttpSensor
    from datetime import timedelta

    # Execution timeout is airflow task level execution timeout
    # Sensor timeout will be different. Should be handled separately
    return HttpSensor(
        task_id = "HTTPSensor1",
        endpoint = "endpoint",
        request_params = {'paran1' : 'value1'},
        headers = {'paran1' : 'value1'},
        response_check = None,
        http_conn_id = "Fabric-airflow_HTTP",
        poke_interval = 60,
        timeout = 600,
    )

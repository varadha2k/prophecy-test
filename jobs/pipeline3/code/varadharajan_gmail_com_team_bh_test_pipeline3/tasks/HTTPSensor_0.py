from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def HTTPSensor_0():
    from airflow.providers.http.sensors.http import HttpSensor
    from datetime import timedelta

    # Execution timeout is airflow task level execution timeout
    # Sensor timeout will be different. Should be handled separately
    return HttpSensor(
        task_id = "HTTPSensor_0",
        endpoint = "",
        request_params = None,
        headers = None,
        response_check = None,
        http_conn_id = None,
        poke_interval = 60,
        timeout = 600,
    )

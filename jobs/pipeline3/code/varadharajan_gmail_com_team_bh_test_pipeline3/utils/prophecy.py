from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/Pipeline2": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/Pipeline2-1.0-py3-none-any.whl", 
    "pipelines/pipeline1": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline1-1.0-py3-none-any.whl", 
    "pipelines/pipeline4": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline4-1.0-py3-none-any.whl"
}
emr_pipeline_id_to_path_dict = {
    "pipelines/Pipeline2": "s3://prophecytesting/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/Pipeline2-1.0-py3-none-any.whl", 
    "pipelines/pipeline1": "s3://prophecytesting/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline1-1.0-py3-none-any.whl", 
    "pipelines/pipeline4": "s3://prophecytesting/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline4-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/pipeline1": "pipeline1", 
    "pipelines/Pipeline2": "Pipeline2", 
    "pipelines/pipeline4": "pipeline4"
}

import boto3
import json
import logging
import pprint

def l_p():
#   logger = logging.getLogger()
#   logger.setLevel(logging.INFO)
#   logger.debug(json.dumps(event))

  codepipeline = boto3.client('codepipeline')
#   s3 = boto3.client('s3')
#   job_id = event['CodePipeline.job']['id']

  try:
    #   user_parameters = event['CodePipeline.job']['data']['actionConfiguration']['configuration']['UserParameters']
    #   logger.info(f'User parameters: {user_parameters}')
      response = codepipeline.list_pipelines()
    #   pp = pprint.PrettyPrinter(indent=2)
    #   pp.pprint(response)
    #   print(response["pipelines"]["name"][0])
    #   print(response["pipelines"][0]["name"])
      for i in response["pipelines"]:
          print (i["name"])
    #   json_object = json.loads(response)
    #   json_formatted_str = json.dumps(json_object, indent=2)
    #   print(json_formatted_str)
    #   print (response)
    #   logger.debug(response)
  except Exception as error:
      logger.exception(error)
    #   response = codepipeline.put_job_failure_result(
    #       jobId=job_id,
    #       failureDetails={
    #         'type': 'JobFailed',
    #         'message': f'{error.__class__.__name__}: {str(error)}'
    #       }
    #   )
    #   logger.debug(response)

def list_pipelines():
    session= boto3.client("sts")
    # session = boto3.Session(
    #     aws_access_key_id="AKIAJMO63R4OAY6HMXUQ",
    #     aws_secret_access_key="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"
    # )
    # credentials = session.get_credentials()
    # print credentials
    code_pipeline = boto3.client('codepipeline')
    # pipelines = code_pipeline.list_pipelines(nextToken=credentials.token)
    pipelines = code_pipeline.list_pipelines()
    while pipelines['hasMoreResults']:
        pipelines = code_pipeline.list_pipelines(nextToken=pipelines['marker'])
        for i in pipelines:
            print (i)


def main():
    # list_pipelines()
    l_p()
    
if __name__ == "__main__":
    main()

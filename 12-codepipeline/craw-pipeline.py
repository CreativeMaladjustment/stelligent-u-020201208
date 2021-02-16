import boto3
# import json
import logging
# import pprint

def l_p():
#   logger = logging.getLogger()
#   logger.setLevel(logging.INFO)
#   logger.debug(json.dumps(event))

  codepipeline = boto3.client('codepipeline')
#   s3 = boto3.client('s3')
#   job_id = event['CodePipeline.job']['id']

  try:
      response = codepipeline.list_pipelines()
    #   pp = pprint.PrettyPrinter(indent=2)
    #   pp.pprint(response)
    #   print(response["pipelines"]["name"][0])
    #   print(response["pipelines"][0]["name"])
      for i in response["pipelines"]:
          print (i["name"])
    #   logger.debug(response)
  except Exception as error:
      logger.exception(error)
    #   logger.debug(response)

def main():
    l_p()
    
if __name__ == "__main__":
    main()

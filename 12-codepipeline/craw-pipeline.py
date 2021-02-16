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
        #   print (i["name"])
          response = codepipeline.list_pipeline_executions(pipelineName=i["name"],maxResults=99)
        #   print (response)
          for i_lpe in response["pipelineExecutionSummaries"]:
            #   print (i_lpe["name"])
              print (i["name"], "id:", i_lpe["pipelineExecutionId"], i_lpe["status"])
            #   print (i_lpe)
    #   logger.debug(response)
  except Exception as error:
      logger.exception(error)
    #   logger.debug(response)

def main():
    l_p()
    
if __name__ == "__main__":
    main()

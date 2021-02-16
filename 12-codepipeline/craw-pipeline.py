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
          response_lae = codepipeline.list_action_executions(pipelineName=i["name"],maxResults=99)
        #   print (response)
          for i_lae in response_lae["actionExecutionDetails"]:
            #   print (i_lpe["name"])
              print (i["name"], "action id:", i_lae["pipelineExecutionId"], i_lae["actionExecutionId"], i_lae["status"])
#              print (i_lae)
              #, i_lae["status"], i_lae["output"]["executionResult"]["externalExecutionSummary"])
              try:
                  print ("rawr", i_lae["output"]["executionResult"]["externalExecutionSummary"])
              except:
                  print ("no summary")

  except Exception as error:
      logger.exception(error)
    #   logger.debug(response)

def main():
    l_p()
    
if __name__ == "__main__":
    main()

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
              print ("===pipelinename:",i["name"])
              print ("===pipeline exe id:", i_lae["pipelineExecutionId"])
              print ("pipeline events")
              print (i_lae["stageName"], "name = StringField(max_length=120, required=True)")
              print (i_lae["pipelineExecutionId"], "number = IntField()")
              print ("repo = StringField(max_length=200)")
              print ("branch = StringField(max_length=50)")
              print ("sha = StringField(max_length=50)")
              print ("commit_id = StringField(max_length=50)")

              print ("build_files = ListField(StringField(max_length=128))")
              print ("file_count = IntField()")

              print (i_lae["actionExecutionId"], "buildnumber = IntField(required=True)")
              print ("building = BooleanField(required=True)")
              actionduration=(i_lae["lastUpdateTime"] - i_lae["startTime"]).microseconds
              print (actionduration, "duration_millis = IntField()")
              print (i_lae["status"], "result = StringField(max_length=50)")
              print (i_lae["startTime"], "timestamp = DateTimeField()")
              print ("url = StringField(max_length=256)")

              print ("fail_stage = StringField(max_length=50)")
              print ("fail_logs = StringField(max_length=10000)")
    
              try:
                  print ("rawr", i_lae["output"]["executionResult"]["externalExecutionSummary"])
              except:
                  print ("no summary")

  except Exception as error:
    print("had an error:", error)
      # logger.exception(error)
    #   logger.debug(response)

def main():
    l_p()
    
if __name__ == "__main__":
    main()

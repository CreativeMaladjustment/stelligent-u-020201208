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

### from mongo db - a pipeline_run record/document
# {
#     _id: ObjectId('5f73a4f8e6a5ccfdadef1c31'),
#     name: 'archive-mono-pr',
#     buildnumber: 1,
#     building: false,
#     durationMillis: 10843522,
#     result: 'SUCCESS',
#     timestamp: ISODate('2020-03-18T16:38:31.402Z'),
#     url: 'https://jenkins.mono-project.com/job/archive-mono-pr/1/',
#     tags: []
# }

# pipelines name
# ??? a git pr number ??? or an lae value? a guid execution id.... 
# based on status
# pipeline lastupdate - starttime
# status
# lastupdate 
# latest source revision - (in gui/console) / didn't see in lpe will be in some lae's 
# tags?


      for i in response["pipelines"]:
          response = codepipeline.list_pipeline_executions(pipelineName=i["name"],maxResults=99)
          for i_lpe in response["pipelineExecutionSummaries"]:
              print ("pipeline execution summaries")
              print (i["name"], "id:", i_lpe["pipelineExecutionId"], i_lpe["status"])
              pipelineduration=(i_lpe["lastUpdateTime"] - i_lpe["startTime"]).microseconds
              print (pipelineduration, "??-- duration_millis = IntField()")
              print (i_lpe["sourceRevisions"][0]["revisionUrl"], "??--commit_id = StringField(max_length=50)")

          response_lae = codepipeline.list_action_executions(pipelineName=i["name"],maxResults=99)
          for i_lae in response_lae["actionExecutionDetails"]:
              print ("===pipelinename:",i["name"])
              print ("===pipeline exe id:", i_lae["pipelineExecutionId"])
              print ("pipeline events")
              print (i_lae["stageName"], "name = StringField(max_length=120, required=True)")
              print (i_lae["pipelineExecutionId"], "number = IntField()")
              try:
                  print (i_lae["output"]["executionResult"]["externalExecutionUrl"], "repo = StringField(max_length=200)")
              except:
                  print ("not available", "repo = StringField(max_length=200)")
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

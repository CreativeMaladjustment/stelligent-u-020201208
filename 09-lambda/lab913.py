import json
def lab913(event, context):
    print("value1 = " + event['key1'])
    return event['key1']
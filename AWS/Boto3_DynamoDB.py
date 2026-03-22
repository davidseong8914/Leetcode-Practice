# set up IAM
# set up table

import sys
import datetime
import time
import boto3

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table("test_table")

# table.put_item(
#     Item = {
#         'test_id': "3", # important
#         'name'  : "San Andres",
#         'Age'   : "24" 
#     }
# )


response = table.get_item(
    Key = {
        'test_id' : "1"
    }
)
# print(response['Item'])
print(response)


# S3


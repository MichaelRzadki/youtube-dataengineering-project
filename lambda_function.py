import awswrangler as awswr
import pandas as pd
import urllib.parse
import os


#set up os environment variables 
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']


def lambda_handler(event, context):
    # Obtain the object from selected event and display the content type
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:

        # Create the dataframe using the capture content
        df_raw = awswr.s3.read_json('s3://{}/{}'.format(s3_bucket, key))

        #Process only the required columns of data "items":
        df_data = pd.json_normalize(df_raw['items'])

        # Write the data to S3
        awswr_response = awswr.s3.to_parquet( df=df_data, path=os_input_s3_cleansed_layer, dataset=True, database=os_input_glue_catalog_db_name, table=os_input_glue_catalog_table_name, mode=os_input_write_data_operation)

        return awswr_response
    
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Ensure it exists and that the bucket is in the same region.'.format(key, s3_bucket))
        raise e
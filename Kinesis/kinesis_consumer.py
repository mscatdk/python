import boto3
import time
import json
import os.path

def create_checkpoint(record_response):
    if len(record_response['Records']) != 0:
        with open(checkpoint_path, 'w+') as f:
            f.write(record_response['Records'][0]['SequenceNumber'])

def get_shard_iterator():
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path) as f:
            checkpoint = f.read()
    
        print("Reading from Sequence Number %s" % checkpoint)

        shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='AT_SEQUENCE_NUMBER',
                                                      StartingSequenceNumber=checkpoint
                                                      )
    else:
        print("Reading from latest...")
        shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST'
                                                      )                                                       
    return shard_iterator['ShardIterator']

def message_processor(record):
    print(record['Data'])
    time.sleep(1)

kinesis_client = boto3.client('kinesis')

my_stream_name='demo'
batch_size = 3

response = kinesis_client.describe_stream(StreamName=my_stream_name)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
checkpoint_path = "checkpoint.txt"

my_shard_iterator = get_shard_iterator()

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=batch_size)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=batch_size)

    for record in record_response['Records']:
        message_processor(record)
        
    create_checkpoint(record_response)
    if len(record_response['Records']) == 0:
        print("Sleeping...")
        time.sleep(3)
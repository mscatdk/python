import boto3
import time

kinesis_client = boto3.client('kinesis', region_name="eu-west-2")


kinesisRecords = []
shardCount = 1
streamName = 'demo'

counter = 0
n = 10

while True:
    print("Starting %d" % counter)
    for i in range(counter, counter + n):

        encodedValues = str(i).encode()
        print(encodedValues)

        kinesisRecord = {
            "Data": encodedValues,
            "PartitionKey": str(shardCount)
        }

        kinesisRecords.append(kinesisRecord)


    response = kinesis_client.put_records(
                    Records=kinesisRecords,
                    StreamName = streamName)

    kinesisRecords.clear()
    counter += n
    print("Sleeping...")
    time.sleep(5)
        

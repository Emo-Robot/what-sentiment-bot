import boto3
# https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html
# https://jualabs.com/2021/03/02/criando-um-crud-basico-em-python-com-dynamodb/


def create_utils_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.create_table(
        TableName='Utils',
        KeySchema=[
            {
                'AttributeName': 'since_id',
                'KeyType': 'HASH'  # Just hash beacause there will be no other since id
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'since_id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table

utils_table = create_utils_table()
print(utils_table.table_status)
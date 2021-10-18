import boto3
# https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html
# https://jualabs.com/2021/03/02/criando-um-crud-basico-em-python-com-dynamodb/


def get_dynamo(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name="us-east-1")
        return dynamodb


def create_utils_table(dynamodb=None):
    dynamodb = get_dynamo(dynamodb)
    table = None
    try:
        table = dynamodb.create_table(
            TableName='Utils',
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
    except:
        print('create_utils_table ERRO')
    return table


def put_since_id(since_id, dynamodb=None):
    dynamodb = get_dynamo(dynamodb)
    table = dynamodb.Table('Utils')
    print("adding since id:", since_id)
    response = table.put_item(
        Item={
            'name': 'since_id',
            'since_id': since_id
        }
    )
    return response

def get_since_id(dynamodb=None):
    dynamodb = get_dynamo(dynamodb)
    table = dynamodb.Table('Utils')
    response = table.scan()
    since_id = response['Items'][0]['since_id']
    print("Utils table items:",response['Items'])
    return int(since_id)
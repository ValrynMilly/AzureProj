import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PatitionKey


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    numbers = requests.get('servicoone.azurewebsites.net/api/Servicetwo?code=i1RrTrqAOZYz3tYrNOWeHF0CvusKkphai8DF5C5AnQSdUSLiAZ6Q0A==').text
    letters = requests.get('servicoone.azurewebsites.net/api/Servicethree?code=6UOXpQpR2q9LTNEr9jkwHjB0XpwFqdqoN8FS72mmIrTq5YkYjatEvg==').text
    username = ""
    for i in range(5):
        username += numbers[i]
        username += letters[i]
        
        key = ''
    endpoint = ''

    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    database = client.create_database_if_not_exists(id=database_name)

    container_name = "UsernameCont"
    container = database.create_container_if_not_exists(
        id=container_name,
        Partition_key=PartitionKey(path="/username") 
    )
    username_to_add = {
        "id": username
    }
    container.create_iteam(body=username_to_add)
    return username
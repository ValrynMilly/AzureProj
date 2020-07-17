import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = "123456789"
    numberset = ""
    for i in range(5):
        numberset += random.choice(numbers)
    return numberset
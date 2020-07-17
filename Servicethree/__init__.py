import logging
import random
import azure.functions as func
from string import ascii_uppercase

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    stringname = ""
    for i in range(5):
        stringname += random.choice(ascii_uppercase)
    return stringname
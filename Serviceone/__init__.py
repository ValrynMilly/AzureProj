import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    numbers = requests.get('ekserverless.azurewebsites.net/api/servicetwo?code=ZXKVAyF2SHjWtTlkIE7Lkgpl15p7iscRDgwdIGbVnZXQe/8irZzhmg==').text
    letters = requests.get('ekserverless.azurewebsites.net/api/servicethree?code=uPPdbgzMpzq8gjyqcFkM676N5pjilx/aN/oJt3asMuCZVGC7yWOM1A==').text
    useername = ""
    for i in range(5):
        useername += numbers[i]
        useername += letters[i]
        
    return useername
    
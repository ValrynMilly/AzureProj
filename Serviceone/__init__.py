import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letterstring = req.route_params.get('http://localhost:7071/api/Service2')
    nostring = req.route_params.get('http://localhost:7071/api/Service3')
    counter = 0
    output = ''
    while counter < len(letterstring):
        output = output + letterstring[counter]
        output = output + nostring[counter]
        counter += 1
    somemessage = f"{output}"
    return func.HttpResponse(somemessage)

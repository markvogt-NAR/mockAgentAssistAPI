# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(helloworldfunction02) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging

helloworldfunction02 = func.Blueprint()


@helloworldfunction02.route(route="helloworldfunction02", auth_level=func.AuthLevel.FUNCTION)
def helloworldfunction02(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered helloworldfunction02 which executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered helloworldfunction02 which executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
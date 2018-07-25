import requests



def dummy_call():
    response = requests.get("http://localhost:9876/product")

    return response


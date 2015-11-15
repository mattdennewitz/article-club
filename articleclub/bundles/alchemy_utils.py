from alchemy_api.alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

def get_concepts(url):
    response = alchemyapi.concepts('url', url)
    return [concept['text'] for concept in response['concepts']]

def get_read_time(url):
    response = alchemyapi.text('url', url)
    length = len(response['text'])
    #assuming 200 WPM
    return int(length*.3)

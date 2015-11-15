from alchemy_api.alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

def get_concepts(url):
    response = alchemyapi.concepts('url', url)
    return [concept['text'] for concept in response['concepts']]

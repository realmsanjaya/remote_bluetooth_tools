import requests

# Constants
BASE_URL = 'https://cat-fact.herokuapp.com/facts/random'

class CatFact:
    """ This will pull random cat facts """
    def __init__(self, animal_type, amount):
        self.animal_type = animal_type
        self.amount = amount

    def get_facts(self):
        """ This will pull cat facts from the api """
        data = requests.get(BASE_URL)
        result = data.json()
        print(result['text'])

fact1 = CatFact(animal_type='cat', amount=1)
fact1.get_facts()
        
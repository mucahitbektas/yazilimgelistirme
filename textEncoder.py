import json

class Letter_converter:
    def __init__(self, filename='alphabet.json'):
        self.alphabet = self.read_alphabet(filename)
    def read_alphabet(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            db = json.load(f)

        alphabet_dict = db['alphabet']
        return alphabet_dict
        
    def text_encoder(self, word):        
        for c in word:
            if c in self.alphabet:
                word = word.replace(c, self.alphabet[c])

        word = word.upper()
        return word

def resulter(text, result):
    print("-"*50)
    print("TEXT: ", text)
    print("-"*50)
    print("RESULT: ", result)
    print("-"*50)

if "__main__" == __name__:
    obj = Letter_converter()
    text = "y2076u6y9930vx9104uxzz33v09y5w53w47u08w98wy59xy4z491v04360x4401z"
    result = ""

    for i in text:
        result += obj.text_encoder(i)
    
    resulter(text, result)

import numpy as np
import torch
import json
import random
from nltk_utils import bag_of_words, tokenize
from model import NeuralNet

with open('intents_utf8.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

FILE = "data.pth"

data = torch.load(FILE, weights_only=True)


input_size = data['input_size']
hidden_size = data['hidden_size'] 
output_size = data['output_size'] 
all_words = data['all_words'] 
tags = data['tags'] 


model = NeuralNet(input_size, hidden_size, output_size)

model.load_state_dict(data['model_state'])

model.eval()


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model.to(device)


def get_response(msg):
    
    sentence = tokenize(msg)
     
    X = bag_of_words(sentence, all_words)
    
    X = X.reshape(1, X.shape[0])
     
    X = torch.from_numpy(X).to(device)
    
    
    output = model(X)
   
    _, predicted = torch.max(output, dim=1)
    
    
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim=1)
   
    prob = probs[0][predicted.item()]
    
   
    if prob.item() > 0.75:
        
        for intent in intents['intents']:
            if tag == intent["tag"]:
                
                return random.choice(intent['responses'])
    
    return "Não entendi a sua pergunta..."

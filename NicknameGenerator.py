import random
import yaml

with open('C:\\Users\\Gurjot-PC\\Documents\\iNTRO\\adjectives.yml', 'r') as file:
    adjectives = yaml.safe_load(file)

name = input('Enter your name: ')
f_letter_name = name[0].lower()

adj_list = adjectives[f_letter_name]
random_adj = random.choice(adj_list)
print (f'Your new nickname is {random_adj.title()} {name.title()}')


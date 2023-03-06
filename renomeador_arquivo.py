import os

pasta = r'C:\Users\dival\Downloads\pokemon_cries\cries_pokedex'
num_arquivo = 1

for filename in os.listdir(pasta):
    os.rename(pasta + '//' + filename, pasta + '//' + str(num_arquivo) + '.wav')
    num_arquivo += 1

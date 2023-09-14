import json

soma_media_total = 0.0  # soma todas das notas
qtd_alunos = 0  # contador de alunos
nrNotas = 0  # Numero de notas inseridas
dict_nomeNota = {}  # dicionario para incluir nome e notas
vlTotal_Notas = 0.0  # soma das notas
with open("jsonformatter.json", "r") as file:
    jsonData = json.load(file)
# Loop percorre todos os nome de alunos
for name in jsonData:
    arrNotas = name['notas']
    # percorre as notas do aluno que esta no loop
    for sNotas in arrNotas:
        vlTotal_Notas += sNotas
        nrNotas += 1
    dict_nomeNota[name['nome']] = round((
        vlTotal_Notas / nrNotas), 2)  # inseri a media
    soma_media_total += vlTotal_Notas/nrNotas
    nrNotas = 0
    vlTotal_Notas = 0
    qtd_alunos += 1


vl_media_geral = soma_media_total/qtd_alunos
sortedDicByNota = sorted(dict_nomeNota.items(),
                         key=lambda x: x[1],  reverse=True)
converted_dict = dict(sortedDicByNota)

# PRINTS
print('O Aluno mais bem colocado foi: ' + str(list(converted_dict.items())[0]))

for x in range(len(converted_dict)):
    print(str(list(converted_dict.items())[x]))

print('Quantidade de aluno avaliados: ' + str(qtd_alunos))
print('A media e de: ' + str(round(vl_media_geral, 2)))
print('A soma total e : ' + str(round(soma_media_total, 2)))

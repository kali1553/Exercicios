tradução= {

"senhor": "matey",
"hotel": "fleabag inn",
"estudante": "sawbbie",
"garoto": "matey",
"madame": "proud bleggart",
"professor": "fould blaggart",
"restaurante": "galley",
"seu": "yer",
"com licença": "arr",
"estudantes": "swabbies",
"sao": "be",
"advogado": "foul blaggart",
"o": "th",
"banheiro": "head",
"meu": "me",
"oi": "avast",
"é": "be",
"homem": "matey"
}

digite = input("digite a frase: ").split()

igual = ""
existenteigualanao = ''

for y in digite:
    existenteigualanao = True
    
    for i in tradução:
        if y == i:
            igual += tradução[i] + " "
            existenteigualanao = False
    if existenteigualanao:
        igual += y
print(igual)
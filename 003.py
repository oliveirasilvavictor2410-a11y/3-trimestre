# Dicionário com os itens do cardápio e os respectivos preços
cardapio_precos = {
    'pizza': 10,
    'suco': 5,
    'bolo': 7,
    'refrigerante': 8
}

# Transforma as chaves do dicionário em uma lista para usar com o índice do for
itens = list(cardapio_precos.keys())
precos = list(cardapio_precos.values())

print("Itens do cardápio e preços:")
# Usando o for com range(4) conforme o slide para repetir 4 vezes
for i in range(4):
    item_atual = itens[i]
    preco_atual = precos[i]
    print(f"Item: {item_atual} - Preço R${preco_atual}")

# Calcula o valor total do cardápio somando os preços
valor_total = sum(cardapio_precos.values())
print(f"Valor total do cardápio R${valor_total}")

# Pede ao utilizador para escolher o que quer comer
escolha = input("O que você quer comer hoje? ")

# Verifica se a escolha está presente no dicionário do cardápio
if escolha in cardapio_precos:
    print(f"Ótima escolha! Saindo um(a) {escolha} no valor de R${cardapio_precos[escolha]}.")
else:
    print(f"{escolha} não está no cardápio, que tal você pedir {itens}")
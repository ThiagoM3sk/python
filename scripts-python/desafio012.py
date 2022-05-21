preco = float(input('Preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f},  com desconto de 5% agora custa R${:.2f}'.format(preco, desconto))

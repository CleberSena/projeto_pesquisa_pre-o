from codigo_base import*
import datetime

while True:
    cabecalho_do_bot()

    data = format_date()

    driver,wait = inicializacao_do_bot()

    produto = pesquisar_produto(wait)
    
    preco_produto = pesquisar_preco(wait, produto)
    criarPlanilha(produto, data, preco_produto, "https://www.apple.com/br/shop/buy-iphone")

    driver.close() 

    intervalo()

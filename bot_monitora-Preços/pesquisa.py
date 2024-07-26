from codigo_base import*
import datetime

while True:
    inicializacao_do_bot()

    data = datetime.datetime.now()
    data = data.strftime("%d/%m/%Y")

    driver,wait = iniciarDriver()
    driver.get("https://www.apple.com/br/shop/buy-iphone")
    sl(5)

    produto = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH,'//h3[@class="rf-hcard-content-title"]')))
    produto = produto[0].text
    sl(3)
    preco_produto = wait.until(CondicaoExperada.visibility_of_element_located((By.XPATH,'//div//span[text()=" R$ 9.299"]')))
    preco_produto = preco_produto.text.replace('R$','' )
    preco_produto = int(preco_produto.replace('.', ''))
    sl(3)
    criarPlanilha(produto, data, preco_produto, "https://www.apple.com/br/shop/buy-iphone")

    driver.close() 

    intervalo()

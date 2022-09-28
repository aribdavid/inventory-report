from inventory_report.inventory.product import Product


def mock_products():
    return Product(
        id=123,
        nome_do_produto="nome_do_produto",
        nome_da_empresa="nome_da_empresa",
        data_de_fabricacao="data_de_fabricacao",
        data_de_validade="data_de_validade",
        numero_de_serie="numero_de_serie",
        instrucoes_de_armazenamento="instrucoes_de_armazenamento",
    )


def test_relatorio_produto():
    product = mock_products()
    stringRepr = str(product.__repr__)
    text1 = "nome_do_produto"
    text2 = "data_de_validade"
    assert text1 in stringRepr
    assert text2 in stringRepr

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


def test_cria_produto():    
    product = mock_products()
    assert product.id == 123
    assert product.nome_do_produto == 'nome_do_produto'
    assert product.nome_da_empresa == 'nome_da_empresa'
    assert product.data_de_fabricacao == 'data_de_fabricacao'
    assert product.data_de_validade == 'data_de_validade'
    assert product.numero_de_serie == 'numero_de_serie'
    assert product.instrucoes_de_armazenamento == 'instrucoes_de_armazenamento'
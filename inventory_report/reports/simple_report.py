from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        company = [dict_report["nome_da_empresa"] for dict_report in list]
        oldest_date = min(
            [dict_report["data_de_fabricacao"] for dict_report in list]
        )
        next_date = min(
            [
                dict_report["data_de_validade"]
                for dict_report in list
                if date.fromisoformat(dict_report["data_de_validade"])
                >= date.today()
            ]
        )
        count = Counter(company)
        quantity_products = count.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {next_date}\n"
            f"Empresa com mais produtos: {quantity_products}"
        )

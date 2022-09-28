from datetime import date
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        company = [dict_report["nome_da_empresa"] for dict_report in list]
        oldeste_date = min(
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

        str_data = ""

        for company in count.most_common():
            str_data += f"- {company[0]}: {company[1]}\n"

        return (
            f"Data de fabricação mais antiga: {oldeste_date}\n"
            f"Data de validade mais próxima: {next_date}\n"
            f"Empresa com mais produtos: {quantity_products}\n"
            "Produtos estocados por empresa:\n"
            f"{str_data}"
        )

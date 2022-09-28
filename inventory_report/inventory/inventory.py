import csv
import json
import xmltodict


from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def read_file(cls, path: str):
        data = []
        with open(path) as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))
            if path.endswith(".json"):
                return json.load(file)
            if path.endswith(".xml"):
                content = file.read()
                return xmltodict.parse(content)["dataset"]["record"]

        return data

    @classmethod
    def import_data(cls, path: str, result: str):
        data = cls.read_file(path)
        if result == "simples":
            return SimpleReport.generate(data)
        if result == "completo":
            return CompleteReport.generate(data)
        else:
            raise ValueError("error")

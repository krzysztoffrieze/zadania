import json
import re
from _csv import reader


def load_saldo_and_magazyn(file):
    with open(file) as opened_file:
        our_data = json.loads(opened_file.read())
        saldo = our_data.get("saldo")
        magazyn = our_data.get("magazyn")
        return saldo, magazyn

def save_saldo_and_magazyn_to_file(file, saldo, magazyn):
    with open(file, mode="w") as opened_file:
        structure_to_be_saved = {
            "saldo": saldo,
            "magazyn": magazyn
        }
        opened_file.write(json.dumps(structure_to_be_saved))

def load_history(file):
    with open(file) as opened_file:
        our_data = opened_file.read().split(",")
        return our_data



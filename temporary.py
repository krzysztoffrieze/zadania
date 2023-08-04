
file = open("saldo_i_magazyn.txt", mode="w")
file.write('{"saldo": 10000.0, "magazyn": {"rower": {"ilosc": 2, "cena": 100}, "hulajnoga": {"ilosc": 3, "cena": 1500}}}')
file.close()

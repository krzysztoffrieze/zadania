saldo = 1000.0
magazyn = {
    "jablka": {
        "ilość": 5,
        "cena": 10
    },
    "cytryny": {
        "ilość": 8,
        "cena": 10
    },
    "pomarancze": {
        "ilość": 9,
        "cena": 10
    },
    "gruszki": {
        "ilość": 7,
        "cena": 15
    }
}
history = []
initial_message = "Witaj magazynie. Lista dostępnych komend to:\n" \
                  " 1-Saldo  2-Sprzedaż  3-Zakup  4-Konto  5-Lista  6-Magazyn  7-Przegląd  8-Koniec"

end_program = False
while not end_program:
    print(magazyn)
    print(saldo)
    print(initial_message)
    operation = input("Podaj operację, którą chcesz wykonać ")
    if operation == "1":

        amount = float(input("Podaj kwotę, którą chcesz dodać lub odjąć z konta"))
        saldo += amount
        history.append(f"Wykonano instrukcję saldo, zasilono {amount}")
    if operation == "2":

        product = input("Podaj nazwę produktu: ")

        amount = float(input("Podaj ilość, którą chcesz sprzedać: "))
        product_found = False
        # sprawdzmy czy mamy towar
        for item, item_details in magazyn.items():
            if product == item:
                item_details["ilość"] -= amount
                saldo += (item_details["cena"] * amount)
                product_found = True
                history.append(f"Sprzedano {product} w ilości {amount}")
                break
        if not product_found:
            history.append(f"Nie udało się sprzedać towaru {product}, mamy go za mało na magazynie")

    if operation == "3":
        print(magazyn)

        product = input("Podaj nazwę produktu: ")

        amount = float(input("Podaj ilość, którą chcesz nam sprzedać: "))
        product_found = False

        for item, item_details in magazyn.items():
            if product == item:
                item_details["ilość"] -= amount
                saldo -= (item_details["cena"] * amount)
                product_found = True
                history.append(f"Kupiono {product} w ilości {amount}")
                break
        if not product_found:
            history.append(f"Nie udało się nam kupć towaru {product}, nie handlujemy tym towarem")

    if operation == "4":
        print(f"stan konta to: {saldo} \n")
    if operation == "5":
        print(f"stan magazynowy to: {magazyn} \n")
    if operation == "6":
        product = input("Podaj nazwę produktu: ")
        product_found = False
        for item, item_details in magazyn.items():
            if product == item:
                product_found = True
                print(f"stan produktu {product} w magazynie to: {item_details} \n")
                break
        if not product_found:
            print(f"brak w magazynie {product} nie handlujemy tym towarem \n")


    if operation == "7":

        value_from = input("Podaj początkowy zakres")
        value_to = input("Podaj końcowy zakres")
        if not value_to and not value_from:
            print(history)
        if value_from and not value_to:
            print(history[value_from:])

    if operation == "8":
        break
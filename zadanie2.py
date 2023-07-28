parcels_amount = input("Podaj ilosc paczek:")
maximum_weight = 20
kilograms_sent = 0
parcel_weight = 0
stop_program = False
parcels_sent = 1
parcel_number = 1
biggest_gap_in_weight = 0
parcel_with_biggest_gap = None
while not stop_program:
    element = float(input("Podaj wagę elementu"))
    if 10 < element < 1:
        stop_program = True


    else:
        if parcel_weight + element > 20:
            if 20 - parcel_weight > biggest_gap_in_weight:
                biggest_gap_in_weight = 20 - parcel_weight
                parcel_with_biggest_gap = parcel_number
                print(parcel_with_biggest_gap)
                print(f"waga paczki to kg: {parcel_weight}, pustych kg ma: {20 - parcel_weight}")
            if parcel_number == int(parcels_amount):
                stop_program = True
                break
            parcel_weight = 0
            parcel_weight += element
            parcel_number += 1
            parcels_sent += 1
            kilograms_sent += element
        else:
            parcel_weight += element
            kilograms_sent += element

print(f"Wyslano kilogramow: {kilograms_sent}")
print(f"Ilosc wyslanych paczek: {parcels_sent}")
print(f"Paczka z najmniejsza wagą to: {parcel_with_biggest_gap}, ważyła ona {20 - biggest_gap_in_weight}")
print("Zakonczylismy program")
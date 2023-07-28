

inflacja_1	= 1.59282448436825
inflacja_2	= -0.453509101198007
inflacja_3	= 2.32467171712441
inflacja_4	= 1.26125440724877
inflacja_5	= 1.78252628571251
inflacja_6	= 2.32938454145522
inflacja_7	= 1.50222984223283
inflacja_8	= 1.78252628571251
inflacja_9	= 2.32884899407637
inflacja_10	= 0.616921348207244
inflacja_11	= 2.35229588637833
inflacja_12	= 0.337779545187098
inflacja_13	= 1.57703524727525
inflacja_14	= -0.292781442607648
inflacja_15	= 2.48619659017508
inflacja_16	= 0.267110317834564
inflacja_17	= 1.41795267229799
inflacja_18	= 1.05424326726375
inflacja_19	= 1.4805201044812
inflacja_20	= 1.57703524727525
inflacja_21	= -0.0774206903147018
inflacja_22	=1.16573339872354
inflacja_23	= -0.404186717638335
inflacja_24	= 1.49970852083123

oprocentowanie_kredytu = float(input("podaj oprocentowanie kredytu: "))
kwota_poczatkowa_kredytu = float(input("podaj kwote poczatkowa kredytu: "))
stala_wartosc_raty = float(input("podaj stałą wartość raty: "))
formula_do_wyswietlenia ='Twoja pozostała rata kredytu to {kwota_kredytu}, to {roznica_w_racie} mniej niż w poprzednim miesiącu.'
print(f'Oprocentowanie to: {oprocentowanie_kredytu}, kwota początkowa to: {kwota_poczatkowa_kredytu}, stala wartosc raty: {stala_wartosc_raty}')

kwota_po_pierwszej_racie = (1 +((inflacja_1+oprocentowanie_kredytu)/1200)) * kwota_poczatkowa_kredytu - stala_wartosc_raty
kwota_po_drugiej_racie = (1 +((inflacja_2+oprocentowanie_kredytu)/1200)) * kwota_po_pierwszej_racie - stala_wartosc_raty
kwota_po_trzeciej_racie = (1 +((inflacja_3+oprocentowanie_kredytu)/1200)) * kwota_po_drugiej_racie - stala_wartosc_raty
kwota_po_czwartej_racie = (1 +((inflacja_4+oprocentowanie_kredytu)/1200)) * kwota_po_trzeciej_racie - stala_wartosc_raty
kwota_po_piatej_racie = (1 +((inflacja_5+oprocentowanie_kredytu)/1200)) * kwota_po_czwartej_racie - stala_wartosc_raty
kwota_po_szostej_racie = (1 +((inflacja_6+oprocentowanie_kredytu)/1200)) * kwota_po_piatej_racie - stala_wartosc_raty
kwota_po_siodmej_racie = (1 +((inflacja_7+oprocentowanie_kredytu)/1200)) * kwota_po_szostej_racie - stala_wartosc_raty
kwota_po_osmej_racie = (1 +((inflacja_8+oprocentowanie_kredytu)/1200)) * kwota_po_siodmej_racie - stala_wartosc_raty
kwota_po_dziewiatej_racie = (1 +((inflacja_9+oprocentowanie_kredytu)/1200)) * kwota_po_osmej_racie - stala_wartosc_raty
kwota_po_dziesiatej_racie = (1 +((inflacja_10+oprocentowanie_kredytu)/1200)) * kwota_po_dziewiatej_racie - stala_wartosc_raty
kwota_po_jedenastej_racie = (1 +((inflacja_11+oprocentowanie_kredytu)/1200)) * kwota_po_dziesiatej_racie - stala_wartosc_raty
kwota_po_dwunastej_racie = (1 +((inflacja_12+oprocentowanie_kredytu)/1200)) * kwota_po_jedenastej_racie - stala_wartosc_raty
kwota_po_trzynastej_racie = (1 +((inflacja_13+oprocentowanie_kredytu)/1200)) * kwota_po_dwunastej_racie - stala_wartosc_raty
kwota_po_czternastej_racie = (1 +((inflacja_14+oprocentowanie_kredytu)/1200)) * kwota_po_trzynastej_racie - stala_wartosc_raty
kwota_po_pietnastej_racie = (1 +((inflacja_15+oprocentowanie_kredytu)/1200)) * kwota_po_czternastej_racie - stala_wartosc_raty
kwota_po_szesnastej_racie = (1 +((inflacja_16+oprocentowanie_kredytu)/1200)) * kwota_po_pietnastej_racie - stala_wartosc_raty
kwota_po_siedemnnastej_racie = (1 +((inflacja_17+oprocentowanie_kredytu)/1200)) * kwota_po_szesnastej_racie - stala_wartosc_raty
kwota_po_osiemnastej_racie = (1 +((inflacja_18+oprocentowanie_kredytu)/1200)) * kwota_po_siedemnnastej_racie - stala_wartosc_raty
kwota_po_dziewietnastej_racie = (1 +((inflacja_19+oprocentowanie_kredytu)/1200)) * kwota_po_osiemnastej_racie - stala_wartosc_raty
kwota_po_dwudziestej_racie = (1 +((inflacja_20+oprocentowanie_kredytu)/1200)) * kwota_po_dziewietnastej_racie - stala_wartosc_raty
kwota_po_dwudziestejpierwszej_racie = (1 +((inflacja_21+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_racie - stala_wartosc_raty
kwota_po_dwudziestejdrugiej_racie = (1 +((inflacja_22+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestejpierwszej_racie - stala_wartosc_raty
kwota_po_dwudziestejtrzeciej_racie = (1 +((inflacja_23+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestejdrugiej_racie - stala_wartosc_raty
kwota_po_dwudziestejczwartej_racie = (1 +((inflacja_24+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestejtrzeciej_racie - stala_wartosc_raty

print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_pierwszej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_pierwszej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_drugiej_racie, roznica_w_racie = (kwota_po_pierwszej_racie - kwota_po_drugiej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_trzeciej_racie, roznica_w_racie = (kwota_po_drugiej_racie - kwota_po_trzeciej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_czwartej_racie, roznica_w_racie = (kwota_po_trzeciej_racie - kwota_po_czwartej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_piatej_racie, roznica_w_racie = (kwota_po_czwartej_racie - kwota_po_piatej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_szostej_racie, roznica_w_racie = (kwota_po_piatej_racie - kwota_po_szostej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_siodmej_racie, roznica_w_racie = (kwota_po_szostej_racie - kwota_po_siodmej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_osmej_racie, roznica_w_racie = (kwota_po_siodmej_racie - kwota_po_osmej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dziewiatej_racie, roznica_w_racie = (kwota_po_osmej_racie - kwota_po_dziewiatej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dziesiatej_racie, roznica_w_racie = (kwota_po_dziewiatej_racie - kwota_po_dziesiatej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_jedenastej_racie, roznica_w_racie = (kwota_po_dziesiatej_racie - kwota_po_jedenastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwunastej_racie, roznica_w_racie = (kwota_po_jedenastej_racie - kwota_po_dwunastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_trzynastej_racie, roznica_w_racie = (kwota_po_dwunastej_racie - kwota_po_trzynastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_czternastej_racie, roznica_w_racie = (kwota_po_trzynastej_racie - kwota_po_czternastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_pietnastej_racie, roznica_w_racie = (kwota_po_czternastej_racie - kwota_po_pietnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_szesnastej_racie, roznica_w_racie = (kwota_po_pietnastej_racie - kwota_po_szesnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_siedemnnastej_racie, roznica_w_racie = (kwota_po_szesnastej_racie - kwota_po_siedemnnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_osiemnastej_racie, roznica_w_racie = (kwota_po_siedemnnastej_racie - kwota_po_osiemnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dziewietnastej_racie, roznica_w_racie = (kwota_po_osiemnastej_racie - kwota_po_dziewietnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestej_racie, roznica_w_racie = (kwota_po_dziewietnastej_racie - kwota_po_dwudziestej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestejpierwszej_racie, roznica_w_racie = (kwota_po_dwudziestej_racie - kwota_po_dwudziestejpierwszej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestejdrugiej_racie, roznica_w_racie = (kwota_po_dwudziestejpierwszej_racie - kwota_po_dwudziestejdrugiej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestejtrzeciej_racie, roznica_w_racie = (kwota_po_dwudziestejdrugiej_racie - kwota_po_dwudziestejtrzeciej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestejczwartej_racie, roznica_w_racie = (kwota_po_dwudziestejtrzeciej_racie - kwota_po_dwudziestejczwartej_racie)))


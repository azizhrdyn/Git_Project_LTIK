while True:
    try:
        coef = int(input("Masukkan angka: "))
    except ValueError:
        continue
    
    print("---TABEL PERKALIAN---")
    
    for calculate in range (1,11):
        if calculate < 11:
            multiple = calculate*coef
            print(f"{coef} x {calculate} = {multiple}")
            calculate = calculate + 1

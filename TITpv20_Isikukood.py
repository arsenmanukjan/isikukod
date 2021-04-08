while True:
    kod=input()
    pol=kod[0]
    date=kod[1:7] # берется от первой строки до 7-ой строки
    if int(pol)>=1 and int(pol) <=6 and len(kod)==11 and kod.isdigit():  # Проверка состоит ли строка из цифр
        year = int(date[0] + date[1])
        month = int(date[2] + date[3])
        day = int(date[4] + date[5])
        if int(pol) <= 4:
            year += 1900
        else:
            year += 2000
        if month > 12:
            date= "Ошибка"
        elif day > 31:
            date= "Ошибка"
        elif month == 2 and day > 29:
            date= "Ошибка"
        elif month % 2 == 1 and day > 30:
            date= "Ошибка"
        date= f"{day}/{month}/{year}"
        if int(pol) == 1 or int(pol) == 3 or int(pol) == 5:
            pol= "Мужской"
        elif int(pol) == 2 or int(pol) == 4 or int(pol) == 6:
            pol= "Женский"
        else:
            pol= "Неопределенный"
        print(f"Пол: {pol} родился {date}")


    

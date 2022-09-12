def calc_discount(total_price):
    discount = ((total_price / 100) * 10)
    total_price = total_price - discount
    return total_price, discount


def calc_price(age):
    price = 0
    if age > 25:
        price = 1390
    elif 25 >= age >= 18:
        price = 990
    return price


def sell_tickets():
    total_price = 0
    while True:
        try:
            ticket_num = int(input('Сколько билетов вы хотите приобрести на мероприятие? '))
            break
        except ValueError:
            print('Введите целое число')
    for i in range(1, ticket_num + 1):
        while True:
            try:
                age = int(input(f'Для какого возраста билет {i}?'))
                price = calc_price(age)
                if price > 0:
                    print(f'Стоимость билета: {price} руб.')
                    total_price += price
                else:
                    print('Билет бесплатный')
                break
            except ValueError:
                print('Введите целое число')
    if ticket_num > 3:
        total_price, discount = calc_discount(total_price)
        print(f'Сумма к оплате: {total_price} руб. с учетом 10% скидки на полную стоимость заказа за регистрацию больше 5-и человек')
        print(f'Скидка составила: {discount} руб')
    else:
        if total_price > 0:
            print(f'Сумма к оплате: {total_price} руб.')


if __name__ == "__main__":
    sell_tickets()

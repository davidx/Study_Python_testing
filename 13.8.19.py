'''Для онлайн-конференции необходимо написать программу, которая будет подсчитывать
общую стоимость билетов. Программа должна работать следующим образом:
1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением
которого выбирается стоимость:
Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
От 18 до 25 лет — 990 руб.
От 25 лет — полная стоимость 1390 руб.
3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует
больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.'''

# L = list(map(int, input().split()))
#
# print(not any(L))

amount_of_tickets = int(input('Введите желаемое кол-во билетов: '))

print('Введите возраст посетителя для каждого из билетов')

age_of_person = dict(key,value for key in range(amount_of_tickets) )
print(age_of_person)
 # Дан словарь, создать новый словарь при помощи конструкции
# генератор словаря, поменяв местами ключ и значение.


chess_players = {
    "Carlsen, Magnus": 2865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 2792,
    "Nepomniachtchi, Ian": 2773
}

a2 = {int(chess_players[i]): str(i) for i in chess_players}
print(a2)
#                        ИЛИ

a3 = {int(value): str(i) for i, value in chess_players.items()}
print(a3)
#                       ИЛИ

a4 = {int(items[1]): str(items[0]) for items in chess_players.items()}
print(a4)

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data_list = list(poet_data)
poet_data_list[2] = 'Москва'
poet_data = tuple(poet_data_list)
print(poet_data)
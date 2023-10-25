students = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
]

print([i['full_name'] for i in students])
print([i['full_name'] for i in students for j in ([i['full_name'].split()[1]]) if len(j) > 6])



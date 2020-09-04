goods = []
features = {'имя': '', 'цена': '', 'количество': '', 'ед. измерения': ''}
analytics = {'имя': [], 'цена': [], 'количество': [], 'ед. измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', начать заново 'Enter', вывести аналитику 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Функция ввода "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
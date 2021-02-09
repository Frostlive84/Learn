import os



def user():
    use = input('Имя пользователя: ')
    com = 'adduser {0}'.format(use)
    os.system(com)
    com1 = 'passwd {0}'.format(use)
    os.system(com1)
    print('Пользователь создан', use)
    print('Желаете добвить его в групппу?')
    ch = input('Да "Y", Нет "N" ')
    if ch == 'y':
        grr = input('Введите группу: "Wheel" или любую другую ')
        comg = 'usermod -aG {0} {1}'.format(grr, use)
        os.system(comg)
        print('Пользователь {0} успешно создан и входит в группу {1}'.format(use, grr))
    else:
        print('Пользователь {0} успешно создан БЕЗ ГРУППЫ'.format(use))

user()

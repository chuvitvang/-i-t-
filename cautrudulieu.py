loikhai = {
    'A': input('Nhập lời khai của A: '),
    'B': input('Nhập lời khai của B: '),
    'C': input('Nhập lời khai của C: ')
}
#cả 3 người đều im lăng
if all(value == 'slient' for value in loikhai.values()):
    print('A, B, C lãnh án 5 năm.')
#cả 3 người đều tố cáo
elif all(value != 'slient' for value in loikhai.values()):
    print('A, B, C lãnh án 10 năm.')
# Kiểm tra trường hợp có 2 người tố cáo, 1 người giữ im lặng
elif sum(value != 'slient' for value in loikhai.values()) == 2:
    for person, statement in loikhai.items():
        if statement == 'slient':
            print(f'{person} lãnh án 20 năm, các người còn lại lãnh án 10 năm.')
        break
# Kiểm tra trường hợp 1 người tố cáo và 2 người im lặng
elif sum(value != 'tocao' for value in loikhai.values()) == 2:
    for person, statement in loikhai.items():
        if statement == 'tocao':
            print(f'{person} tự do, các người còn lại lãnh án 10 năm.')
        break

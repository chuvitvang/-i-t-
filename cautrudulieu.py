loikhai = {
    'A': input('Nhập lời khai của A: '),
    'B': input('Nhập lời khai của B: '),
    'C': input('Nhập lời khai của C: ')
}
#cả 3 người đều im lăng và 3 người đều tố cáo
if all(value == 'slient' for value in loikhai.values()):
    print('A, B, C lãnh án 5 năm.')
else:
    print('A, B, C lãnh án 10 năm.')

for person, statement in loikhai.items():
    # Kiểm tra trường hợp có 2 người tố cáo, 1 người giữ im lặng
    if sum(value != 'slient' for value in loikhai.values()) == 2 and statement == 'slient':
        print(f'{person} lãnh án 20 năm, các người còn lại lãnh án 10 năm.')
        break
    # Kiểm tra trường hợp 1 người tố cáo và 2 người im lặng
    elif sum(value != 'tocao' for value in loikhai.values()) == 2 and statement == 'tocao':
        print(f'{person} tự do, các người còn lại lãnh án 10 năm.')
        break

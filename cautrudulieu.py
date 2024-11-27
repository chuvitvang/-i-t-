loikhai = {
    'A': input('Nhập lời khai của A: ').strip().lower(),
    'B': input('Nhập lời khai của B: ').strip().lower(),
    'C': input('Nhập lời khai của C: ').strip().lower()
}

# Kiểm tra trường hợp tất cả giữ im lặng
if all(value == 'slient' for value in loikhai.values()):
    print('A, B, C lãnh án 5 năm.')
# Kiểm tra trường hợp cả 3 không giữ im lặng
elif all(value != 'slient' for value in loikhai.values()):
    print('A, B, C lãnh án 10 năm.')
# Kiểm tra trường hợp có 2 người không giữ im lặng, 1 người giữ im lặng
elif sum(value != 'slient' for value in loikhai.values()) == 2:
    for person, statement in loikhai.items():
        if statement == 'slient':
            print(f'{person} lãnh án 20 năm, các người còn lại lãnh án 10 năm.')
            break
# Kiểm tra trường hợp 2 người cùng tố cáo 1 người
else:
    cases = {
        ('tocaoC', 'tocaoC'): ('A, B', 'C'),
        ('tocaoA', 'tocaoA'): ('B, C', 'A'),
        ('tocaoB', 'tocaoB'): ('A, C', 'B')
    }
    for (key1, key2), (accusers, accused) in cases.items():
        if list(loikhai.values()) == [key1, key1, 'slient']:
            print(f'{accusers} lãnh án 10 năm, {accused} lãnh án 20 năm.')
            break
    else:
        # Trường hợp tố cáo đơn lẻ
        for person, statement in loikhai.items():
            if statement.startswith('tocao'):
                accused = statement[-1].upper()
                print(f'{person} tự do, {accused} và người còn lại lãnh án 10 năm.')
                break

# Nhập lời khai từ người dùng và lưu vào dictionary
loikhai = {nguoi: input(f'Nhập lời khai của {nguoi} (imlang/tocao): ') for nguoi in ['A', 'B', 'C']}

# Kiểm tra các trường hợp
if all(statement == 'imlang' for statement in loikhai.values()):
    # Cả 3 người đều im lặng
    print('A, B, C lãnh án 5 năm.')
else:
    # Đếm số người tố cáo và im lặng
    so_tocao = sum(statement == 'tocao' for statement in loikhai.values())
    so_imlang = len(loikhai) - so_tocao

    for nguoi, statement in loikhai.items():
        if so_tocao == 2 and statement == 'imlang':
            # Có 2 người tố cáo, xét người im lặng
            print(f'{nguoi} lãnh án 20 năm, các người còn lại lãnh án 10 năm.')
            break
        elif so_imlang == 2 and statement == 'tocao':
            # Có 2 người im lặng, xét người tố cáo
            print(f'{nguoi} tự do, các người còn lại lãnh án 10 năm.')
            break
    else:
        # Trường hợp không khớp với các điều kiện trên
        print('A, B, C lãnh án 10 năm.')

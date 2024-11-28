#tạo 1 dictionary với các key A,B,C
loikhai = {
    'A': input('Nhập lời khai của A: '),
    'B': input('Nhập lời khai của B: '),
    'C': input('Nhập lời khai của C: ')
}
#cả 3 người đều im lăng và 3 người đều tố cáo
if all(value == 'imlang' for value in loikhai.values()): #hàm all() chọn tất cả các values(giá trị)
    print('A, B, C lãnh án 5 năm.')
else:
    print('A, B, C lãnh án 10 năm.')

for nguoi, statement in loikhai.items():# hàm items() lấy cả key và giá trị
    # Đếm số người tố cáo và im lặng
    so_tocao = sum(value == 'tocao' for value in loikhai.values())
    so_imlang = len(loikhai) - so_tocao
    if so_tocao == 2 and statement == 'imlang':#đk tổng số người tố cáo =2 ,chỉ xét người im lặng là statement
        print(f'{nguoi} lãnh án 20 năm, các người còn lại lãnh án 10 năm.')
        break
    elif so_imlang == 2 and statement == 'tocao':#đk tổng số người im lặng =2 ,chỉ xét người tố cáo là statement
        print(f'{nguoi} tự do, các người còn lại lãnh án 10 năm.')
        break

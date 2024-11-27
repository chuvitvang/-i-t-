loikhai_A = input('Nhập lời khai của A: ')
loikhai_B = input('Nhập lời khai của B: ')
loikhai_C = input('Nhập lời khai của C: ')

#cả 3 người đều im lặng
if loikhai_A == loikhai_B == loikhai_C == 'slient':
    print('A, B, C lãnh án 5 năm.')
#cả 3 người đều tố cáo
elif loikhai_A == loikhai_B == loikhai_C != 'slient':
    print('A, B, C lãnh án 10 năm.')
# Kiểm tra trường hợp có 2 người tố cáo, 1 người giữ im lặng
#3 truong hop:
#a b to cao c im
#a c to cao b im
#b c to cao a im
elif loikhai_A == loikhai_B =='tocao':
    print('C lãnh án 20 năm , A B lãnh án 10 năm')
elif loikhai_A == loikhai_C =='tocao':
    print('B lãnh án 20 năm , A C lãnh án 10 năm')
elif loikhai_B == loikhai_C =='tocao':
    print('A lãnh án 20 năm , B C lãnh án 10 năm')
# Kiểm tra trường hợp có 1 người tố cáo, 2 người giữ im lặng
#3 truong hop:
#a b im c to cao
#a c im b to cao
#b c im a to cao
elif loikhai_A == loikhai_B =='slient':
    print('C tự do , A B lãnh án 10 năm')
elif loikhai_A == loikhai_C =='slient':
    print('B tự do , A C lãnh án 10 năm')
elif loikhai_B == loikhai_C =='slient':
    print('A tự do , B C lãnh án 10 năm')


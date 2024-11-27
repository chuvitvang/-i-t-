loikhai_A = input('Nhập lời khai của A: ')
loikhai_B = input('Nhập lời khai của B: ')
loikhai_C = input('Nhập lời khai của C: ')

if loikhai_A == loikhai_B == loikhai_C == 'slient':
    print('A, B, C lãnh án 5 năm.')
elif loikhai_A == 'tocaoC' and loikhai_B == 'tocaoC':
    print('A, B lãnh án 10 năm, C lãnh án 20 năm.')
elif loikhai_B == 'tocaoA' and loikhai_C == 'tocaoA':
    print('B, C lãnh án 10 năm, A lãnh án 20 năm.')
elif loikhai_A == 'tocaoB' and loikhai_C == 'tocaoB':
    print('A, C lãnh án 10 năm, B lãnh án 20 năm.')
elif loikhai_A == 'slient' and loikhai_B != 'slient' and loikhai_C != 'slient':
    print('B, C lãnh án 10 năm, A lãnh án 20 năm.')
elif loikhai_B == 'slient' and loikhai_A != 'slient' and loikhai_C != 'slient':
    print('A, C lãnh án 10 năm, B lãnh án 20 năm.')
elif loikhai_C == 'slient' and loikhai_A != 'slient' and loikhai_B != 'slient':
    print('A, B lãnh án 10 năm, C lãnh án 20 năm.')
elif loikhai_A == 'tocaoC':
    print('A tự do, B và C lãnh án 10 năm.')
elif loikhai_B == 'tocaoC':
    print('B tự do, A và C lãnh án 10 năm.')
elif loikhai_B == 'tocaoA':
    print('B tự do, A và C lãnh án 10 năm.')
elif loikhai_C == 'tocaoA':
    print('C tự do, A và B lãnh án 10 năm.')
elif loikhai_A == 'tocaoB':
    print('A tự do, B và C lãnh án 10 năm.')
elif loikhai_C == 'tocaoB':
    print('C tự do, A và B lãnh án 10 năm.')
else:
    print('A, B, C lãnh án 10 năm.')

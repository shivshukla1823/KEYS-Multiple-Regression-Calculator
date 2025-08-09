def DALYs():
    hmod = float(-49.74)
    rmod = float(-89.90)
    pmod = float(-35.31)
    while True:
        try:
            nh = int(input('Number of Graduates as Physicians: '))
            break
        except ValueError:
            print('Invalid input. Please enter a number')
    while True:
        try:
            nr = int(input('Number of Graduates as Researchers: '))
            break
        except ValueError:
            print('Invalid input. Please enter a number')
    while True:
        try:
            np = int(input('Number of Graduates as Drug Developers: '))
            break
        except ValueError:
            print('Invalid input. Please enter a number')
    daly_h = float(hmod*nh)
    daly_r = float(rmod*nr)
    daly_p = float(pmod*np)
    daly = daly_h + daly_r + daly_p
    print(f'Estimated DALYs Avoided from Physicians: {daly_h:.2f}')
    print(f'Estimated DALYs Avoided from Researchers: {daly_r:.2f}')
    print(f'Estimated DALYs Avoided from Drug Developers: {daly_p:.2f}')
    print(f'Estimated Total DALYs Avoided: {daly:.2f}')
DALYs()

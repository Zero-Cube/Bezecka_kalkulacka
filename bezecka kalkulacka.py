import math


km_h = float(input("Zadaj rýchlosť v km/h: "))
m_s = km_h / 3.6
print(f'{m_s:.2f} m/s ')
minuta_meter = m_s * 60
print(f'{minuta_meter:.2f} metrov za minutu')
cooper = minuta_meter * 12
print(f'{cooper:.2f} metrov za 12 minút')

tempo = 60 / km_h
print(f'Tempo = {tempo:.2f} min/km')


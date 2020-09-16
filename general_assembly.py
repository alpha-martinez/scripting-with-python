squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Yoel',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]

ga_file = open('general_assembly.text', 'w')

for i in range(len(squad_713)):
    p = squad_713[i]
    if i == 0:
        ga_file.write(f'{p}')
    else:
        ga_file.write(f'\n{p}')

print(ga_file)

ga_file.close()
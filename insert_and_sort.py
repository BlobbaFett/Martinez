a = ['Master', 'Online']
a.insert(1, 'code')
print(a)

d = ['1','2','3']
c = ['4','5','6']
c.insert(0, 'd')
print(c)

#Sort as A-Z
company = ['Jualia', 'Erick', 'Dillion']
company.sort()
print(company)

#Sort as Z-A
company2 = ['Aguado', 'Manfred', 'Juanito', 'Pepe botellas']
company2.sort(reverse=True)
print(company2)

#Sort as length
company3 = ['Aguado', 'Manfred Salas Gomez', 'Juanito Perez', 'Pepe botellas']
company3.sort(reverse=True, key=len)
print(company3)
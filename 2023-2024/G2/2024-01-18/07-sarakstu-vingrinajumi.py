bakterijas = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(bakterijas[0])
print(bakterijas[5])
print(bakterijas[-1])
print(bakterijas[0:3])
print(bakterijas[2:5])
print(bakterijas[4:6])

tiksanas = ['9:00', '10:30', '14:00', '15:00', '15:30']
tiksanas.append('16:30')
tiksanas.append('18:30')
tiksanas.extend(['19:00', '20:00'])
print(tiksanas)
print(tiksanas[2:9])

pilsetas = ['Jelgava', 'Ķegums', 'Lubāna', 'Mazsalaca', 'Sabile', 'Ainaži', 'Baloži', 'Cesvaine', 'Dobele', 'Gulbene']
pilsetas.append('Iecava')
pilsetas.insert(2, 'Vecpiebalga')
print(pilsetas)
pilsetas.remove('Iecava')
pilsetas.pop()
pilsetas.sort()
print(pilsetas)

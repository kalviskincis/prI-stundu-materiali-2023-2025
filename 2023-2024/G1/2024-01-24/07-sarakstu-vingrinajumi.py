bakterijas = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(bakterijas[0])
print(bakterijas[-1])
print(bakterijas[0:3])
print(bakterijas[2:5])
print(bakterijas[4:6])

for viena in bakterijas:
    print(viena)
    if viena == "Bacteria":
        print("Īpaši bīstama! Veicina aizgulēšanos.")

tiksanas =  ['9:00', '10:30', '14:00', '15:00', '15:30']
tiksanas.append('16:30')
tiksanas.append('18:30')
tiksanas.extend(['19:00', '20:00'])

pilsetas = ['Jelgava', 'Ķekava', 'Lubāna', 'Mazsalaca', 'Sabile', 'Ainaži', 'Baloži', 'Cesvaine', 'Dobele', 'Gulbene']
pilsetas.append('Iecava')
pilsetas.insert(2, 'Vecpiebalga')
pilsetas.sort()
print(pilsetas)
pilsetas.remove('Iecava')
pilsetas.pop()


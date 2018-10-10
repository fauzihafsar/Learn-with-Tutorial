"""
sequences
list [] - Tuples() - dictionary{} -sets
"""

data = {1:{'nama' : "Haru",'umur' : '21','hobby' : 'nga-nime'},
        2:{'nama' : "Aki",'umur' : '31','hobby' : 'nge-manga'}}

#untuk mencetak semua datang
#print(data)

#jika ingin mencetak hanya data ke-2
#print(data[2])

#untuk mencetak hanya data tertentu saja pada key dan value yang dipilih
#print(data[2]['hobby'])

#penggunaan loop pada dictionary
for key, value, in data.items():
    print("key-nya: ", key)

    for key2 in value:
        print(key2 + ":", value[key2])

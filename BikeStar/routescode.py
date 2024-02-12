import folium
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


cursor.execute("SELECT coordinates FROM routes")
rows = cursor.fetchall()

i = 0
coordinates= []
for row in rows:
    if i == 0:
        print(str(row))
        coords=(''.join((''.join((']a['.join(str(row).split("], ["))).split("('"))).split("',)"))).split("a")
        #coordinates.append(list(map(float, ''.join(''.join(str(row).split("('")).split("',)")).split(', '))))
        for coord in coords:
            #print(coord[1:-1].split(', '))
            coordinates.append(list(map(float, str(coord)[1:-1].split(', '))))
        i+=1



m = folium.Map(location=coordinates[len(coordinates)//2], zoom_start=14)


folium.Marker(coordinates[0]).add_to(m)
folium.Marker(coordinates[-1]).add_to(m)


folium.PolyLine(locations=coordinates, color='blue').add_to(m)

conn.close()
m.save('static/new_bicycle_route.html')
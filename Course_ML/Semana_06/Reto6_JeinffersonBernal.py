import folium

# Coordenadas de Medellín, Colombia
medellin_coords = [6.2442, -75.5812]

# Crear un mapa centrado en Medellín
map_medellin = folium.Map(location=medellin_coords, zoom_start=13)

# Añadir un marcador en una ubicación específica
folium.Marker(medellin_coords, popup="Medellín, Colombia").add_to(map_medellin)

# Guardar el mapa como archivo HTML
map_medellin.save("mapa_medellin.html")
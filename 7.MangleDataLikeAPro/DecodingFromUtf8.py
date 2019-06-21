place = 'caf\u00e9'
print(place)
type(place)

place_bytes = place.encode('utf-8')
print(place_bytes)
type(place_bytes)

decoded_place = place_bytes.decode('utf-8')
print(decoded_place)
type(decoded_place)

wrongly_decoded_place = place_bytes.decode('ascii')

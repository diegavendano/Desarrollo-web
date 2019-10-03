def es_vocal(letra):
  return letra.lower() in ['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú','Á','É','Í','Ó','Ú']

letra = input('Introduce una letra por favor: ')
if es_vocal(letra):
  print(True)
else:
  print(False)   
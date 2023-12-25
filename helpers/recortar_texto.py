def recortar_texto(texto, longitud_maxima):

  if len(texto) <= longitud_maxima:
    return texto

  return texto[:longitud_maxima]

def morse():
    global palabra

    while len(palabra) != 0:
        if len(palabra) > 0:
            cuatro = palabra[:4]
            tres = palabra[:3]
            dos = palabra[:2]
            uno = palabra[:1]
            if cuatro in inverso_codigo_morse:
                caracter4 =  inverso_codigo_morse[cuatro]
                conversion.append(caracter4)
                palabra = palabra[4:]
            elif tres in inverso_codigo_morse:
                caracter3 = inverso_codigo_morse[tres]
                conversion.append(caracter3)
                palabra = palabra[3:]
            elif dos in inverso_codigo_morse:
                caracter2 = inverso_codigo_morse[dos]
                conversion.append(caracter2)
                palabra = palabra[2:]
            elif uno in inverso_codigo_morse:
                caracter1 = inverso_codigo_morse[uno]
                conversion.append(caracter1)
                palabra = palabra[1:]

codigo_morse = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.', 
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',   ' ': '/'
}

inverso_codigo_morse = {v: k for k, v in codigo_morse.items()}


palabra = input("Ingrese la palabra o código que desea convertir: ").upper()


conversion= []
if palabra[0] == "." or palabra[0] == "-":
    if " " in palabra :
        palabras = palabra.split(' / ')
        for palabra in palabras:
            letras = palabra.split(' ')
        for letra in letras:
            if letra in inverso_codigo_morse:
                conversion.append(inverso_codigo_morse[letra])

        conversion_final = ''.join(conversion)
        print(f"Palabra de {palabra}: {conversion_final}")
    else:
        morse()
        conversion_final = ''.join(conversion)
        print(f"Palabra de {palabra}: {conversion_final}")
else:
    letra = 0
    while letra != len(palabra):
        l = palabra[letra]
        conversion.append(codigo_morse[l])
        letra += 1

    conversion_final = ' '.join(conversion)
    print(f"Código morse de {palabra}: {conversion_final}")
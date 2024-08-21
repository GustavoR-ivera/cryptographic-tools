def cifrar(texto_claro, desplazamiento, abecedario):
    texto_cifrado = ""
    for caracter in texto_claro:
        indice = (abecedario.index(caracter.lower()) + desplazamiento) % len(abecedario)
        texto_cifrado += abecedario[indice].upper()
    return texto_cifrado

def descifrar(texto_cifrado, desplazamiento, abecedario):
    texto_claro = ""
    for caracter in texto_cifrado:
        indice = (abecedario.index(caracter.lower()) - desplazamiento) % len(abecedario)
        texto_claro += abecedario[indice]
    return texto_claro

def main():
    #conjunto de simbolos del alfabeto
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    #texto a cifrar
    texto = "nesoacademy"
    desplazamiento = 3
    print(cifrar(texto, desplazamiento, abecedario))
    cifrado = "QHVRDFDGHPB"
    print(descifrar(cifrado, desplazamiento, abecedario))


main()
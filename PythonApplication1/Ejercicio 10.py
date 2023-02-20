
#INVIRTIENDO CADENAS

# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def reverse(text):
    text_len = len(text)
    reverse_text = ""
    for i in range(0, text_len):
        reverse_text += text[text_len - i - 1]
    return reverse_text

print(reverse("Hello World"))

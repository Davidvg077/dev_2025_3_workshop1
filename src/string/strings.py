class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        """
        texto = "".join(c.lower() for c in texto if c.isalnum())
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        """
        invertida = ""
        for c in texto:
            invertida = c + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        """
        vocales = "aeiouáéíóú"
        return sum(1 for c in texto.lower() if c in vocales)
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        """
        vocales = "aeiouáéíóú"
        return sum(1 for c in texto.lower() if c.isalpha() and c not in vocales)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        """
        t1 = sorted(c.lower() for c in texto1 if c.isalnum())
        t2 = sorted(c.lower() for c in texto2 if c.isalnum())
        return t1 == t2
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        return len([p for p in texto.split(" ") if p.strip() != ""])
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        """
        words = texto.split()
        result = texto
        for word in words:
            capitalized = word.capitalize()
            result = result.replace(word, capitalized)
        return result
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        """
        has_leading_space = texto.startswith(' ')
        has_trailing_space = texto.endswith(' ')
        cleaned = " ".join(texto.split())
        if has_leading_space:
            cleaned = ' ' + cleaned
        if has_trailing_space:
            cleaned = cleaned + ' '
        return cleaned
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
    
        """
        if texto.startswith("-"):
            return texto[1:].isdigit()
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        """
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado

    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
    
        """
        if not subcadena:  
            return []
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
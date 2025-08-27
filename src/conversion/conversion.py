class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        
        return (fahrenheit - 32) * 5 / 9
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.   
        """
        return metros * 3.28084
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.   
        """
        return pies * 0.3048
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.  
        """
        return bin(decimal)[2:]
    
    def binario_a_decimal(self, binario):
        """
       Convierte un número binario a decimal.
        """
        return int(binario, 2)
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        romano = ""
        i = 0
        while numero > 0:
            for _ in range(numero // val[i]):
                romano += syms[i]
                numero -= val[i]
            i += 1
        return romano
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        pass
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass
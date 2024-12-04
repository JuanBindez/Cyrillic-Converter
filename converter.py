class CyrillicConverter:
    """Mapping for Latin characters to visually identical Cyrillic characters"""
    def __init__(self):
        self.mapping = {
            'A': 'А', 'B': 'В', 'E': 'Е', 'K': 'К', 'M': 'М',
            'H': 'Н', 'O': 'О', 'P': 'Р', 'C': 'С', 'T': 'Т',
            'Y': 'У', 'X': 'Х', 'a': 'а', 'b': 'в', 'e': 'е',
            'k': 'к', 'm': 'м', 'h': 'н', 'o': 'о', 'p': 'р',
            'c': 'с', 't': 'т', 'y': 'у', 'x': 'х'
        }

    def convert_to_cyrillic(self, text):
        """
        Convert a text with Latin characters to visually identical Cyrillic characters.
        """
        return ''.join(self.mapping.get(char, char) for char in text)

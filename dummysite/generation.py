import random


alphabet = "abcdefghijklmnopqrstuvwxyz"


class Generator:
    def __init__(self, seed):
        self.__seed = seed

    def generate_string(self, length):
        return ''.join(random.choice(alphabet) for _ in range(length))

    def generate_text(self, length):
        return ''.join(random.choice(alphabet + "  ") for _ in range(length))

    def generate(self, f, n):
        return [ f() for _ in range(n) ]

    def generate_id(self):
        return self.generate_string(10)

    def generate_link(self):
        id = self.generate_id()
        text = self.generate_text(10)
        return f'<a href="/{id}">{text}</a>'

    def generate_paragraph(self):
        strings = self.generate(lambda: self.generate_text(100), 10)
        strings2 = self.generate(lambda: self.generate_text(100), 10)
        links = self.generate(self.generate_link, 10)
        content = " ".join( f'{string} {link} {string2}' for string, link, string2 in zip(strings, links, strings2) )
        return f'<p>{content}</p>'

    def generate_page(self, id):
        paragraphs = "\n".join(self.generate(self.generate_paragraph, 100))
        random.seed(hash(id) + self.__seed)
        return f'''
        <html><body>{paragraphs}</body></html>
        '''
import os

os.system("cls||clear")

class Livro:
    def __init__(self, titilo: str, autor: str, numero_paginas: int, preco: float) -> None:
        self.titulo = titilo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"\nTitulo: {self.titulo} \nAutor: {self.autor} \nNumero de paginas: {self.numero_paginas} \nPreco: {self.preco}"
    
primeiro_livro = Livro("A seleção", "Kiera Cass", 363, 39.72)
segundo_livro = Livro("Verity", "Collen Hoover", 320, 43.70)

print(primeiro_livro.exibir_dados())
print(segundo_livro.exibir_dados())
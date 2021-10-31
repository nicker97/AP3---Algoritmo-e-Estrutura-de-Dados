class Fila:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def inserir(self, item):
        if fila.size() < 5:
            self.items.append(item)
            print()
            print(f"\033[32mO número {numero} foi INSERIDO a Fila com sucesso!\033[m")
            print()
        else:
            print()
            print("\033[31mERRO! A Fila está CHEIA\033[m")
            print("\033[31mNenhum número foi INSERIDO!\033[m")
            print()

    def excluir(self):
        if self.size() == 0:
            print()
            print("\033[31mErro! A Fila está vazia! Não há o que remover!\033[m")
            print()
        else:
            print()
            print(f"\033[32mO numero {fila.items[0]} foi RETIRADO da fila!\033[m")
            print()
            return self.items.pop(0)


fila = Fila()

print("=" * 33)
print("\033[34m AP3 - Fila de 5 Números Inteiros\033[m")
print("=" * 33)
while True:
    print("\033[32m1\033[m - INSERIR Número")
    print("\033[32m2\033[m - REMOVER Número")
    print("\033[32m3\033[m - EXIBIR Fila")
    print("\033[32m4\033[m - MOSTRAR Pares ")
    print("\033[32m5\033[m - ESVAZIAR Fila")
    print("\033[32m6\033[m - SAIR")

    print("=" * 33)
    try:
        resposta = int(input("\033[34mSua Opção:\033[m "))
        print("=" * 33)
    except:
        print()
        print("\033[31mERRO! Escolha uma opção VÁLIDA!\033[m")
        print()
    else:

        if resposta == 1:
            if fila.size()<5:
                try:
                    numero = int(input("\033[34mDigite um Número Inteiro: \033[m"))
                except:
                    print()
                    print("\033[31mERRO! Digite um Valor INTEIRO!\033[m")
                    print()
                else:
                    if numero > 0:
                        fila.inserir(numero)
                    else:
                        print()
                        print("\033[31mERRO! O número deve ser maior que ZERO!\033[m")
                        print("\033[31mNenhum número foi INSERIDO!\033[m")
                        print()
            else:
                print()
                print("\033[31mA FILA está CHEIA!\033[m")
                print()

        if resposta == 2:
            fila.excluir()

        if resposta == 3:
            if fila.size() == 0:
                print()
                print("\033[31mA Fila ESTÁ VAZIA!\033[m")
                print()

            elif 0 < fila.size() < 5:
                print()
                print("\033[32mFila:\033[m", fila.items)
                print()

            else:
                print()
                print("\033[32mFila: \033[m", fila.items)
                print("\033[31mA FILA está CHEIA!\033[m")
                print()

        if resposta == 4:
            if fila.size() == 0:
                print()
                print("\033[31mA Fila ESTÁ VAZIA!\033[m")
                print()
            else:
                lista = []
                for c in range(0, fila.size()):
                    if fila.items[c] % 2 == 0:
                        lista.append(fila.items[c])
                if len(lista) != 0:
                    print()
                    print("\033[32mPares da FILA:\033[m", lista)
                    print()
                else:
                    print()
                    print("\033[31mA Fila não POSSUI pares!\033[m")
                    print()

        if resposta == 5:
            if fila.size() == 0:
                print()
                print("\033[31mA Fila já ESTÁ VAZIA!\033[m")
                print()
            else:
                while fila.size() > 0:
                    fila.excluir()
                print()
                print("\033[32mA Fila foi esvaziada com sucesso!\033[m")
                print()

        if resposta == 6:
            print("\033[32mSaindo...\033[m")
            break

        if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4 or resposta == 5:
            continue
        print()
        print("\033[31mERRO! DIGITE UMA OPÇÃO VÁLIDA!\033[m")
        print()
        print("=" * 33)

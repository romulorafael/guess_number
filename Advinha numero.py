"""
this program is a game that will guess a number that the user is thinking
is a class and try/except exercise
"""

class Jogo(object):
    def __init__(self):
        self.__cartoes = ('''
        1   3   5   7   9   11  13  15
        17  19  21  23  25  27  29  31
        33  35  37  39  41  43  45  47
        49  51  53  55  57  59  61  63
        ''','''
        2   3   6   7   10  11  14  15
        18  19  22  23  26  27  30  31
        34  35  38  39  42  43  46  47
        50  51  54  55  58  59  62  63
        ''','''
        4   5   6   7   12  13  14  15
        20  21  22  23  28  29  30  31
        36  37  38  39  44  45  46  47
        52  53  54  55  60  61  62  63
        ''','''
        8   9   10  11  12  13  14  15
        24  25  26  27  28  29  30  31
        40  41  42  43  44  45  46  47
        56  57  58  59  60  61  62  63
        ''','''
        16  17  18  19  20  21  22  23
        24  25  26  27  28  29  30  31
        48  49  50  51  52  53  54  55
        56  57  58  59  60  61  62  63
        ''','''
        32  33  34  35  36  37  38  39
        40  41  42  43  44  45  46  47
        48  49  50  51  52  53  54  55
        56  57  58  59  60  61  62  63
        ''')
        self.__card = 0
        self.__num = 0
        self.main()


    #Quick game explanation
    def apresentação(self):       

        print("""You need to choose a number between 0 and 63
the program will show you 5 cards
And you will answer if the number is in the card
At the end the program will say your number""")


    #Return True or False if the user responds yes or not   
    def recebeEntradaDoUsuário(self):
        while True:
            res = input('Is the number in this list?(yes/not): ').lower()
            try:
                if res == "yes":
                    return True
                elif res == "not":
                    return False
                raise RespostaError

            except RespostaError:
                print(RespostaError())

    #prints the number
    def imprimeNumeroSecreto(self):
        print('the chosen number is:', self.__num)


    #Print the cards to the user
    def mostraCartão(self):
        
        print(self.__cartoes[self.__card])
    

    #Add the valor to numb
    def adicionaNumero(self, esta):

        if esta:
            self.__num += int(self.__cartoes[self.__card].split()[0])


    def main(self):
        
        self.apresentação()

        for i in range(len(self.__cartoes)):
            self.__card = i
            self.mostraCartão()
            self.adicionaNumero(self.recebeEntradaDoUsuário())
            print(self.__num)

        self.imprimeNumeroSecreto()

class RespostaError(Exception):
    def __str__(self):
        return "Resposta errada, resonda sim ou não"


if __name__ == '__main__':
    x = Jogo()

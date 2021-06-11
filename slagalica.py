class Polje(object):
    def __init__(self,broj=0):
        self.__broj=broj
        

    def vratiBroj(self):
        return self.__broj

    @property
    def jeBroj(self):
        if self.__broj !=0:
            return True
        else:
            return False
    @property
    def jePrazno(self):
        if self.__broj==0:
            return True
        else:
            return False

    def __str__(self):
        if self.__broj==0:
            return ''
        else:
            return '%d' % self.__broj

    def __repr__(self):
        return 'Polje(%d)' %self.__broj
        

print('**test 1**')
brojevi=list(range(9))
for broj in brojevi:
    p=Polje(broj)
    print(p.vratiBroj(), p.jeBroj, p.jePrazno)

print('**test2**')
polja=[Polje(broj) for broj in range(9)]

for p in polja:
    print (str(p), repr(p))

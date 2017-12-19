class CHELOVEK:
    def __init__ (self, prozvishe, rankrabstva ):
        self.__prozvishe=prozvishe
        self.__rank_rankrabstva= rank_rabstva
    def display(self):
        print("Name:", self.__name, "\tAge:", self.__age)
class LUDYA(CHELOVEK):
    def rank_rabstva(self, rankrabstva):
        print("RANK_RABSTVA:",rankrabstva)
    def prozvishe(self, prozvishe):
        print("PROZVISHE", prozvishe)
Sultan=CHELOVEK("Sultan")
t=LUDYA("Sultan", "25 rankrabstva")
t.rank_rabstva("100")
t.prozvishe("debil")


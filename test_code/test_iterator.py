class MyIterator:
    def __init__(self):
        self.i = 1
        print(f"Je m'initialise à {self.i}")

    def __iter__(self):
        print("On appelle __iter__")
        return self

    def __next__(self):
        print("On a appele __next__")
        self.i *= 2
        if self.i > 3000:
            print("Fin d'iteration")
            raise StopIteration()
        return self.i


# _________________fonction generatrice ----------------------------
def my_generator(start=0, end=0):
    cnt = start
    while cnt <= end:
        if cnt % 2 == 0:
            print(f"   on s'arrete au yield {cnt}")
            yield float(cnt)
            print(f"  On reprend apres le yield {cnt}")
        else:
            print(f"  On s'arrete au yield str")
            yield str(cnt)
            print(f"  On reprend apres le yield str")
        cnt += 1
    yield "C'est bientot la fin"
    yield "C'est VRAIMENT bientot la fin"
    yield "C'est la fin !!!"


# -----------------affiche l'iterator -----------------------------
debut = 0
for i in MyIterator():
    debut = i
    print(i)
# -----------------afficher la fct generator ---------------------------
print(my_generator())
v = 4
# for j in my_generator(4, 8):
for j in my_generator(v, 8):
    v += 1
    print(f"valeur de l'iteration de genrator() : {j}")


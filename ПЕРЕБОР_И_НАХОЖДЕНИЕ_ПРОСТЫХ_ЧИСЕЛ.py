def prostoe(chislo):
    for delitel in (2, int(chislo ** 0.5) + 1):
        if chislo % delitel == 0:
            return False
    return True
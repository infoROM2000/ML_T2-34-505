
import numpy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def entropie(partitii):
    suma = 0
    for x in partitii:
        suma += x
    entropia = 0
    for x in partitii:
        if(x!=0): #daca x e 0, atunci termenul va fi nul altfel da eroare log2(0)
            entropia -= x / suma * numpy.log2(x / suma)
    return entropia


def entropie_conditionala(partitii):
    suma = 0
    for x in partitii:
        for y in x:
            suma += y
    valori_totale = []
    entropia = 0
    a = 0
    while a < len(partitii):
        x = partitii[a]
        s = 0
        for i in x:
            s += i
        valori_totale.append(s)
        a += 1
    a = 0
    while a < len(partitii):
        entropia += valori_totale[a] / suma * entropie(partitii[a])
        a += 1
    return entropia


def problema_34(m=2, n=2, *partitii):
    a = 0;
    valori_totale = []
    while a < len(partitii[0]):
        s = 0
        coloana = [item[a] for item in partitii]
        for x in coloana:
            s += x
        valori_totale.append(s)
        a += 1

    entropii_conditionale_specifice = []
    a = 0
    while a < len(partitii):
        entropii_conditionale_specifice.append(entropie(partitii[a]))
        a += 1
    print("\nEntropia all:")
    entropia_atributului = entropie(valori_totale)  # a
    print(entropia_atributului)
    print("\nEntropii specifice:")
    for x in entropii_conditionale_specifice:  # b
        print(x)
    print("\nEntropia medie:")
    entropia_conditionala = entropie_conditionala(partitii)  # c
    print(entropia_conditionala)
    print("\nCastig de informatie:")
    information_gain = entropia_atributului - entropia_conditionala
    print(information_gain)  # d


problema_34(2, 2, [3, 2], [2, 2])
print("\n\n\n")
problema_34(2, 2, [5, 1], [0, 3])

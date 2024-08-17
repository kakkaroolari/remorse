
def tehtava25():
    print(tehtava25.__name__)
    numero = 2009
    print("saara on syntynyt:", numero)

def tehtava26():
    print(tehtava26.__name__)
    syntymavuosi = 2009
    tamavuosi = 2023
    ika = tamavuosi - syntymavuosi
    print("taytat tana vuonna:", ika)

def tehtavaXX():
    print(tehtavaXX.__name__)
    for i in range(1,5):
        print("iteraatio:", i)
    

if __name__ == "__main__":
    tehtava25()
    tehtava26()
    tehtavaXX()
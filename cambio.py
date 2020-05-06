
def dar_cambio_monedas(cambio: int) -> str:
    """
        Function that return a quantity of coins
        :param cambio: The quantity of change to donner
    """
    cambio_restante = cambio
    monedas_de_500 = str(( cambio_restante - cambio_restante % 500) // 500)
    cambio_restante = cambio_restante % 500
    monedas_de_200 = str(( cambio_restante - cambio_restante % 200) // 200)
    cambio_restante = cambio_restante % 200
    monedas_de_100 = str(( cambio_restante - cambio_restante % 100) // 100)
    cambio_restante = cambio_restante % 100
    monedas_de_50 = str(( cambio_restante - cambio_restante % 50 ) // 50)

    return "" + monedas_de_500 + "," + monedas_de_200 + "," + monedas_de_100 + "," + monedas_de_50

print(dar_cambio_monedas(1850))

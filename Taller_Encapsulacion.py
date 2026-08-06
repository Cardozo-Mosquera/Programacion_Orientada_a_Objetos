class CuentaBancaria:

    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    
    @property
    def titular(self):
        return self._titular

    
    @property
    def saldo(self):
        return self._saldo

    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        else:
            self._saldo = nuevo_saldo


    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo = self._saldo + cantidad
            return True
        else:
            return False


    def retirar(self, cantidad):
        if cantidad > self._saldo:
            return False

        if cantidad <= 0:
            return False

        self._saldo = self._saldo - cantidad
        return True



def main():

    cuenta = CuentaBancaria("Juan", 500)

    print("Titular:", cuenta.titular)
    print("Saldo:", cuenta.saldo)

    print("\nDepositar 100")
    if cuenta.depositar(100):
        print("Depósito realizado.")
    else:
        print("No se pudo realizar el depósito.")

    print("Saldo:", cuenta.saldo)

    print("\nRetirar 200")
    if cuenta.retirar(200):
        print("Retiro realizado.")
    else:
        print("No se pudo realizar el retiro.")

    print("Saldo:", cuenta.saldo)

    print("\nIntentar retirar 1000")
    if cuenta.retirar(1000):
        print("Retiro realizado.")
    else:
        print("No hay suficiente dinero.")

    print("Saldo:", cuenta.saldo)

    print("\nIntentar colocar saldo negativo")
    try:
        cuenta.saldo = -50
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
"""
Módulo principal de la aplicación bancaria.
Permite interactuar con la cuenta a través de un menú.
"""
import sys
from cuenta_banco import CuentaBanco


def mostrar_menu():
    """Imprime las opciones del menú en pantalla."""
    print("\n--- BIENVENIDO A TU BANCO ---")
    print("1. Realizar Depósito")
    print("2. Realizar Retiro")
    print("3. Realizar Transferencia")
    print("4. Consultar Saldo")
    print("5. Salir")


def main():
    """Función principal que ejecuta el flujo del programa."""
    mi_cuenta = CuentaBanco("Ronaldo Gonzales", 0.0)
    cuenta_destino = CuentaBanco("Cuenta Amigo", 0.0)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                monto = float(input("Ingrese monto a depositar: "))
                mi_cuenta.deposito_cuenta(monto)
                print(f"✅ Depósito exitoso. Nuevo saldo: {mi_cuenta.saldo_cuenta()}")

            elif opcion == '2':
                monto = float(input("Ingrese monto a retirar: "))
                mi_cuenta.retiro_cuenta(monto)
                print(f"✅ Retiro exitoso. Nuevo saldo: {mi_cuenta.saldo_cuenta()}")

            elif opcion == '3':
                monto = float(input("Ingrese monto a transferir: "))
                mi_cuenta.transferencia_cuenta(monto, cuenta_destino)
                print(f"✅ Transferencia enviada a {cuenta_destino.titular}.")
                print(f"Nuevo saldo: {mi_cuenta.saldo_cuenta()}")

            elif opcion == '4':
                print(f"💰 Su saldo actual es: {mi_cuenta.saldo_cuenta()}")

            elif opcion == '5':
                print("¡Gracias por usar nuestro banco! Hasta luego.")
                sys.exit()

            else:
                print("⚠️ Opción no válida. Por favor ingrese un número del 1 al 5.")

        except ValueError as err:
            print(f"❌ ERROR: {err}")
        except TypeError as err:
            print(f"❌ ERROR DE TIPO: {err}")


if __name__ == "__main__":
    main()

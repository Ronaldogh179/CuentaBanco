"""
Módulo que define la clase CuentaBanco.
Maneja operaciones básicas bancarias.
"""

class CuentaBanco:
    """Representa una cuenta bancaria con operaciones básicas."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Inicializa la cuenta bancaria.

        Args:
            titular (str): Nombre del dueño de la cuenta.
            saldo_inicial (float): Saldo inicial de la cuenta.
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        """
        Realiza un depósito en la cuenta.

        Args:
            monto (float): Cantidad a depositar.

        Raises:
            ValueError: Si el monto es negativo o cero.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto

    def retiro_cuenta(self, monto: float):
        """
        Realiza un retiro de la cuenta.

        Args:
            monto (float): Cantidad a retirar.

        Raises:
            ValueError: Si el monto es negativo, cero o mayor al saldo.
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= monto

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        """Pendiente de implementación."""

    def saldo_cuenta(self) -> float:
        """Pendiente de implementación."""

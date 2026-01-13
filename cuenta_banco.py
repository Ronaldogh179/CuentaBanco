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
        """Pendiente de implementación."""

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        """Pendiente de implementación."""

    def saldo_cuenta(self) -> float:
        """Pendiente de implementación."""

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._historico = Historico()
        self._agencia = "0001" 
        self._numero = numero

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero 
        
    @property
    def historico(self):
        return self._historico

    @property 
    def cliente(self):
        return self.cliente
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class Conta_Corrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saque=3):
        super().__init__(cliente, numero)
    


class Cliente:
    pass

class Pessoa_Fisica(Cliente):
    pass

class Historico:
    pass
from FactorRiesgo import FactorRiesgo
from Problema import Problema


class ProfesionalSalud:
    def __init__(self, identifiacionFactor: int):
        self._identificacionProfesionalSalud = identifiacionFactor

    @property
    def identificacionProfesionalSalud(self):
        return self._identificacionProfesionalSalud

    @identificacionProfesionalSalud.setter
    def identificacionProfesionalSalud(self, value):
        self._identificacionProfesionalSalud = value

    def encargarProblema(self, problema: Problema):
        problema.identificacionProfesionalSalud = self._identificacionProfesionalSalud

    def encargarFactorRiesgo(self, factorRiesgo: FactorRiesgo):
        factorRiesgo.identificacionProfesionalSalud = self._identificacionProfesionalSalud

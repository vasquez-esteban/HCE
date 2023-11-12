from FactorRiesgo import FactorRiesgo
from Problema import Problema


class Paciente:
    def __init__(
        self,
        identificacionPaciente: int,
        historiaPrevia: int,
    ):
        self.identificacionPaciente = identificacionPaciente
        self.historiaPrevia = historiaPrevia

    def asociarProblema(self, problema: Problema):
        problema.identificacionPaciente = self.identificacionPaciente

    def asociarFactorRiesgo(self, factorRiesgo: FactorRiesgo):
        factorRiesgo.identificacionPaciente = self.identificacionPaciente

    def __str__(self):
        return (f"Identificación del Paciente: {self.identificacionPaciente}"
                f"Historia Previa:"
                f"{self.historiaPrevia}")

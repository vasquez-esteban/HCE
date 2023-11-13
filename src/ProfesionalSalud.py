from src.FactorRiesgo import FactorRiesgo
from src.Problema import Problema


class ProfesionalSalud:
    def __init__(self, identifiacionFactor: int):
        """
        Clase que representa a un profesional de la salud en el sistema.

        Args:
            identifiacionFactor (int): Identificador único del profesional de la salud.
        """
        self._identificacionProfesionalSalud = identifiacionFactor

    # Inicio de métodos get y set
    @property
    def identificacionProfesionalSalud(self):
        return self._identificacionProfesionalSalud

    @identificacionProfesionalSalud.setter
    def identificacionProfesionalSalud(self, value):
        self._identificacionProfesionalSalud = value

    def encargarProblema(self, problema: Problema):
        """
        Asigna la responsabilidad de un problema de salud a este profesional de la salud.

        Args:
            problema (Problema): Instancia del problema de salud a ser asignado.
        """
        problema.identificacionProfesionalSalud = self._identificacionProfesionalSalud

    def encargarFactorRiesgo(self, factorRiesgo: FactorRiesgo):
        """
        Asigna la responsabilidad de un factor de riesgo de salud a este profesional de la salud.

        Args:
            factorRiesgo (FactorRiesgo): Instancia del factor de riesgo a ser asignado.
        """
        factorRiesgo.identificacionProfesionalSalud = (
            self._identificacionProfesionalSalud
        )

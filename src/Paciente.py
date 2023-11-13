from src.FactorRiesgo import FactorRiesgo
from src.Problema import Problema


class Paciente:
    def __init__(
        self,
        identificacionPaciente: int,
        historiaPrevia: int,
    ):
        """
        Clase que representa a un paciente en el Historial Clínico Electrónico.

        Args:
            identificacionPaciente (int): Identificación única del paciente.
            historiaPrevia (int): Historia previa del paciente en el sistema.
        """
        self.identificacionPaciente = identificacionPaciente
        self.historiaPrevia = historiaPrevia

    def asociarProblema(self, problema: Problema):
        """
        Asocia un problema de salud al paciente.

        Args:
            problema (Problema): Instancia del problema de salud a asociar.
        """
        problema.identificacionPaciente = self.identificacionPaciente

    def asociarFactorRiesgo(self, factorRiesgo: FactorRiesgo):
        """
        Asocia un factor de riesgo de salud al paciente.

        Args:
            factorRiesgo (FactorRiesgo): Instancia del factor de riesgo a asociar.
        """
        factorRiesgo.identificacionPaciente = self.identificacionPaciente

    def __str__(self):
        """
        Representación de cadena del objeto Paciente.
        """
        return (
            f"Identificación del Paciente: {self.identificacionPaciente}\n"
            f"Historia Previa:\n"
            f"{self.historiaPrevia}"
        )

from HistoriaFactorRiesgo import HistoriaFactorRiesgo
from Tipo import Tipo


class FactorRiesgo:
    def __init__(
            self,
            identificacionFactorRiesgo: int,
            identificacionPaciente: int,
            identificacionProfesionalSalud: int,
            nombre: str,
            estatus: str,
            tipo: Tipo,
            motivoCierre: str,
            historia: HistoriaFactorRiesgo,
            notas: list[str],
    ):
        self.identificacionFactorRiesgo = identificacionFactorRiesgo
        self._identificacionPaciente = identificacionPaciente
        self._identificacionProfesionalSalud = identificacionProfesionalSalud
        self._nombre = nombre
        self.estatus = estatus
        self._tipo = tipo
        self._motivoCierre = motivoCierre
        self._historia = historia
        self._notas = notas

    @property
    def identificacionPaciente(self):
        return self._identificacionPaciente

    @identificacionPaciente.setter
    def identificacionPaciente(self, value):
        self._identificacionPaciente = value

    @property
    def identificacionProfesionalSalud(self):
        return self._identificacionProfesionalSalud

    @identificacionProfesionalSalud.setter
    def identificacionProfesionalSalud(self, value):
        self._identificacionProfesionalSalud = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def motivoCierre(self):
        return self._motivoCierre

    @motivoCierre.setter
    def motivoCierre(self, value):
        self._motivoCierre = value

    @property
    def historia(self):
        return self._historia

    @historia.setter
    def historia(self, value):
        self._historia = value

    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, value):
        self._notas = value

    def agregarNota(self, nota: str):
        self.notas.append(nota)
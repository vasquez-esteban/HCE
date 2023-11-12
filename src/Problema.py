from HistoriaProblema import HistoriaProblema
from Tipo import Tipo


class Problema:
    def __init__(
        self,
        identificacionProblema: int,
        identificacionPaciente: int,
        identificacionProfesionalSalud: int,
        nombre: str,
        estatus: str,
        tipo: Tipo,
        motivoCierre: str,
        historia: HistoriaProblema,
        notas: list[str],
    ):
        """
        Clase que representa un problema de salud asociado a un paciente.

        Args:
            identificacionProblema (int): Identificador único del problema de salud.
            identificacionPaciente (int): Identificador del paciente con el problema.
            identificacionProfesionalSalud (int): id del Profesional que gestiona el problema.
            nombre (str): Nombre o descripción del problema de salud.
            estatus (str): Estado del problema de salud (Activo, Cerrado).
            tipo (Tipo): Representa el tipo/categoría del problema de salud.
            motivoCierre (str): Razón de cierre del problema de salud (si aplica).
            historia (HistoriaProblema): Representa datos históricos asociados.
            notas (lista de str): Una lista de notas adicionales del problema de salud.
        """
        self.identificacionProblema = identificacionProblema
        self._identificacionPaciente = identificacionPaciente
        self._identificacionProfesionalSalud = identificacionProfesionalSalud
        self._nombre = nombre
        self.estatus = estatus
        self._tipo = tipo
        self._motivoCierre = motivoCierre
        self._historia = historia
        self._notas = notas

    # Inicio de métodos get y set
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
        """Método para agregar una nota a la lista de notas del problema"""
        self.notas.append(nota)

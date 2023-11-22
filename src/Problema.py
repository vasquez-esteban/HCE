from pydantic import BaseModel, Field
import data.modelos


class Problema(BaseModel):
    """
    Clase que representa un problema de salud asociado a un paciente.

    Args:
        identificacionPaciente (int): Identificador del paciente con el problema.
        identificacionProfesionalSalud (int): id del Profesional que gestiona el problema.
        nombre (str): Nombre o descripción del problema de salud.
        estatus (str): Estado del problema de salud (Activo, Cerrado).
        tipo (str): Representa el tipo/categoría del problema de salud.
        motivoCierre (str): Razón de cierre del problema de salud (si aplica).
        historia (str): Representa datos históricos asociados.
        notas (str): Una lista de notas adicionales del problema de salud.
    """

    identificacionPaciente: int = Field(gt=-1)
    identificacionProfesionalSalud: int = Field(gt=-1)
    nombre: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    tipo: str = Field(min_length=1)
    motivoCierre: str = Field(min_length=1)
    notas: str = Field(min_length=1)

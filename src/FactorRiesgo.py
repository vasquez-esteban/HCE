from pydantic import BaseModel, Field


class FactorRiesgo(BaseModel):
    """
    Clase que representa un factor de riesgo asociado a la salud de un paciente.

    Args:
        identificacionPaciente (int): Identificador del paciente asociado.
        identificacionProfesionalSalud (int): Id del profesional que gestiona el factor.
        nombre (str): Nombre o descripción del factor de riesgo.
        estatus (str): Estado del factor de riesgo (Activo, Cerrado).
        tipo (str): Representa el tipo/categoría del factor de riesgo.
        motivoCierre (str): Razón de cierre del factor de riesgo (si aplica).
        historia (str): Representa la evolución del factor.
        notas (str): Una lista de notas adicionales del factor de riesgo.
    """

    identificacionPaciente: int = Field(gt=-1)
    identificacionProfesionalSalud: int = Field(gt=-1)
    nombre: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    tipo: str = Field(min_length=1)
    motivoCierre: str = Field(min_length=1)
    notas: str = Field(min_length=1)

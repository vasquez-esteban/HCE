from pydantic import BaseModel, Field
import data.modelos


class Paciente(BaseModel):
    """
    Clase que representa a un paciente en el Historial Clínico Electrónico.

    Args:
        historiaPrevia (int): Historia previa del paciente en el sistema.
    """

    historiaPrevia: str = Field(min_length=1)

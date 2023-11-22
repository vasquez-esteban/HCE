from pydantic import BaseModel, Field
import data.modelos


class ProfesionalSalud(BaseModel):
    """
    Clase que representa a un profesional de la salud en el sistema.

    Args:
        identifiacionProfesionalSalud (int): Identificador único del profesional de la salud.
    """

    identificacionProfesionalSalud: int = Field(gt=-1)

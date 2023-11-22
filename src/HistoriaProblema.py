from pydantic import BaseModel, Field
import data.modelos


class HistoriaProblema(BaseModel):
    """
    Clase que representa la historia asociada a un problema de salud.

    Args:
        identificacionProblema (int): Identificador del problema de salud asociado.
        fecha (str): Fecha de la historia del problema de salud.
        estatus (str): Estado del problema de salud en esta fecha.
        observacion (str): Observación relacionada con el problema de salud.
    """

    identificacionProblema: int = Field(gt=-1)
    fecha: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    observacion: str = Field(min_length=1)

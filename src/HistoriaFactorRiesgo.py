from pydantic import BaseModel, Field
import data.modelos


class HistoriaFactorRiesgo(BaseModel):
    """
    Clase que representa la historia asociada a un factor de riesgo de la salud.

    Args:
        identificacionFactorRiesgo (int): Identificador del factor de riesgo asociado.
        fecha (str): Fecha de la historia del factor de riesgo.
        estatus (str): Estado del factor de riesgo en esta fecha.
        observacion (str): Observación relacionada el factor de riesgo en esta fecha.
    """

    identificacionFactorRiesgo: int = Field(gt=-1)
    fecha: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    observacion: str = Field(min_length=1)

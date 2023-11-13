from pydantic import BaseModel, Field
import data.modelos


class HistoriaFactorRiesgo(BaseModel):
    identificacionFactorRiesgo: int = Field(gt=-1)
    fecha: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    observacion: str = Field(min_length=1)

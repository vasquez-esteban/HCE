from pydantic import BaseModel, Field
import data.modelos


class HistoriaProblema(BaseModel):
    identificacionHistoriaProblema: int = Field(gt=-1)
    identificacionProblema: int = Field(gt=-1)
    fecha: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    observacion: str = Field(min_length=1)

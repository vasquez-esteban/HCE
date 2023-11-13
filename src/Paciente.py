from pydantic import BaseModel, Field
import data.modelos


class Paciente(BaseModel):
    identificacionPaciente: int = Field(gt=-1)
    historiaPrevia: str = Field(min_length=1)

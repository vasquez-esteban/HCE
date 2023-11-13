from pydantic import BaseModel, Field
import data.modelos


class Paciente(BaseModel):
    historiaPrevia: str = Field(min_length=1)

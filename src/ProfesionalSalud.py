from pydantic import BaseModel, Field
import data.modelos


class ProfesionalSalud(BaseModel):
    identificacionProfesionalSalud: int = Field(gt=-1)

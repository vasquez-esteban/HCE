from pydantic import BaseModel, Field


class FactorRiesgo(BaseModel):
    identificacionPaciente: int = Field(gt=-1)
    identificacionProfesionalSalud: int = Field(gt=-1)
    nombre: str = Field(min_length=1)
    estatus: str = Field(min_length=1)
    tipo: str = Field(min_length=1)
    motivoCierre: str = Field(min_length=1)
    notas: str = Field(min_length=1)

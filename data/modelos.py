from sqlalchemy import Column, Integer, String, ForeignKey, Text
from data.database import Base


# Crear modelos de clases para la conexión con SQLite
class FactorRiesgo(Base):
    __tablename__ = 'Factor Riesgo'

    identificacionFactorRiesgo = Column(Integer, primary_key=True, autoincrement=True)
    identificacionPaciente = Column(Integer, ForeignKey('Paciente.identificacionPaciente'), nullable=False)
    identificacionProfesionalSalud = Column(Integer, ForeignKey('ProfesionalSalud.identificacionProfesionalSalud'),
                                            nullable=False)
    nombre = Column(String, nullable=False)
    estatus = Column(String)
    tipo = Column(String)
    motivoCierre = Column(String)
    notas = Column(String)


class HistoriaFactor(Base):
    __tablename__ = 'Historia Factor'

    identificacionHistoriaFactor = Column(Integer, primary_key=True, autoincrement=True)
    identificacionFactorRiesgo = Column(Integer, ForeignKey('FactorRiesgo.identificacionFactorRiesgo'), nullable=False)
    fecha = Column(String, nullable=False)
    estatus = Column(String)
    observacion = Column(Text)


class HistoriaProblema(Base):
    __tablename__ = 'Historia Problema'

    identificacionHistoriaProblema = Column(Integer, primary_key=True, autoincrement=True)
    identificacionProblema = Column(Integer, ForeignKey('Problema.identificacionProblema'), nullable=False)
    fecha = Column(String, nullable=False)
    estatus = Column(String)
    observacion = Column(Text)


class Paciente(Base):
    __tablename__ = 'Paciente'

    identificacionPaciente = Column(Integer, primary_key=True, autoincrement=True)
    historiaPrevia = Column(String, nullable=False)


class Problema(Base):
    __tablename__ = 'Problema'

    identificacionProblema = Column(Integer, primary_key=True, autoincrement=True)
    identificacionPaciente = Column(Integer, ForeignKey('Paciente.identificacionPaciente'), nullable=False)
    identificacionProfesionalSalud = Column(Integer, ForeignKey('ProfesionalSalud.identificacionProfesionalSalud'),
                                            nullable=False)
    nombre = Column(String, nullable=False)
    estatus = Column(String)
    tipo = Column(String)
    motivoCierre = Column(String)
    notas = Column(Text)


class ProfesionalSalud(Base):
    __tablename__ = 'ProfesionalSalud'

    identificacionProfesionalSalud = Column(Integer, primary_key=True, autoincrement=True)

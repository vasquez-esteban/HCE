from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class FactorRiesgo(Base):
    __tablename__ = 'FactorRiesgo'

    identificacionFactorRiesgo = Column(Integer, primary_key=True, autoincrement=True)
    identificacionPaciente = Column(Integer, ForeignKey('Paciente.identificacionPaciente'), nullable=False)
    identificacionProfesionalSalud = Column(Integer, ForeignKey('ProfesionalSalud.identificacionProfesionalSalud'),
                                            nullable=False)
    nombre = Column(String, nullable=False)
    estatus = Column(String)
    tipo = Column(String)
    motivoCierre = Column(String)
    notas = Column(String)

    # Definición de las relaciones con las tablas Paciente y ProfesionalSalud
    paciente = relationship('Paciente', back_populates='factores_riesgo')
    profesional_salud = relationship('ProfesionalSalud', back_populates='factores_riesgo')


class HistoriaFactor(Base):
    __tablename__ = 'HistoriaFactor'

    identificacionHistoriaFactor = Column(Integer, primary_key=True, autoincrement=True)
    identificacionFactorRiesgo = Column(Integer, ForeignKey('FactorRiesgo.identificacionFactorRiesgo'), nullable=False)
    fecha = Column(String, nullable=False)
    estatus = Column(String)
    observacion = Column(Text)

    # Definición de la relación con la tabla FactorRiesgo
    factor_riesgo = relationship('FactorRiesgo', back_populates='historias_factor')


class HistoriaProblema(Base):
    __tablename__ = 'HistoriaProblema'

    identificacionHistoriaProblema = Column(Integer, primary_key=True, autoincrement=True)
    identificacionProblema = Column(Integer, ForeignKey('Problema.identificacionProblema'), nullable=False)
    fecha = Column(String, nullable=False)
    estatus = Column(String)
    observacion = Column(Text)

    # Definición de la relación con la tabla Problema
    problema = relationship('Problema', back_populates='historias_problema')


class Paciente(Base):
    __tablename__ = 'Paciente'

    identificacionPaciente = Column(Integer, primary_key=True, autoincrement=True)
    historiaPrevia = Column(String, nullable=False)

    # Definición de la relación con la tabla FactorRiesgo
    factores_riesgo = relationship('FactorRiesgo', back_populates='paciente')
    # Definición de la relación con la tabla HistoriaProblema
    historias_problema = relationship('HistoriaProblema', back_populates='problema')


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

    # Definición de la relación con la tabla Paciente
    paciente = relationship('Paciente', back_populates='problemas')
    # Definición de la relación con la tabla ProfesionalSalud
    profesional_salud = relationship('ProfesionalSalud', back_populates='problemas')


class ProfesionalSalud(Base):
    __tablename__ = 'ProfesionalSalud'

    identificacionProfesionalSalud = Column(Integer, primary_key=True, autoincrement=True)

    # Definición de la relación con la tabla FactorRiesgo
    factores_riesgo = relationship('FactorRiesgo', back_populates='profesional_salud')
    # Definición de la relación con la tabla Problema
    problemas = relationship('Problema', back_populates='profesional_salud')

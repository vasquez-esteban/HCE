from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from data.database import engine, SessionLocal
import data.modelos as modelos
from src.FactorRiesgo import FactorRiesgo
from src.HistoriaFactorRiesgo import HistoriaFactorRiesgo
from src.HistoriaProblema import HistoriaProblema
from src.Paciente import Paciente
from src.Problema import Problema
from src.ProfesionalSalud import ProfesionalSalud

app = FastAPI()

modelos.Base.metadata.create_all(bind=engine)


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/leer_factores")
def leer_factores(db: Session = Depends(get_db)):
    return db.query(modelos.FactorRiesgo).all()


@app.post("/crear_factor")
def crear_factor(factorRiesgo: FactorRiesgo, db: Session = Depends(get_db)):
    modelo_factor = modelos.FactorRiesgo()

    modelo_factor.identificacionPaciente = factorRiesgo.identificacionPaciente
    modelo_factor.identificacionProfesionalSalud = factorRiesgo.identificacionProfesionalSalud
    modelo_factor.nombre = factorRiesgo.nombre
    modelo_factor.estatus = factorRiesgo.estatus
    modelo_factor.tipo = factorRiesgo.tipo
    modelo_factor.motivoCierre = factorRiesgo.motivoCierre
    modelo_factor.notas = factorRiesgo.notas

    db.add(modelo_factor)
    db.commit()

    return factorRiesgo


@app.get("/leer_historias_factores")
def leer_historias_factores(db: Session = Depends(get_db)):
    return db.query(modelos.HistoriaFactor).all()


@app.post("/crear_historia_factor")
def crear_historia_factor(historia: HistoriaFactorRiesgo, db: Session = Depends(get_db)):
    modelo_historia = modelos.HistoriaFactor()

    modelo_historia.identificacionFactorRiesgo = historia.identificacionFactorRiesgo
    modelo_historia.fecha = historia.fecha
    modelo_historia.estatus = historia.estatus
    modelo_historia.observacion = historia.observacion

    db.add(modelo_historia)
    db.commit()

    return historia


@app.get("/leer_historias_problemas")
def leer_historias_problemas(db: Session = Depends(get_db)):
    return db.query(modelos.HistoriaProblema).all()


@app.post("/crear_historia_problema")
def crear_historia_problema(historia: HistoriaProblema, db: Session = Depends(get_db)):
    modelo_historia = modelos.HistoriaProblema()

    modelo_historia.identificacionProblema = historia.identificacionProblema
    modelo_historia.fecha = historia.fecha
    modelo_historia.estatus = historia.estatus
    modelo_historia.observacion = historia.observacion

    db.add(modelo_historia)
    db.commit()

    return historia


@app.get("/leer_pacientes")
def leer_pacientes(db: Session = Depends(get_db)):
    return db.query(modelos.Paciente).all()


@app.post("/crear_paciente")
def crear_paciente(paciente: Paciente, db: Session = Depends(get_db)):
    modelo_paciente = modelos.Paciente()
    modelo_paciente.historiaPrevia = paciente.historiaPrevia
    db.add(modelo_paciente)
    db.commit()

    return paciente


@app.get("/leer_problemas")
def leer_problemas(db: Session = Depends(get_db)):
    return db.query(modelos.Problema).all()


@app.post("/crear_problema")
def crear_problema(problema: Problema, db: Session = Depends(get_db)):
    modelo_problema = modelos.Problema()

    modelo_problema.identificacionPaciente = problema.identificacionPaciente
    modelo_problema.identificacionProfesionalSalud = problema.identificacionProfesionalSalud
    modelo_problema.nombre = problema.nombre
    modelo_problema.estatus = problema.estatus
    modelo_problema.tipo = problema.tipo
    modelo_problema.motivoCierre = problema.motivoCierre
    modelo_problema.notas = problema.notas

    db.add(modelo_problema)
    db.commit()

    return problema


@app.get("/leer_profesionales_salud")
def leer_profesionales_salud(db: Session = Depends(get_db)):
    return db.query(modelos.ProfesionalSalud).all()


@app.post("/crear_profesional_salud")
def crear_profesional_salud(profesionalSalud: ProfesionalSalud, db: Session = Depends(get_db)):
    db.add(profesionalSalud)
    db.commit()

    return profesionalSalud

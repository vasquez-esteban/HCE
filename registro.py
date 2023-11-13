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


FACTORESRIESGO = []
HISTORIASFACTORES = []
HISTORIASPROBLEMAS = []
PACIENTES = []
PROBLEMAS = []
PROFESIONALESSALUD = []


@app.get("/leer_factores")
def leer_factores(db: Session = Depends(get_db)):
    return db.query(modelos.FactorRiesgo).all()


@app.post("/crear_factor")
def crear_factor(factorRiesgo: FactorRiesgo):
    FACTORESRIESGO.append(factorRiesgo)


@app.get("/leer_historias_factores")
def leer_historias_factores(db: Session = Depends(get_db)):
    return db.query(modelos.HistoriaFactor).all()


@app.post("/crear_historia_factor")
def crear_historia_factor(historia: HistoriaFactorRiesgo):
    HISTORIASFACTORES.append(historia)


@app.get("/leer_historias_problemas")
def leer_historias_problemas(db: Session = Depends(get_db)):
    return db.query(modelos.HistoriaProblema).all()


@app.post("/crear_historia_problema")
def crear_historia_problema(historia: HistoriaProblema):
    HISTORIASPROBLEMAS.append(historia)


@app.get("/leer_pacientes")
def leer_pacientes(db: Session = Depends(get_db)):
    return db.query(modelos.Paciente).all()


@app.post("/crear_paciente")
def crear_paciente(paciente: Paciente):
    PACIENTES.append(paciente)


@app.get("/leer_problemas")
def leer_problemas(db: Session = Depends(get_db)):
    return db.query(modelos.Problema).all()


@app.post("/crear_problema")
def crear_problema(problema: Problema):
    PROBLEMAS.append(problema)


@app.get("/leer_profesionales_salud")
def leer_profesionales_salud(db: Session = Depends(get_db)):
    return db.query(modelos.ProfesionalSalud).all()


@app.post("/crear_profesional_salud")
def crear_profesional_salud(profesionalSalud: ProfesionalSalud):
    PROFESIONALESSALUD.append(profesionalSalud)

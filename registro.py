from fastapi import FastAPI
from src.FactorRiesgo import FactorRiesgo
from src.HistoriaFactorRiesgo import HistoriaFactorRiesgo
from src.HistoriaProblema import HistoriaProblema
from src.Paciente import Paciente
from src.Problema import Problema
from src.ProfesionalSalud import ProfesionalSalud

app = FastAPI()


class API:
    def __init__(self):
        self.FACTORESRIESGO = []
        self.HISTORIASFACTORES = []
        self.HISTORIASPROBLEMAS = []
        self.PACIENTES = []
        self.PROBLEMAS = []
        self.PROFESIONALESSALUD = []

    @app.get("/leer_factores")
    def leerFactores(self):
        return self.FACTORESRIESGO

    @app.post("/crear_factor")
    def crearFactor(self, factorRiesgo: FactorRiesgo):
        self.FACTORESRIESGO.append(factorRiesgo)

    @app.get("/leer_historias_factores")
    def leerHistoriasFactores(self):
        return self.HISTORIASFACTORES

    @app.post("/crear_historia_factor")
    def crearHistoriaFactor(self, historia: HistoriaFactorRiesgo):
        self.HISTORIASFACTORES.append(historia)

    @app.get("/leer_historias_problemas")
    def leerHistoriasProblemas(self):
        return self.HISTORIASPROBLEMAS

    @app.post("/crear_historia_problema")
    def crearHistoriaProblema(self, historia: HistoriaProblema):
        self.HISTORIASPROBLEMAS.append(historia)

    @app.get("/leer_pacientes")
    def leerPacientes(self):
        return self.PACIENTES

    @app.post("/crear_paciente")
    def crearPaciente(self, paciente: Paciente):
        self.PACIENTES.append(paciente)

    @app.get("/leer_problemas")
    def leerProblemas(self):
        return self.PROBLEMAS

    @app.post("/crear_problema")
    def crearProblema(self, problema: Problema):
        self.PROBLEMAS.append(problema)

    @app.get("/leer_profesionales_salud")
    def leerProfesionalesSalud(self):
        return self.PROFESIONALESSALUD

    @app.post("/crear_profesional_salud")
    def crearProfesionalSalud(self, profesionalSalud: ProfesionalSalud):
        self.PROFESIONALESSALUD.append(profesionalSalud)


api = API()

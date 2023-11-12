class HistoriaFactorRiesgo:
    def __init__(
        self,
        identificacionHistoriaFactor: int,
        identificacionFactorRiesgo: int,
        fecha: str,
        estatus: str,
        observacion: str,
    ):
        self.identificacionHistoriaProblema = identificacionHistoriaFactor
        self._identificacion = identificacionFactorRiesgo
        self.fecha = fecha
        self.estatus = estatus
        self._observacion = observacion

    @property
    def identificacionFactorRiesgo(self):
        return self._identificacion

    @identificacionFactorRiesgo.setter
    def identificacionFactorRiesgo(self, value):
        self._identificacion = value

    @property
    def observacion(self):
        return self._observacion

    @observacion.setter
    def observacion(self, value):
        self._observacion = value

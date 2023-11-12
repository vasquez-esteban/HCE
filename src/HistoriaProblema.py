class HistoriaProblema:
    def __init__(
        self,
        identificacionHistoriaProblema: int,
        identificacionProblema: int,
        fecha: str,
        estatus: str,
        observacion: str,
    ):
        self.identificacionHistoriaProblema = identificacionHistoriaProblema
        self._identificacionProblema = identificacionProblema
        self.fecha = fecha
        self.estatus = estatus
        self._observacion = observacion

    @property
    def identificacionProblema(self):
        return self._identificacionProblema

    @identificacionProblema.setter
    def identificacionProblema(self, value):
        self._identificacionProblema = value

    @property
    def observacion(self):
        return self._observacion

    @observacion.setter
    def observacion(self, value):
        self._observacion = value

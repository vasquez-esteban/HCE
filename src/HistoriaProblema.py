class HistoriaProblema:
    def __init__(
        self,
        identificacionHistoriaProblema: int,
        identificacionProblema: int,
        fecha: str,
        estatus: str,
        observacion: str,
    ):
        """
        Clase que representa la historia asociada a un problema de salud.

        Args:
            identificacionHistoriaProblema (int): Identificador único de la historia del problema.
            identificacionProblema (int): Identificador del problema de salud asociado.
            fecha (str): Fecha de la historia del problema de salud.
            estatus (str): Estado del problema de salud en esta fecha.
            observacion (str): Observación relacionada con el problema de salud.
        """
        self.identificacionHistoriaProblema = identificacionHistoriaProblema
        self._identificacionProblema = identificacionProblema
        self.fecha = fecha
        self.estatus = estatus
        self._observacion = observacion

    # Inicio de métodos get y set
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

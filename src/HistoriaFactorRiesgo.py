class HistoriaFactorRiesgo:
    def __init__(
        self,
        identificacionHistoriaFactor: int,
        identificacionFactorRiesgo: int,
        fecha: str,
        estatus: str,
        observacion: str,
    ):
        """
        Clase que representa la historia asociada a un factor de riesgo de la salud.

        Args:
            identificacionHistoriaFactor (int): Identificador único de la historia.
            identificacionFactorRiesgo (int): Identificador del factor de riesgo asociado.
            fecha (str): Fecha de la historia del factor de riesgo.
            estatus (str): Estado del factor de riesgo en esta fecha.
            observacion (str): Observación relacionada el factor de riesgo en esta fecha.
        """
        self.identificacionHistoriaProblema = identificacionHistoriaFactor
        self._identificacion = identificacionFactorRiesgo
        self.fecha = fecha
        self.estatus = estatus
        self._observacion = observacion

    # Inicio de métodos get y set
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

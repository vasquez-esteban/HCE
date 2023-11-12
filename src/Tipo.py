from enum import Enum


class Tipo(Enum):
    """Clase que sirve para representar tipos de problemas y/o factores de riesgo"""

    HEREDITARIO = "H"
    ADQUIRIDO = "A"
    MIXTO = "M"

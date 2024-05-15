from dataclasses import dataclass
from model.country import Country

@dataclass
class Connessione:
    v1: Country
    v2: Country

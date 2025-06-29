from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class Visitor:
    """Value Object que representa un visitante del museo"""
    name: str
    
    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("El nombre del visitante no puede estar vacío")
        # Normalizar el nombre para comparaciones
        object.__setattr__(self, 'name', self.name.strip().title())
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Visitor):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)


@dataclass(frozen=True)
class Room:
    """Value Object que representa una sala del museo"""
    number: int
    
    def __post_init__(self):
        if self.number not in [1, 2, 3]:
            raise ValueError("El número de sala debe ser 1, 2 o 3")
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Room):
            return False
        return self.number == other.number
    
    def __hash__(self) -> int:
        return hash(self.number)
    
    def __str__(self) -> str:
        return f"Sala {self.number}"

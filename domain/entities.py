from typing import Dict, Set, List
from .value_objects import Visitor, Room


class Museum:
    """
    Entidad principal que representa el museo y gestiona los visitantes por sala.
    Es el agregado raíz del dominio.
    """
    
    def __init__(self):
        # Diccionario que mapea cada sala con su conjunto de visitantes
        self._visitors_by_room: Dict[Room, Set[Visitor]] = {
            Room(1): set(),
            Room(2): set(),
            Room(3): set()
        }
    
    def register_visitor_in_room(self, visitor: Visitor, room: Room) -> None:
        """
        Registra un visitante en una sala específica del museo.
        
        Args:
            visitor: El visitante a registrar
            room: La sala en la que se registra el visitante
        """
        if room not in self._visitors_by_room:
            raise ValueError(f"La sala {room.number} no existe en el museo")
        
        self._visitors_by_room[room].add(visitor)
    
    def get_visitors_in_room(self, room: Room) -> Set[Visitor]:
        """
        Obtiene todos los visitantes registrados en una sala específica.
        
        Args:
            room: La sala de la cual obtener los visitantes
            
        Returns:
            Conjunto de visitantes en la sala especificada
        """
        if room not in self._visitors_by_room:
            raise ValueError(f"La sala {room.number} no existe en el museo")
        
        return self._visitors_by_room[room].copy()
    
    def get_all_visitors_by_room(self) -> Dict[Room, Set[Visitor]]:
        """
        Obtiene todos los visitantes organizados por sala.
        
        Returns:
            Diccionario con las salas como clave y conjuntos de visitantes como valor
        """
        return {room: visitors.copy() for room, visitors in self._visitors_by_room.items()}
    
    def get_all_rooms(self) -> List[Room]:
        """
        Obtiene todas las salas del museo.
        
        Returns:
            Lista de todas las salas disponibles
        """
        return list(self._visitors_by_room.keys())

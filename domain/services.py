from typing import Set, List
from .entities import Museum
from .value_objects import Visitor


class MuseumDomainService:
    """
    Servicio de dominio que contiene la lógica de negocio compleja
    que no pertenece a ninguna entidad específica.
    """
    
    @staticmethod
    def get_unique_visitors(museum: Museum) -> Set[Visitor]:
        """
        Obtiene una lista única de todos los visitantes que han estado
        en alguna de las salas del museo.
        
        Args:
            museum: La instancia del museo
            
        Returns:
            Conjunto único de visitantes (sin duplicados)
        """
        all_visitors = set()
        visitors_by_room = museum.get_all_visitors_by_room()
        
        # Unir todos los conjuntos de visitantes de todas las salas
        for visitors in visitors_by_room.values():
            all_visitors.update(visitors)
        
        return all_visitors
    
    @staticmethod
    def get_unique_visitors_as_sorted_list(museum: Museum) -> List[str]:
        """
        Obtiene una lista ordenada alfabéticamente de nombres únicos de visitantes.
        
        Args:
            museum: La instancia del museo
            
        Returns:
            Lista ordenada de nombres de visitantes únicos
        """
        unique_visitors = MuseumDomainService.get_unique_visitors(museum)
        return sorted([visitor.name for visitor in unique_visitors])

from typing import List
from domain.entities import Museum
from domain.value_objects import Visitor, Room
from domain.services import MuseumDomainService
from domain.dto import VisitorRegistrationDto, MuseumReportDto


class RegisterVisitorUseCase:
    """Caso de uso para registrar un visitante en una sala del museo"""
    
    def __init__(self, museum: Museum):
        self._museum = museum
    
    def execute(self, registration_dto: VisitorRegistrationDto) -> None:
        """
        Ejecuta el registro de un visitante en una sala.
        
        Args:
            registration_dto: DTO con los datos del visitante y sala
        """
        try:
            visitor = Visitor(registration_dto.visitor_name)
            room = Room(registration_dto.room_number)
            
            self._museum.register_visitor_in_room(visitor, room)
            
        except ValueError as e:
            raise ValueError(f"Error al registrar visitante: {str(e)}")


class GetMuseumReportUseCase:
    """Caso de uso para obtener el reporte completo del museo"""
    
    def __init__(self, museum: Museum):
        self._museum = museum
        self._domain_service = MuseumDomainService()
    
    def execute(self) -> MuseumReportDto:
        """
        Ejecuta la generación del reporte completo del museo.
        
        Returns:
            DTO con el reporte completo del museo
        """
        # Obtener visitantes por sala
        visitors_by_room_dict = {}
        all_rooms = self._museum.get_all_rooms()
        
        for room in all_rooms:
            visitors = self._museum.get_visitors_in_room(room)
            visitors_by_room_dict[room.number] = sorted([v.name for v in visitors])
        
        # Obtener lista única de visitantes
        unique_visitors = self._domain_service.get_unique_visitors_as_sorted_list(self._museum)
        
        return MuseumReportDto(
            visitors_by_room=visitors_by_room_dict,
            unique_visitors=unique_visitors,
            total_unique_visitors=len(unique_visitors)
        )


class RegisterMultipleVisitorsUseCase:
    """Caso de uso para registrar múltiples visitantes de una vez"""
    
    def __init__(self, museum: Museum):
        self._register_use_case = RegisterVisitorUseCase(museum)
    
    def execute(self, registrations: List[VisitorRegistrationDto]) -> List[str]:
        """
        Ejecuta el registro de múltiples visitantes.
        
        Args:
            registrations: Lista de DTOs con registros de visitantes
            
        Returns:
            Lista de mensajes de error (vacía si todo fue exitoso)
        """
        errors = []
        
        for registration in registrations:
            try:
                self._register_use_case.execute(registration)
            except ValueError as e:
                errors.append(str(e))
        
        return errors

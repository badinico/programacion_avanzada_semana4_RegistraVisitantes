from dataclasses import dataclass
from typing import List, Dict


@dataclass
class VisitorRegistrationDto:
    """DTO para el registro de un visitante en una sala"""
    visitor_name: str
    room_number: int


@dataclass
class RoomVisitorsDto:
    """DTO que representa los visitantes de una sala específica"""
    room_number: int
    visitors: List[str]


@dataclass
class MuseumReportDto:
    """DTO para el reporte completo del museo"""
    visitors_by_room: Dict[int, List[str]]
    unique_visitors: List[str]
    total_unique_visitors: int

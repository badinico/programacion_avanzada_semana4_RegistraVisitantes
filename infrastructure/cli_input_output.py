from typing import List, Optional
from domain.dto import VisitorRegistrationDto, MuseumReportDto


class CliInputOutput:
    """Clase para manejo de entrada y salida por consola"""
    
    @staticmethod
    def show_welcome_message() -> None:
        """Muestra el mensaje de bienvenida del sistema"""
        print("=" * 60)
        print("SISTEMA DE REGISTRO DE VISITANTES DEL MUSEO DE PARIS")
        print("=" * 60)
        print()
    
    @staticmethod
    def show_menu() -> None:
        """Muestra el menú principal de opciones"""
        print("\nMENU PRINCIPAL:")
        print("1. Registrar visitante en sala")
        print("2. Ver reporte de visitantes")
        print("3. Registrar multiples visitantes")
        print("4. Salir")
        print("-" * 40)
    
    @staticmethod
    def get_menu_choice() -> str:
        """Obtiene la opción seleccionada del menú"""
        return input("Seleccione una opción (1-4): ").strip()
    
    @staticmethod
    def get_visitor_registration() -> Optional[VisitorRegistrationDto]:
        """
        Obtiene los datos para registrar un visitante.
        
        Returns:
            DTO con los datos del visitante o None si hay error
        """
        try:
            print("\nREGISTRO DE VISITANTE:")
            visitor_name = input("Ingrese el nombre del visitante: ").strip()
            
            if not visitor_name:
                print("ERROR: El nombre no puede estar vacio")
                return None
            
            print("Salas disponibles: 1, 2, 3")
            room_str = input("Ingrese el numero de sala (1-3): ").strip()
            
            if not room_str.isdigit() or int(room_str) not in [1, 2, 3]:
                print("ERROR: Debe ingresar un numero de sala valido (1, 2 o 3)")
                return None
            
            return VisitorRegistrationDto(
                visitor_name=visitor_name,
                room_number=int(room_str)
            )
            
        except Exception as e:
            print(f"ERROR inesperado: {str(e)}")
            return None
    
    @staticmethod
    def get_multiple_visitors_registration() -> List[VisitorRegistrationDto]:
        """
        Obtiene datos para registrar múltiples visitantes.
        
        Returns:
            Lista de DTOs con los datos de los visitantes
        """
        registrations = []
        print("\nREGISTRO MULTIPLE DE VISITANTES:")
        print("(Presione Enter en el nombre para terminar)")
        
        while True:
            visitor_name = input(f"\nIngrese el nombre del visitante #{len(registrations) + 1}: ").strip()
            
            if not visitor_name:
                if len(registrations) == 0:
                    print("ERROR: Debe registrar al menos un visitante")
                    continue
                break
            
            print("Salas disponibles: 1, 2, 3")
            room_str = input("Ingrese el numero de sala (1-3): ").strip()
            
            if not room_str.isdigit() or int(room_str) not in [1, 2, 3]:
                print("ERROR: Numero de sala invalido. Intente nuevamente.")
                continue
            
            registrations.append(VisitorRegistrationDto(
                visitor_name=visitor_name,
                room_number=int(room_str)
            ))
            
            print(f"Visitante '{visitor_name}' agregado a la sala {room_str}")
        
        return registrations
    
    @staticmethod
    def show_registration_success(visitor_name: str, room_number: int) -> None:
        """Muestra mensaje de éxito en el registro"""
        print(f"Visitante '{visitor_name}' registrado exitosamente en la Sala {room_number}")
    
    @staticmethod
    def show_registration_error(error_message: str) -> None:
        """Muestra mensaje de error en el registro"""
        print(f"ERROR: {error_message}")
    
    @staticmethod
    def show_museum_report(report: MuseumReportDto) -> None:
        """
        Muestra el reporte completo del museo.
        
        Args:
            report: DTO con los datos del reporte
        """
        print("\n" + "=" * 60)
        print("REPORTE DE VISITANTES DEL MUSEO")
        print("=" * 60)
        
        # Mostrar visitantes por sala
        print("\nVISITANTES POR SALA:")
        for room_number in sorted(report.visitors_by_room.keys()):
            visitors = report.visitors_by_room[room_number]
            print(f"\n   Sala {room_number}:")
            if visitors:
                for visitor in visitors:
                    print(f"   - {visitor}")
            else:
                print("   - Sin visitantes registrados")
        
        # Mostrar lista única de visitantes
        print(f"\nLISTA UNICA DE VISITANTES:")
        if report.unique_visitors:
            for visitor in report.unique_visitors:
                print(f"   - {visitor}")
        else:
            print("   - No hay visitantes registrados")
        
        print(f"\nTOTAL DE VISITANTES UNICOS: {report.total_unique_visitors}")
        print("=" * 60)
    
    @staticmethod
    def show_multiple_registration_results(errors: List[str], total_attempted: int) -> None:
        """
        Muestra los resultados del registro múltiple.
        
        Args:
            errors: Lista de errores ocurridos
            total_attempted: Total de registros intentados
        """
        successful = total_attempted - len(errors)
        
        print(f"\nRESULTADOS DEL REGISTRO MULTIPLE:")
        print(f"   Registros exitosos: {successful}")
        print(f"   Registros con error: {len(errors)}")
        
        if errors:
            print("\nERRORES ENCONTRADOS:")
            for i, error in enumerate(errors, 1):
                print(f"   {i}. {error}")
    
    @staticmethod
    def show_goodbye_message() -> None:
        """Muestra mensaje de despedida"""
        print("\nGracias por usar el Sistema de Registro de Visitantes!")
        print("Que tenga un buen dia!")
    
    @staticmethod
    def wait_for_enter() -> None:
        """Espera a que el usuario presione Enter para continuar"""
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def show_invalid_option() -> None:
        """Muestra mensaje de opción inválida"""
        print("Opcion invalida. Por favor, seleccione una opcion valida (1-4).")

"""
Sistema de Registro de Visitantes del Museo de París
Implementado con arquitectura Domain-Driven Design (DDD)
"""

from domain.entities import Museum
from application.use_cases import (
    RegisterVisitorUseCase, 
    GetMuseumReportUseCase, 
    RegisterMultipleVisitorsUseCase
)
from infrastructure.cli_input_output import CliInputOutput


class MuseumApplication:
    """Clase principal de la aplicación del museo"""
    
    def __init__(self):
        # Inicializar el agregado raíz del dominio
        self._museum = Museum()
        
        # Inicializar los casos de uso
        self._register_visitor_use_case = RegisterVisitorUseCase(self._museum)
        self._get_report_use_case = GetMuseumReportUseCase(self._museum)
        self._register_multiple_use_case = RegisterMultipleVisitorsUseCase(self._museum)
        
        # Inicializar la infraestructura de I/O
        self._io = CliInputOutput()
    
    def run(self) -> None:
        """Ejecuta el bucle principal de la aplicación"""
        self._io.show_welcome_message()
        
        # Cargar datos de prueba
        self._load_test_data()
        
        while True:
            try:
                self._io.show_menu()
                choice = self._io.get_menu_choice()
                
                if choice == "1":
                    self._handle_register_visitor()
                elif choice == "2":
                    self._handle_show_report()
                elif choice == "3":
                    self._handle_register_multiple_visitors()
                elif choice == "4":
                    self._handle_exit()
                    break
                else:
                    self._io.show_invalid_option()
                    
            except KeyboardInterrupt:
                print("\n\nOperacion cancelada por el usuario")
                self._handle_exit()
                break
            except Exception as e:
                print(f"\nError inesperado: {str(e)}")
                self._io.wait_for_enter()
    
    def _handle_register_visitor(self) -> None:
        """Maneja el registro de un visitante individual"""
        registration_dto = self._io.get_visitor_registration()
        
        if registration_dto is None:
            return
        
        try:
            self._register_visitor_use_case.execute(registration_dto)
            self._io.show_registration_success(
                registration_dto.visitor_name, 
                registration_dto.room_number
            )
        except ValueError as e:
            self._io.show_registration_error(str(e))
        
        self._io.wait_for_enter()
    
    def _handle_show_report(self) -> None:
        """Maneja la visualización del reporte del museo"""
        try:
            report = self._get_report_use_case.execute()
            self._io.show_museum_report(report)
        except Exception as e:
            self._io.show_registration_error(f"Error al generar reporte: {str(e)}")
        
        self._io.wait_for_enter()
    
    def _handle_register_multiple_visitors(self) -> None:
        """Maneja el registro de múltiples visitantes"""
        registrations = self._io.get_multiple_visitors_registration()
        
        if not registrations:
            print("ERROR: No se registraron visitantes")
            self._io.wait_for_enter()
            return
        
        try:
            errors = self._register_multiple_use_case.execute(registrations)
            self._io.show_multiple_registration_results(errors, len(registrations))
        except Exception as e:
            self._io.show_registration_error(f"Error en registro múltiple: {str(e)}")
        
        self._io.wait_for_enter()
    
    def _handle_exit(self) -> None:
        """Maneja la salida de la aplicación"""
        self._io.show_goodbye_message()
    
    def _load_test_data(self) -> None:
        """Carga datos de prueba en el museo"""
        from domain.dto import VisitorRegistrationDto
        
        # Datos de prueba según el ejemplo mostrado en la imagen
        test_data = [
            VisitorRegistrationDto("Pedro", 1),
            VisitorRegistrationDto("Carlos", 1),
            VisitorRegistrationDto("Manuel", 1),
            VisitorRegistrationDto("Laura", 2),
            VisitorRegistrationDto("Juan", 2),
            VisitorRegistrationDto("Elena", 3),
            VisitorRegistrationDto("Luis", 3),
            VisitorRegistrationDto("Pedro", 2),  # Pedro visita también la sala 2
            VisitorRegistrationDto("Carlos", 3),  # Carlos visita también la sala 3
        ]
        
        # Registrar datos de prueba
        errors = self._register_multiple_use_case.execute(test_data)
        
        if errors:
            print("ADVERTENCIA: Algunos datos de prueba no se pudieron cargar:")
            for error in errors:
                print(f"   - {error}")


def main():
    """Función principal de entrada"""
    try:
        app = MuseumApplication()
        app.run()
    except Exception as e:
        print(f"\nError critico en la aplicacion: {str(e)}")
        print("Por favor, contacte al administrador del sistema.")


if __name__ == "__main__":
    main()

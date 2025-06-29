# Sistema de Registro de Visitantes - Museo de París

## Descripción

Sistema de registro de visitantes para el museo de París que permite controlar y gestionar los visitantes que han recorrido las tres salas del museo (Sala 1, Sala 2 y Sala 3). El sistema permite registrar visitantes por sala y generar una lista única de todos los visitantes que han estado en alguna de las salas, eliminando automáticamente los duplicados de aquellos que visitaron múltiples salas.

## Características Principales

- Registro de visitantes en las tres salas del museo (1, 2, 3)
- Generación automática de lista única de visitantes (sin duplicados)
- Validación de nombres de visitantes (no pueden estar vacíos)
- Verificación de números de sala válidos (1, 2 o 3)
- Normalización automática de nombres (formato título)
- Interfaz CLI interactiva con menús intuitivos
- Datos de prueba precargados para demostración
- Arquitectura limpia basada en Domain Driven Design (DDD)

## Arquitectura del Proyecto

El proyecto sigue los principios de **Domain Driven Design (DDD)** con la siguiente estructura:

```
programacion_avanzada_semana4_RegistraVisitantes/
├── domain/                 # Capa de dominio
│   ├── entities.py        # Entidades del negocio (Museum)
│   ├── value_objects.py   # Objetos de valor (Visitor, Room)
│   ├── services.py        # Servicios del dominio
│   └── dto.py            # Data Transfer Objects
├── application/           # Capa de aplicación
│   └── use_cases.py      # Casos de uso
├── infrastructure/        # Capa de infraestructura
│   └── cli_input_output.py # Implementación CLI
└── main.py               # Punto de entrada
```

### Componentes Principales

#### Domain Layer (Dominio)
- **`Museum`**: Entidad principal (agregado raíz) que gestiona los visitantes por sala
- **`Visitor`**: Objeto de valor que representa un visitante con validaciones
- **`Room`**: Objeto de valor para las salas del museo (1, 2, 3)
- **`MuseumDomainService`**: Servicio que contiene la lógica para obtener visitantes únicos
- **DTOs**: Para transferir datos entre capas

#### Application Layer (Aplicación)
- **`RegisterVisitorUseCase`**: Caso de uso para registrar un visitante individual
- **`GetMuseumReportUseCase`**: Caso de uso para generar reportes del museo
- **`RegisterMultipleVisitorsUseCase`**: Caso de uso para registro múltiple

#### Infrastructure Layer (Infraestructura)
- **`CliInputOutput`**: Implementación CLI para interactuar con el usuario

## Requisitos

- Python 3.8 o superior
- No se requieren dependencias externas

## Instalación y Uso

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <repository-url>
   cd programacion_avanzada_semana4_RegistraVisitantes
   ```

2. **Ejecutar el sistema**
   ```bash
   python main.py
   ```

3. **Seguir las instrucciones en pantalla**
   - Seleccionar una opción del menú principal
   - Registrar visitantes individuales o múltiples
   - Ver reportes completos del museo

## Ejemplos de Uso

### Caso Exitoso - Registro Individual
```
============================================================
SISTEMA DE REGISTRO DE VISITANTES DEL MUSEO DE PARIS
============================================================

MENU PRINCIPAL:
1. Registrar visitante en sala
2. Ver reporte de visitantes
3. Registrar multiples visitantes
4. Salir

Seleccione una opción (1-4): 1

REGISTRO DE VISITANTE:
Ingrese el nombre del visitante: María García
Salas disponibles: 1, 2, 3
Ingrese el numero de sala (1-3): 1

Visitante 'María García' registrado exitosamente en la Sala 1
```

### Reporte de Visitantes
```
============================================================
REPORTE DE VISITANTES DEL MUSEO
============================================================

VISITANTES POR SALA:

   Sala 1:
   - Carlos
   - Manuel
   - María García
   - Pedro

   Sala 2:
   - Juan
   - Laura
   - Pedro

   Sala 3:
   - Carlos
   - Elena
   - Luis

LISTA UNICA DE VISITANTES:
   - Carlos
   - Elena
   - Juan
   - Laura
   - Luis
   - Manuel
   - María García
   - Pedro

TOTAL DE VISITANTES UNICOS: 8
============================================================
```

### Caso de Error - Nombre Vacío
```
REGISTRO DE VISITANTE:
Ingrese el nombre del visitante: 
ERROR: El nombre no puede estar vacio
```

### Caso de Error - Sala Inválida
```
Salas disponibles: 1, 2, 3
Ingrese el numero de sala (1-3): 5
ERROR: Debe ingresar un numero de sala valido (1, 2 o 3)
```

### Registro Múltiple
```
REGISTRO MULTIPLE DE VISITANTES:
(Presione Enter en el nombre para terminar)

Ingrese el nombre del visitante #1: Ana López
Salas disponibles: 1, 2, 3
Ingrese el numero de sala (1-3): 2
Visitante 'Ana López' agregado a la sala 2

Ingrese el nombre del visitante #2: 

RESULTADOS DEL REGISTRO MULTIPLE:
   Registros exitosos: 1
   Registros con error: 0
```

## Datos de Prueba

El sistema incluye datos de prueba precargados que simulan visitantes del museo:

- **Sala 1**: Pedro, Carlos, Manuel
- **Sala 2**: Laura, Juan, Pedro (Pedro visita múltiples salas)
- **Sala 3**: Elena, Luis, Carlos (Carlos visita múltiples salas)

**Lista única resultante**: Carlos, Elena, Juan, Laura, Luis, Manuel, Pedro (7 visitantes únicos)

## Validaciones Implementadas

1. **Nombres no vacíos**: Los nombres de visitantes no pueden estar vacíos o contener solo espacios
2. **Normalización de nombres**: Los nombres se normalizan automáticamente al formato título
3. **Salas válidas**: Solo acepta números de sala 1, 2 o 3
4. **Eliminación de duplicados**: Los visitantes que visitan múltiples salas aparecen una sola vez en la lista única
5. **Entrada numérica válida**: Valida que se ingresen números válidos para las salas

## Manejo de Excepciones

- **ValueError**: Para validaciones de dominio (nombres vacíos, salas inválidas)
- **KeyboardInterrupt**: Para manejo graceful de interrupción del usuario (Ctrl+C)
- **Excepciones generales**: Captura y maneja cualquier error inesperado con mensajes informativos

## Funcionalidades del Sistema

### 1. Registro Individual de Visitantes
- Permite registrar un visitante en una sala específica
- Validación inmediata de datos
- Confirmación de registro exitoso

### 2. Registro Múltiple de Visitantes
- Permite registrar varios visitantes de una vez
- Proceso interactivo con validación por visitante
- Reporte de resultados con errores y éxitos

### 3. Reporte Completo del Museo
- Muestra visitantes organizados por sala
- Genera lista única de todos los visitantes
- Cuenta total de visitantes únicos
- Formato profesional y fácil de leer

### 4. Gestión de Duplicados
- Identifica automáticamente visitantes que visitan múltiples salas
- Mantiene registro por sala pero genera lista única global
- Algoritmo eficiente usando conjuntos (sets) de Python

## Principios de Diseño Aplicados

- **Single Responsibility Principle**: Cada clase tiene una responsabilidad específica
- **Dependency Inversion**: Las capas superiores no dependen de las inferiores
- **Clean Architecture**: Separación clara entre dominio, aplicación e infraestructura
- **Domain Driven Design**: El dominio del museo es el centro de la aplicación
- **Immutable Value Objects**: Los objetos Visitor y Room son inmutables
- **Aggregate Pattern**: Museum actúa como agregado raíz del dominio
- **Error Handling**: Manejo robusto de errores con capacidad de reintento

## Estructura de Clases Principales

### Value Objects
- **`Visitor`**: Representa un visitante con validaciones y normalización
- **`Room`**: Representa una sala del museo con validaciones

### Entities
- **`Museum`**: Agregado raíz que gestiona el estado de visitantes por sala

### Services
- **`MuseumDomainService`**: Lógica de negocio para obtener listas únicas

### Use Cases
- **`RegisterVisitorUseCase`**: Registro individual
- **`GetMuseumReportUseCase`**: Generación de reportes
- **`RegisterMultipleVisitorsUseCase`**: Registro en lote

## Desarrollado por

Sistema de Gestión para el Museo de París - Arquitectura DDD


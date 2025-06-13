# Cascada de Eventos: Diseño y Simulación Interactiva de Máquinas de Goldberg usando Pygame/pymunk

## Autores

- Kevin Sebastián Cifuentes López  
- Mariana Lopera Correa  
- Emanuel García Ríos  

### Universidad de Medellín

## Descripción

La enseñanza de la física mecánica presenta el reto constante de conectar conceptos teóricos con experiencias significativas que fomenten el aprendizaje activo. En este contexto, la presente propuesta introduce una simulación computacional de una máquina de Goldberg como herramienta pedagógica para la exploración de los principios fundamentales de la mecánica clásica, tales como la conservación de la energía, las leyes del movimiento de Newton y las interacciones entre cuerpos rígidos.

El objetivo principal del proyecto es diseñar y desarrollar una simulación interactiva que permita visualizar de manera intuitiva y entretenida los efectos de fuerzas, colisiones, fricción y trayectorias complejas dentro de un sistema mecánico encadenado. La metodología se basa en el uso de Pymunk, una biblioteca de Python para simulación de física 2D, que facilita el modelado de objetos, cuerpos dinámicos y contactos realistas mediante un motor de física robusto.

Durante la ejecución del proyecto se implementaron diferentes módulos que representan componentes típicos de una máquina de Goldberg (planos inclinados, esferas, palancas, etc.), integrados en una secuencia que desencadena múltiples reacciones en cadena.

## Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd physic-goldberg-machine
```

## Dependencias

- Python 3.12.3  
- pymunk>=7.0.0  
- pygame>=2.5.0  
- numpy>=1.24.0  
- pandas>=2.1.0  
- matplotlib>=3.8.0  
- jupyter>=1.0.0  
- scipy>=1.11.0  

## Instalación de dependencias

### 1. Crear y activar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate # Linux / macOS
# o en Windows
venv\Scripts\activate
```

### 2. Instalar paquetes

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

Presione `ESC` durante la simulación para salir.

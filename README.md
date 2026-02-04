# Timer Apagado

Aplicación de escritorio en Python con interfaz Tkinter que permite configurar una cuenta regresiva y apagar el equipo cuando llega a $00:00:00$.

## Características
- Configuración de horas, minutos y segundos.
- Controles de iniciar, pausar/reanudar y detener.
- Muestra del tiempo restante en formato `HH:MM:SS`.
- Ejecuta apagado del sistema al finalizar la cuenta.

## Uso
1. Ejecuta el script:
   ````bash
   python apagado.py
2. Introduce el tiempo deseado y presiona Iniciar cuenta regresiva.

## Estructura
apagado.py: contiene la clase ContadorRegresivo y la interfaz.
Notas
El apagado se ejecuta con shutdown /s /t 0, pensado para Windows.

Para generar un ejecutable se puede usar PyInstaller con Timer Out.spec.
O puedes encontrar el ejecutable en la carpeta Dist

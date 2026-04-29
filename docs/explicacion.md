# Explicación del JSON de Wokwi y del diseño de hardware

## Resumen del JSON

El JSON de Wokwi describe una simulación con:

- 1 Raspberry Pi Pico (`wokwi-pi-pico`)
- 1 teclado matricial (`wokwi-membrane-keypad`)
- resistencias de 1 kΩ (componentes `wokwi-resistor`)
- al menos 1 LED explícito en el extracto (`wokwi-led`)

Aunque el fragmento mostrado no incluye todo el arreglo de LEDs/cables, el firmware original y la migración definen claramente el uso de **12 salidas GPIO para LEDs** y **8 GPIO para keypad**.

## Interpretación funcional

El sistema se divide en dos bloques:

1. **Entrada (keypad 4x4):**
   - Se escanean filas y columnas para detectar una tecla.
   - Se obtiene un carácter (`'0'..'9', 'A'..'D', '*', '#'`).

2. **Salida (12 LEDs):**
   - Cada tecla aplica una acción de encendido/apagado sobre uno o varios LEDs.

## Paridad con el programa original

La migración a MicroPython conserva:

- misma tabla de teclas (`keys`)
- mismos pines para filas/columnas y LEDs
- misma semántica de acciones por tecla
- misma cadencia de lazo (~10 ms)

## Comportamiento importante

El diseño es **acumulativo** para comandos de encendido individuales:

- Pulsar `1` enciende LED0, pero no apaga los demás.
- Pulsar `A` enciende LED8, sin afectar LED9..LED11.

Solo ciertas teclas realizan acciones grupales de apagado:

- `0` apaga LEDs 0..7
- `#` apaga LEDs 8..11

## Consideración sobre rebote (debounce)

Se implementa un antirrebote simple:

- se reporta una tecla solo al detectar transición de “sin tecla” a “tecla presionada”
- se espera a la liberación para permitir nueva detección

Esto evita repeticiones rápidas no deseadas y replica el uso típico de `getKey()` de librerías tipo Arduino.

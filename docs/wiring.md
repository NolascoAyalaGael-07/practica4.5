# Conexiones de Hardware (Raspberry Pi Pico W + Keypad 4x4 + 12 LEDs)

Este documento describe el cableado recomendado para reproducir el comportamiento del proyecto.

## 1) Teclado matricial 4x4

El teclado tiene 8 líneas: 4 filas y 4 columnas.

- **Filas (outputs en escaneo):**
  - R1 -> GP26
  - R2 -> GP22
  - R3 -> GP21
  - R4 -> GP20

- **Columnas (inputs con pull-up):**
  - C1 -> GP19
  - C2 -> GP18
  - C3 -> GP17
  - C4 -> GP16

### Lógica de escaneo utilizada

- Las filas se mantienen en HIGH por defecto.
- Se baja una fila a LOW por vez.
- Si una columna se lee LOW durante ese instante, hay tecla presionada en esa intersección fila-columna.

## 2) LEDs

### Lista de GPIO para LEDs (12)

1. LED0  -> GP11
2. LED1  -> GP10
3. LED2  -> GP9
4. LED3  -> GP8
5. LED4  -> GP7
6. LED5  -> GP6
7. LED6  -> GP5
8. LED7  -> GP4
9. LED8  -> GP3
10. LED9 -> GP2
11. LED10 -> GP28
12. LED11 -> GP27

### Conexión eléctrica recomendada por LED

- GPx -> resistencia (220 Ω a 1 kΩ) -> ánodo del LED
- cátodo del LED -> GND

Con esta topología, `Pin.value(1)` enciende el LED y `Pin.value(0)` lo apaga.

## 3) Alimentación y tierra

- Usa GND común entre todos los componentes.
- Alimenta la Pico W por USB durante pruebas.

## 4) Correspondencia de teclas (matriz)

La matriz de teclas considerada es:

```text
[ ['1','2','3','A'],
  ['4','5','6','B'],
  ['7','8','9','C'],
  ['*','0','#','D'] ]
```

Esto define exactamente qué tecla corresponde a cada intersección de fila/columna.

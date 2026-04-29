# Control de 12 LEDs con Teclado Matricial 4x4 en Raspberry Pi Pico W (MicroPython)

Este proyecto migra una implementación original en **C++/Arduino** a **MicroPython** para la **Raspberry Pi Pico W (RP2040)**, manteniendo exactamente el mismo comportamiento funcional:

- Lectura de un teclado matricial 4x4.
- Control directo de 12 LEDs según la tecla presionada.

## Estructura del repositorio

```text
.
├── README.md
├── docs/
│   ├── wiring.md
│   └── explicacion.md
└── src/
    └── main.py
```

## Requisitos

- Raspberry Pi Pico W
- Firmware MicroPython para RP2040 instalado
- Teclado matricial 4x4
- 12 LEDs
- Resistencias limitadoras (recomendado: 220 Ω a 1 kΩ por LED)
- Protoboard y cables

## Mapeo de pines (igual al código original)

- **LEDs (12):** `GP11, GP10, GP9, GP8, GP7, GP6, GP5, GP4, GP3, GP2, GP28, GP27`
- **Filas keypad (4):** `GP26, GP22, GP21, GP20`
- **Columnas keypad (4):** `GP19, GP18, GP17, GP16`

## Comportamiento de teclas

- `1..8` → enciende LED individual (índices 0..7)
- `9` → enciende LEDs 0..7
- `0` → apaga LEDs 0..7
- `A` → enciende LED 8
- `B` → enciende LED 9
- `C` → enciende LED 10
- `D` → enciende LED 11
- `*` → enciende LEDs 8..11
- `#` → apaga LEDs 8..11

> Nota: igual que en el original, las teclas de encendido **no apagan automáticamente** otros LEDs.

## Carga y ejecución

1. Copia `src/main.py` como `main.py` a la Pico W (por ejemplo con Thonny).
2. Reinicia la placa.
3. Presiona teclas del keypad para verificar la respuesta de LEDs.

## Validación rápida

- Al pulsar `9`, los primeros 8 LEDs quedan encendidos.
- Al pulsar `0`, los primeros 8 LEDs quedan apagados.
- Al pulsar `*`, los últimos 4 LEDs quedan encendidos.
- Al pulsar `#`, los últimos 4 LEDs quedan apagados.

Consulta la documentación detallada en:

- `docs/wiring.md`
- `docs/explicacion.md`

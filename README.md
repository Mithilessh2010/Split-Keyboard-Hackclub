# Split Keyboard Project

This repository contains the full design for my custom split keyboard, including the PCB, schematic, case files, and bill of materials. Everything needed to build or modify the keyboard is documented here in a clear and approachable format.

## Overview

The keyboard is built around the Seeed XIAO nRF52840 microcontroller, Kailh Choc low profile switches, SOD-123 diodes, and a simple two-piece 3D printed case. The goal of the project is to create a compact split keyboard that is straightforward to assemble and easy to modify.

## Images

All images for the project can be found in the Images folder.

### CAD View (Final, just unmated for clarity)
![CAD](Images/Screen%20Shot%202025-12-04%20at%206.03.44%20PM.png)

### PCB Layout
![PCB](Images/Screen%20Shot%202025-12-02%20at%208.39.47%20PM.png)

### Schematics
![Schematics](Images/Screen%20Shot%202025-12-02%20at%206.21.25%20PM.png)

## Bill of Materials

Below is the full set of components used in the keyboard.

### BOM Table

| Category         | Part Description             | Footprint                    | Quantity |
|------------------|------------------------------|------------------------------|----------|
| Resistors        | 806k ohm                     | R_0805_2012Metric            | 2        |
|                  | 2M ohm                       | R_0805_2012Metric            | 2        |
|                  | R (0 ohm or jumper)          | R_0805_2012Metric            | 1        |
| Diodes           | SOD-123 diode                | D_SOD-123                    | 42       |
| Microcontrollers | Seeed XIAO nRF52840          | modified-XIAO-nRF52840-SMD   | 2        |
| Switches         | Kailh Choc V1 switches       | SW_choc_v1_1u                | 41       |
| Test Points      | Test pad                     | TestPoint_Pad_D2.0mm         | 4        |

## 3D Printed Parts

The keyboard uses two printed case parts.

- Top case  
- Bottom case  

Both parts are sized so the PCB fits properly without forcing anything into place.

## Assembly Instructions

1. Install and solder all diodes first. These sit flat on the PCB.
2. Solder all resistors.
3. Insert and solder all Kailh Choc switches.
4. Attach both XIAO nRF52840 modules and verify each pin is properly soldered.
5. Inspect the board and test the key matrix.
6. Place the PCB into the printed case and complete the assembly.

## Cost Breakdown

### AliExpress Order
![ALIEXPRESSTOTAL](https://github.com/Mithilessh2010/Split-Keyboard-Hackclub/blob/main/Images/Screen%20Shot%202025-12-05%20at%207.49.29%20AM.png)
![ALIEXPRESS1](https://github.com/Mithilessh2010/Split-Keyboard-Hackclub/blob/main/Images/Screen%20Shot%202025-12-05%20at%207.50.40%20AM.png)
![ALIEXPRESS2](https://github.com/Mithilessh2010/Split-Keyboard-Hackclub/blob/main/Images/Screen%20Shot%202025-12-05%20at%207.50.35%20AM.png)


| Item                                                                 | Quantity | Price    |
|----------------------------------------------------------------------|----------|----------|
| SMD Capacitor and Resistor Book (0603 0805 1206)                    | 1        | $15.33   |
| Kailh Choc V1 Switches (Olive, 90 pcs)                               | 1        | $39.81   |
| RGeek 6.0 W/mK Thermal Pad (200mm x 400mm, 2mm thick)                | 1        | $23.29   |
| Seeed Studio XIAO BLE nRF52840 Module                                | 1        | $22.85   |
| Shipping for XIAO module                                            | 1        | $5.04    |
| Additional charges (import, fees)                                   | —        | $10.38   |
|                                                                      |          |          |
| Subtotal                                                             |          | $101.28  |
| Shipping                                                             |          | $5.04    |
| Additional charges                                                   |          | $10.38   |
| **AliExpress total**                                                 |          | **$116.70** |

### JLCPCB Order

![JLPCB](Images/Screen%20Shot%202025-12-04%20at%208.39.20%20PM.png)

| Item                          | Quantity | Price  |
|-------------------------------|----------|--------|
| PCB prototype (5 boards)      | 5        | $28.92 |

## Total Spent

| Source        | Cost     |
|---------------|----------|
| AliExpress    | $116.70  |
| JLCPCB        | $28.92   |
|               |          |
| **Total spent** | **$145.62** |

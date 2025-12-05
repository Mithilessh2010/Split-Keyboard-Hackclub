# Split Keyboard Project

This repository contains the full design for my custom split keyboard, including the PCB, schematic, case files, and bill of materials. Everything needed to build or modify the keyboard is documented here in a clear and approachable format.

## Overview

The keyboard is built around the Seeed XIAO nRF52840 microcontroller, Kailh Choc low profile switches, SOD-123 diodes, and a simple two-piece 3D printed case. The goal of the project is to create a compact split keyboard that is straightforward to assemble and easy to modify.

## Images

All images for the project can be found in the Images folder.

### CAD View  
![CAD](Images/Screen%20Shot%202025-12-04%20at%206.03.44%20PM.png)

### PCB Layout  
![PCB](Images/Screen%20Shot%202025-12-02%20at%208.39.47%20PM.png)

### Schematics  
![Schematics](Images/Screen%20Shot%202025-12-02%20at%206.21.25%20PM.png)

## Bill of Materials

Below is the full list of components used in the keyboard.

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

The keyboard case consists of two printed parts.

- Top case  
- Bottom case  

Both parts are sized so that the PCB fits properly without forcing anything into place.

## Assembly Instructions

1. Install and solder all diodes. These sit flat on the board and are easiest to place first.  
2. Solder all resistors.  
3. Insert and solder all Kailh Choc switches.  
4. Attach both XIAO nRF52840 modules and verify each pin is fully soldered.  
5. Inspect the board and test the key matrix.  
6. Place the PCB into the printed case pieces and close the assembly.

## Cost Breakdown

### Amazon Order
![Amazon](https://github.com/Mithilessh2010/Split-Keyboard-Hackclub/blob/main/Images/Screen%20Shot%202025-12-04%20at%208.11.51%20PM.png)

| Item                                      | Quantity | Price   | Subtotal |
|-------------------------------------------|----------|---------|----------|
| Yobett 0805 Resistor and Capacitor Book  | 1        | $33.99  | $33.99   |
| Frienda Thermal Pad Set                   | 1        | $9.99   | $9.99    |
| Seeed Studio XIAO nRF52840                | 1        | $16.99  | $16.99   |
| Kailh Choc V1 Switches (35 pack)         | 2 packs  | $19.99  | $39.98   |
|                                           |          |         |          |
| Items total                               |          |         | $100.95  |
| Shipping, tax, and adjustments            |          |         | $10.34   |
| **Amazon total**                          |          |         | **$111.29** |

### JLCPCB Order
![JLPCB](https://github.com/Mithilessh2010/Split-Keyboard-Hackclub/blob/main/Images/Screen%20Shot%202025-12-04%20at%208.33.57%20PM.png)

| Item                          | Quantity | Price  |
|-------------------------------|----------|--------|
| PCB prototype (5 boards)      | 5        | $28.92 |

## Total Spent

| Source        | Cost    |
|---------------|---------|
| Amazon        | $111.29 |
| JLCPCB        | $28.92  |
|               |         |
| **Total spent** | **$140.21** |

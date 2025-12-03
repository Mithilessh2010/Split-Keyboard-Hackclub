# Split Keyboard Project

This repository contains the full design for my custom split keyboard, including the PCB, schematic, case files, and bill of materials. Everything needed to build or modify the keyboard is documented here in a simple, human-readable format.

---

## Overview

This project uses the XIAO nRF52840 microcontroller, Kailh Choc low profile switches, SOD-123 diodes, and a two part 3D printed case. The design is meant to be easy to assemble while still being fully custom.

---

## Images

All project images are located in the Images folder.

### CAD View

![CAD](Images/Screen%20Shot%202025-12-02%20at%209.17.59%20PM.png)

### PCB Layout

![PCB](Images/Screen%20Shot%202025-12-02%20at%208.39.47%20PM.png)

### Schematics

![Schematics](Images/Screen%20Shot%202025-12-02%20at%206.21.25%20PM.png)

---

## Bill of Materials

Below is the complete BOM used in the design.

### Resistors

* R1, R4: 806k, footprint R_0805_2012Metric, quantity 2
* R2, R5: 2M, footprint R_0805_2012Metric, quantity 2
* R3: R, footprint R_0805_2012Metric, quantity 1

### Diodes

* D1 through D42: Standard diode, footprint D_SOD-123, quantity 42

### Microcontrollers

* U1, U2: XIAO nRF52840 SMD modules, footprint modified-XIAO-nRF52840-SMD, quantity 2

### Switches

* SW1 through SW42: Kailh Choc style switches, footprint SW_choc_v1_1u, quantity 41

### Test Points

* TP1 through TP4: Test pads, footprint TestPoint_Pad_D2.0mm, quantity 4

---

## 3D Printed Parts

This keyboard uses two printed parts:

* Top case piece
* Bottom case piece

Both pieces should be printed with enough tolerance for the PCB to fit cleanly.

---

## Assembly Instructions

1. Solder all diodes first. They sit flat against the board and are easier to install before anything else.
2. Solder the resistors.
3. Install the Kailh Choc switches and solder them in place.
4. Attach both XIAO modules and make sure all pins are properly connected.
5. Inspect every solder joint and test the key matrix.
6. Place the PCB into the printed case parts and close everything up.

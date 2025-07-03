# 🧠 Fermi Semiconductors – VLSI Design Platform

Welcome to the official repository of **Fermi Semiconductors**, a chip design startup focused on building open-source, end-to-end VLSI design tools for digital, analog, and ASIC design flows.

This Streamlit-based web platform enables users to simulate, synthesize, layout, and generate GDSII files for their chip designs using industry-standard open-source EDA tools.

---

## 🚀 Features

- 📐 **Digital Design Flow**  
  Upload Verilog RTL, run simulation (Icarus Verilog), synthesis (Yosys), placement & routing (OpenROAD), and layout (Magic VLSI).

- ⚡ **Analog Design Flow**  
  Upload SPICE netlists, simulate using Ngspice, create layout with Magic, and run LVS/DRC with Netgen.

- 💾 **ASIC Design Flow**  
  Plan floorplan, integrate IPs, perform place & route, and generate final GDSII files.

- 📁 **Project Showcase**  
  Visualize existing chip design projects with netlists, simulation waveforms, and layouts.

- 🖥️ **Built with Streamlit**  
  Lightweight, interactive web interface accessible through your browser.

---

## 🛠 Tech Stack

| Component         | Technology         |
|------------------|--------------------|
| Frontend         | Streamlit          |
| Simulation       | Icarus Verilog, Ngspice |
| Synthesis        | Yosys              |
| Layout & DRC/LVS | Magic VLSI, Netgen |
| P&R + GDSII      | OpenROAD           |
| Visualization    | Matplotlib, SVG, PNG |
| Version Control  | Git + GitHub       |

---

## 📦 Installation & Running

### 🔧 Prerequisites

- Python 3.8+
- Pip
- EDA Tools Installed:
  - Icarus Verilog (`iverilog`)
  - Yosys
  - Magic VLSI
  - Ngspice
  - OpenROAD (optional)
  - Netgen

### 📥 Clone this Repository

```bash
git clone https://github.com/<your-username>/fermi-semiconductors.git
cd fermi-semiconductors

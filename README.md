# shear-force-and-bending-moment-for-Osdag-
Develop an algorithm to calculate the shear force and bending moment values of a simply supported beam subjected to a moving load.

# ⚙️ Shear Force and Bending Moment for Osdag

This project aims to develop an open-source Python algorithm that calculates **shear force** and **bending moment** values for a **simply supported beam under moving loads**. It is designed to be integrated into [**Osdag**](https://osdag.github.io/), an open-source software for the design of steel structures developed under the FOSSEE project, IIT Bombay.

---

## 🎯 Objective

To provide an accurate and extensible analytical backend that:
- Computes **support reactions**, **shear force**, and **bending moment** values for any point along a simply supported beam.
- Handles **multiple point loads** (including moving loads).
- Outputs results suitable for plotting SFD and BMD.
- Supports future integration with **Osdag UI** or **web interfaces**.

---

## 🛠️ Features

- ✅ Calculates reactions at supports (RA and RB).
- ✅ Evaluates shear force and bending moment at a specific location.
- ✅ Identifies maximum shear force and maximum bending moment.
- ✅ Structured, documented Python code for modular use.
- ✅ Includes a command-line interface for basic testing.
- 🔄 Designed for extension to include:
  - Uniformly distributed loads (UDL)
  - Moment loads
  - Continuous beams

---

## 📁 Project Structure


.
├── analyze_ss_movingload.py   # Core analysis logic with CLI interface
├── beam_animation.py          # Manim animation for educational visualization
├── README.md                  # Project documentation

🚀 How to Run
🔧 Prerequisites
Python 3.8+

Manim (only required for animations)

▶️ Run the Beam Analysis Script
bash
Copy
Edit
python analyze_ss_movingload.py

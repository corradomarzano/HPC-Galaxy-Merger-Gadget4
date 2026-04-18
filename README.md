# HPC Galaxy Merger Simulation with Gadget4 🌌

[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20HPC%20Cluster-red)](#)
[![Language](https://img.shields.io/badge/Language-C%20%7C%20Python%20%7C%20Bash-blue)](#)
[![Parallelization](https://img.shields.io/badge/Parallel-MPI%20%7C%20OpenMP-orange)](#)
[![Physics](https://img.shields.io/badge/Physics-SPH%20%26%20N--Body-green)](#)

This project focuses on simulating the collision and merging process of two galaxies using **Gadget4**, a massively parallel code for cosmological N-body/SPH simulations. The simulation accounts for Dark Matter dynamics, gas hydrodynamics, radiative cooling, and star formation.



## 🚀 Technical Overview

- **Code:** Gadget4 (C language, MPI/OpenMP parallelization).

- **Environment:** Run on an HPC cluster to manage high-resolution particle interaction.

- **Physics Modules:** - N-body dynamics for Dark Matter and Stars.

  - Smoothed Particle Hydrodynamics (SPH) for the gaseous component.

  - Star formation and cooling functions.



## 🛠️ Data Pipeline

The project implements a complete data analysis pipeline:

1. **Simulation:** Execution of the merger using specialized `.param` and `.config` setups.

2. **Preprocessing:** A Python-based extraction tool converts raw binary simulation outputs into structured `.csv` datasets for efficient handling.

3. **Analysis:** Statistical modeling of gas density histograms, mass conservation checks, and star formation rate (SFR) evolution.



## 📊 Key Results

- **Mass Conservation:** Verified total mass stability (Gas + Stars) across the cosmic time scale.

- **Morphological Evolution:** Successful visualization of tidal tails and the formation of a single merged entity.

- **Gas Dynamics:** Analysis of density saturation and feedback effects.



*(Qui inseriresti una delle immagini della pagina 9 o 11 della tua presentazione)*



## 📂 Repository Structure

- `config/`: Gadget4 configuration and parameter files.

- `scripts/`: Python tools for data processing and scientific plotting.

- `plots/`: High-resolution renders of the simulation.



---

**Author:** Corrado Marzano  

**Course:** Computing Methods for Astrophysics - Sapienza University of Rome

# HPC Galaxy Merger Simulation with Gadget4 🌌
[Leggi in Italiano (IT)](LEGGIMI.md) | [Read in English (EN)](README.md)

[![Platform](https://img.shields.io/badge/Platforms-Linux%20%7C%20HPC%20Cluster-red)](#)
[![Language](https://img.shields.io/badge/Languages-C%20%7C%20Python%20%7C%20Bash-blue)](#)
[![Parallelization](https://img.shields.io/badge/Parallelization-MPI%20%7C%20OpenMP-orange)](#)
[![Physics](https://img.shields.io/badge/Physics-SPH%20%26%20N--Body-green)](#)

This project focuses on simulating the collision and merging process of two galaxies using **Gadget4**, a massively parallel code for cosmological N-body/SPH simulations. The simulation accounts for Dark Matter dynamics, gas hydrodynamics, radiative cooling, and star formation.

## 📚 State of the Art & Introduction
Cosmological simulations are the primary tool for studying the large-scale structure and evolution of the universe. Following the **$\Lambda CDM$ model**, Dark Matter (DM) provides the main
gravitational framework for structure formation: it is a **massive** yet **non-interactive** type of matter, a characteristic to which it owes its *"dark"* nature, representing over 85% of the total matter in the universe.  

This project simulates a **Galaxy Merger**, focusing on the interplay between:
- **Dark Matter & Stars:** Modeled as collisionless particles (N-body dynamics).
- **Interstellar Gas:** Modeled using **Smoothed Particle Hydrodynamics (SPH)**.
- **Baryonic Physics:** Including radiative cooling and star formation (SFR).

  <figure>
  <p align="center">
    <img width="400" height="200" alt="cosmic web" src="https://github.com/user-attachments/assets/4aa4bef1-1e31-4ec7-9516-11dce0cc2316" />
  </p>
  <figcaption>
    <p align="center">
      <i> 
        <strong>The Cosmic Web:</strong> The large-scale structure of matter in the universe, formed by gravitational interactions.
      (<a href="https://bigthink.com/hard-science/cosmic-web/"><em>Image Reference</em></a>)
      </i>
    </p>
  </figcaption>
  </figure>

## 💻 HPC & Parallel Computing
The simulation was performed on the **Vera** (Sapienza) and **Leonardo** (CINECA) clusters.
- **HPC Infrastructure:** Leveraging massive parallelization to solve gravitational and hydrodynamical equations for thousands of particles.
- **Environment:** Development required managing dependencies (GSL, FFTW, HDF5) and specific shell environments (e.g., `devtoolset-8`).
- **Strategies:** Gadget4 uses a hybrid **MPI/Shared-Memory Use** approach. Each core is divided in two parts, the first one handles the physical computation through MPI (domain decomposition via TreePM), while the other solely intercedes in the communication requests between nodes (minimizing its latency and eliminating the synchronization losses) through Shared-Memory Use.

  <figure>
  <p align="center">
    <img width="350" height="350" alt="mpi_open_mp_tree" src="https://github.com/user-attachments/assets/bea7b9b5-ae7d-4bc4-be67-70d01fae912f" />
  </p>
  <figcaption>
    <p align="center">
      <i> 
        <strong>Gadget4 Parallelization Scheme.</strong><br>
        (<a href="https://arxiv.org/pdf/2010.03567"><em>Image Reference: Gadget4 Code Paper</em></a>)
      </i>
    </p>
  </figcaption>
</figure>


## 🛠️ Compile & Run the Code

### 1. Environment Setup
Load the required compiler and libraries:
```bash
scl enable devtoolset-8 bash
# Ensure MPI and HDF5 paths are exported
```

### 2. Compilation
Configure the code via Config.sh and the Makefile (edit the files as needed):
```bash
make
```

$Note_{(1)}$: Ensure that the compiler you use (and only that one) is set in the Makefile by uncommenting it (Default: SYSTYPE="Generic-gcc").  
$Note_{(2)}$: The **Initial Conditions (ICs)** for the simulation are provided by a *.dat* binary file (lagrangian ICs for each particle) and by a *param* text file containing runtime values, tuning parameters and cosmology setup (not relevant for a galaxy merger).

### 3. Execution
Run the simulation using MPI tasks with *N* processors:
```bash
mpirun -np N ./Gadget4 param.txt
```

*Note*: Specify the full paths to the parameters' file *param.txt* and to the mpi library for *mpirun*.

## 💾 Data Pipeline

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

**Author:** [Corrado Marzano](https://www.linkedin.com/in/corrado-marzano-7846353a8/)  

**Research Context:** Computing Methods for Astrophysics exam @ Sapienza University of Rome

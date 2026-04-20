# Simulazione HPC di Galaxy Merger con Gadget4 🌌
[Read in English (EN)](README.md) | [Leggi in Italiano (IT)](LEGGIMI.md)

[![Platform](https://img.shields.io/badge/Platforms-Linux%20%7C%20HPC%20Cluster-red)](#)
[![Language](https://img.shields.io/badge/Languages-C%20%7C%20Python%20%7C%20Bash-blue)](#)
[![Parallelization](https://img.shields.io/badge/Parallelization-MPI%20%7C%20OpenMP-orange)](#)
[![Physics](https://img.shields.io/badge/Physics-SPH%20%26%20N--Body-green)](#)

[cite_start]Questo progetto riguarda la simulazione del processo di collisione e fusione di due galassie utilizzando **Gadget4**, un codice a parallelizzazione massiva per simulazioni cosmologiche N-body/SPH[cite: 7]. [cite_start]La simulazione modella la dinamica della Materia Oscura, l'idrodinamica del gas, il raffreddamento radiativo e i processi di formazione stellare[cite: 12, 53].

## 🚀 Panoramica Tecnica
- [cite_start]**Codice:** Gadget4 (Linguaggio C, parallelizzazione tramite MPI/OpenMP)[cite: 9, 13].
- [cite_start]**Ambiente:** Eseguito su cluster HPC (Vera/Leonardo) per la gestione di interazioni particellari ad alta risoluzione[cite: 124, 128].
- [cite_start]**Moduli Fisici:** - Dinamica N-body per Materia Oscura e componenti stellari[cite: 8].
  - [cite_start]Smoothed Particle Hydrodynamics (SPH) per la componente gassosa[cite: 8].
  - [cite_start]Funzioni di raffreddamento (Cooling) e formazione stellare (Star Formation)[cite: 12, 53].

## 🛠️ Pipeline dei Dati
Il progetto implementa un workflow completo di analisi:
1. [cite_start]**Simulazione:** Configurazione ed esecuzione del merger tramite setup specifici di `.param` e `Config.sh`[cite: 11, 12].
2. [cite_start]**Preprocessing:** Strumento di estrazione in Python per convertire gli output binari (HDF5) in dataset strutturati `.csv` per un'elaborazione efficiente[cite: 17, 18].
3. [cite_start]**Analisi:** Modellazione statistica degli istogrammi di densità del gas, verifiche di conservazione della massa e analisi dell'evoluzione del tasso di formazione stellare (SFR)[cite: 1, 15].

## 📊 Risultati Principali
- [cite_start]**Conservazione della Massa:** Verifica della stabilità della massa totale (Gas + Stelle) su scala temporale cosmica[cite: 15, 52].
- [cite_start]**Evoluzione Morfologica:** Visualizzazione accurata delle code mareali e della formazione di un'unica entità ellittica post-merger[cite: 52, 53].
- [cite_start]**Dinamica del Gas:** Analisi dei fenomeni di saturazione della densità ed effetti di feedback[cite: 15].

## 📂 Struttura della Repository
- `configs/`: File di configurazione (`Config.sh`) e parametri di input (`.param`) di Gadget4.
- `scripts/`: Tool Python per il processamento dei dati e il plotting scientifico.
- `docs/`: Presentazione tecnica e documentazione del progetto.
- `plots/`: Render ad alta risoluzione della simulazione e istogrammi.

---
**Autore:** Corrado Marzano  
[cite_start]**Corso:** Metodi Computazionali per l'Astrofisica - Università degli Studi di Roma "La Sapienza" [cite: 1, 34]

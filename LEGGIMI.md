# Simulazione HPC di Galaxy Merger con Gadget4 🌌
[Read in English (EN)](README.md) | [Leggi in Italiano (IT)](LEGGIMI.md)

[![Platform](https://img.shields.io/badge/Platforms-Linux%20%7C%20HPC%20Cluster-red)](#)
[![Language](https://img.shields.io/badge/Languages-C%20%7C%20Python%20%7C%20Bash-blue)](#)
[![Parallelization](https://img.shields.io/badge/Parallelization-MPI%20%7C%20OpenMP-orange)](#)
[![Physics](https://img.shields.io/badge/Physics-SPH%20%26%20N--Body-green)](#)

Questo progetto si focalizza sulla simulazione del processo di collisione e fusione (merger) di due galassie utilizzando **Gadget4**, un codice a parallelizzazione massiva per simulazioni cosmologiche N-body/SPH. La simulazione tiene conto della dinamica della Materia Oscura, dell'idrodinamica del gas, del raffreddamento radiativo e della formazione stellare.

## 📚 Stato dell'Arte e Introduzione
Le simulazioni cosmologiche rappresentano lo strumento principale per studiare la struttura su larga scala e l'evoluzione dell'universo. Seguendo il **modello $\Lambda CDM$**, la Materia Oscura (DM) fornisce l'intelaiatura gravitazionale fondamentale per la formazione delle strutture: si tratta di un tipo di materia **massiva** ma **non interattiva**, caratteristica a cui deve la sua natura *"oscura"*, e rappresenta oltre l'85% della materia totale dell'universo.

Questo progetto simula la fusione di due galassie (**Galaxy Merger**), concentrandosi sull'interazione tra:
- **Materia Oscura e Stelle:** Modellati come particelle senza collisioni (dinamica N-body).
- **Gas Interstellare:** Modellato tramite **Smoothed Particle Hydrodynamics (SPH)**.
- **Fisica Barionica:** Include il raffreddamento radiativo e il tasso di formazione stellare (SFR).

  <figure>
  <p align="center">
    <img width="400" height="200" alt="cosmic web" src="https://github.com/user-attachments/assets/4aa4bef1-1e31-4ec7-9516-11dce0cc2316" />
  </p>
  <figcaption>
    <p align="center">
      <i> 
        <strong>La "Cosmic Web":</strong> La struttura su larga scala della materia nell'universo, formata dalle interazioni gravitazionali.
      (<a href="https://bigthink.com/hard-science/cosmic-web/"><em>Fonte Immagine</em></a>)
      </i>
    </p>
  </figcaption>
  </figure>

## 💻 Calcolo ad Alte Prestazioni (HPC) e Parallelizzazione
La simulazione è stata eseguita sui cluster **Vera** (Sapienza) e **Leonardo** (CINECA).
- **Infrastruttura HPC:** Utilizzo di parallelizzazione massiva per risolvere le equazioni gravitazionali e idrodinamiche per migliaia di particelle.
- **Ambiente:** Lo sviluppo ha richiesto la gestione di dipendenze (GSL, FFTW, HDF5) e specifici ambienti shell (es. `devtoolset-8`).
- **Strategie:** Gadget4 utilizza un approccio ibrido **MPI/Shared-Memory Use**. Ogni core è diviso in due parti: la prima gestisce il calcolo fisico tramite MPI (decomposizione del dominio via TreePM), mentre la seconda interviene esclusivamente nelle richieste di comunicazione tra i nodi (minimizzando la latenza ed eliminando le perdite di sincronizzazione) tramite Shared-Memory.

  <figure>
  <p align="center">
    <img width="350" height="350" alt="mpi_open_mp_tree" src="https://github.com/user-attachments/assets/bea7b9b5-ae7d-4bc4-be67-70d01fae912f" />
  </p>
  <figcaption>
    <p align="center">
      <i> 
        <strong>Schema di Parallelizzazione di Gadget4.</strong><br>
        (<a href="https://arxiv.org/pdf/2010.03567"><em>Fonte: Paper ufficiale di Gadget4</em></a>)
      </i>
    </p>
  </figcaption>
</figure>


## 🛠️ Compilazione ed Esecuzione del Codice

### 1. Setup dell'Ambiente
Scaricare il codice [Gadget4](https://wwwmpa.mpa-garching.mpg.de/gadget4/), quindi caricare il compilatore e le librerie richieste:
```bash
scl enable devtoolset-8 bash
# Assicurarsi che i path di MPI e HDF5 siano esportati
```
### 2. Compilazione
Configurare il codice tramite il file Config.sh e il Makefile (modificare i file secondo necessità):
```bash
make
```

$Nota_{(1)}$: Assicurarsi che il compilatore utilizzato (e solo quello) sia impostato nel Makefile decommentandolo (Default: SYSTYPE="Generic-gcc").  
$Nota_{(2)}$: Le **Condizioni Iniziali (ICs)** per la simulazione sono fornite da un file binario *.dat* (ICs lagrangiane per ogni particella) e da un file di testo *param* contenente i valori di runtime, i parametri di tuning e il setup cosmologico (non rilevante per un merger galattico).

### 3. Esecuzione
Eseguire la simulazione utilizzando task MPI con *N* processori:
```bash
mpirun -np N ./Gadget4 param.txt
```

*Nota*: Specificare i percorsi completi del file dei parametri *param.txt* e della libreria mpi per *mpirun*.

## 💾 Pipeline dei Dati

Il progetto implementa una pipeline completa di analisi dei dati:

1. **Preprocessing:** Uno strumento di estrazione basato su Python (`Data_Table_Acquirer.ipynb`) converte gli snapshot binari HDF5 in dataset strutturati `.csv` per una gestione efficiente.

2. **Analisi:** Il Post-processing e l'Analisi Dati sono eseguiti in `Data_Analysis.ipynb`. Questo include:
   - Valutazione del **tasso di formazione stellare (SFR)** e conseguente **deplezione del gas** (integrando un controllo sulla conservazione della massa per verificare l'accuratezza numerica del codice),
   - Generazione di **istogrammi di densità del gas**,
   - Valutazione dell'**efficienza computazionale** (misurata in termini di tempo di esecuzione) in funzione sia del numero di core utilizzati che della durata totale della simulazione.

*Nota - Installazione delle librerie richieste*:
   ```bash
   pip install -r scripts/requirements.txt
   ```

## 📊 Risultati Principali

### 1. Efficienza Computazionale e Scaling Parallelo

Le prestazioni della simulazione sono state sottoposte a benchmark sul cluster HPC per valutare lo **Strong Scaling** e la prevedibilità dell'esecuzione:

* **Speedup Parallelo:** I test indicano che la simulazione su 16 processori risulta circa **1.6 volte più lenta** rispetto a 32 processori, e **2.7 volte più lenta** rispetto a 48 processori. Questi dati dimostrano un'efficace ottimizzazione dell'architettura ibrida MPI/Shared-Memory, evidenziando significativi guadagni prestazionali circa lineari all'aumentare delle risorse computazionali utilizzate.
* **Linearità Temporale:** Per verificare la stabilità del codice e l'overhead di calcolo, è stato eseguito un test di consistenza. Quadruplicando il tempo fisico simulato, mantenendo il setup fisso a 48 processori, si è riscontrato un incremento perfettamente proporzionale (**4x**) del **tempo di calcolo (wall-clock time)**, con un'incertezza trascurabile di $\pm 0.12$ ore.
* **Significatività:** Tali risultati confermano che l'implementazione di Gadget4 sul cluster scala efficientemente e mantiene un costo computazionale prevedibile, requisito fondamentale per simulazioni astrofisiche su larga scala.

  <figure>
  <p align="center">
    <img width="500" height="500" src="plots/Simulation_Times.png" />
  </p>
</figure>

### 2. Evoluzione Morfologica e Analisi Visuale
La simulazione traccia la trasformazione dinamica del sistema su un arco temporale di **3.92 miliardi di anni (Gyrs)**, con una risoluzione temporale di **~69 milioni di anni (Myrs)** per snapshot (57 snapshot in totale). L'analisi visuale permette di distinguere tra l'impalcatura gravitazionale (Materia Oscura) e le componenti barioniche visibili.

- **Mappatura Visiva**
  - **Dinamica degli Aloni:** Rappresentazione degli $\color{blue}{\text{Aloni di Materia Oscura}}$ (in $\color{blue}{blu}$) che forniscono il potenziale gravitazionale.
  - **Componenti Barioniche:** Mappatura multi-colore delle strutture galattiche ($\color{red}{Rosso\text{: Bulges}}$; $\color{limegreen}{Verde\text{: Dischi}}$; $\color{cyan}{Ciano\text{: Gas}}$; $\color{yellow}{Giallo\text{: Stelle}}$). 

- **Fasi Chiave dell'Evoluzione:**

  - **Snapshot 1 (Stato Iniziale):** Le due galassie sono distinte e isolate, all'inizio della fase di avvicinamento.
  - **Snapshot 28 (Fase di Collisione):** Inizio della collisione. L'interazione porta alla formazione di evidenti code mareali e bracci di materia barionica.
  - **Snapshot 56 (Residuo del Merger):** Il processo di fusione del nucleo è completo. Sebbene il sistema sia nelle fasi finali di rilassamento dinamico, le due galassie originali si sono fuse in un'unica entità morfologica indistinguibile.
 
  <figure>
  <p align="center">
    <img width="1000" height="1000" src="plots/DM.png" />
  </p>
  <p align="center">
    <img width="1000" height="1000" src="plots/matter.png" />
  </p>
  <figcaption>
    <p>
      <i> 
        $\hspace{32 mm}$ Snapshot 1 $\hspace{62 mm}$ Snapshot 28 $\hspace{62 mm}$ Snapshot 56 <br>
      </i>
    </p>
  </figcaption>
</figure>

### 3. Dinamica della Formazione Stellare, Conservazione Numerica ed Evoluzione della Densità del Gas
La simulazione traccia accuratamente la conversione della componente gassosa in massa stellare, governata dai processi di formazione stellare e raffreddamento radiativo.
- **Tasso di Formazione Stellare (SFR):** L'analisi post-merger mostra un rapido picco iniziale di formazione stellare dovuto alla compressione del gas. Il processo raggiunge infine un **plateau asintotico**, indicando una saturazione. Questo comportamento è fisicamente coerente con l'assenza di **feedback stellare** nella specifica configurazione, che normalmente reintegrerebbe la riserva di gas o ne regolerebbe la formazione.
- **Test di Conservazione della Massa:** Come verifica cruciale della consistenza numerica del codice, la massa barionica totale ($M_{gas} + M_{stars}$) è stata monitorata durante l'intera scala temporale. Il trend perfettamente costante conferma l'affidabilità dell'integrazione e la corretta implementazione degli algoritmi di conversione.
  
  <figure>
  <p align="center">
    <img width="475" height="475" src="plots/Mass_Gas_Stars.png" />
  </p>
</figure>

- **Evoluzione della Densità del Gas:** Gli istogrammi della densità del gas in scala logaritmica rivelano la transizione dal mezzo interstellare diffuso alle regioni ad alta densità soggette a formazione stellare durante la fase centrale della collisione.

<figure>
  <p align="center">
    <img width="800" height="800" src="plots/Gas_Density_Histogram.png" />
  </p>
</figure>

## 🏁 Conclusioni
Il progetto dimostra come Gadget4 sia uno strumento **potente** e **altamente personalizzabile** per simulazioni cosmologiche. I punti chiave includono:

- **Accuratezza:** Il codice traccia con precisione il moto della materia oscura e barionica, misurando quantità fondamentali (densità, entropia, energia interna, ecc.) su scale cosmologiche, tenendo conto anche della formazione stellare e della funzione di raffreddamento.
- **Insight Fisici:** La simulazione evidenzia il ruolo cruciale del feedback stellare (o della sua assenza) nel rifornimento della componente gassosa durante il processo di formazione stellare.
- **Padronanza Tecnica:** Questo lavoro sottolinea l'importanza vitale dell'ottimizzazione del codice e delle strategie di parallelizzazione per ottenere risultati ad alte prestazioni nel calcolo scientifico.

## 📂 Struttura della Repository

- `config/`: File di configurazione e parametri di Gadget4.
- `scripts/`: Strumenti Python per l'elaborazione dei dati e il plotting scientifico.
- `plots/`: Render ad alta risoluzione della simulazione e grafici dell'analisi dei dati.

---

**Autore:** [Corrado Marzano](https://www.linkedin.com/in/corrado-marzano-7846353a8/)  

**Contesto di Ricerca:** Esame di Metodi Computazionali per l'Astrofisica @ Sapienza Università di Roma

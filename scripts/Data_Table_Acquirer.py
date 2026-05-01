import os
import csv
import h5py

############################################################
# Definition of functions used in the code

def perc(i, N):
  percf = i/float(N) * 100
  M = 20   # Number of spaces in the percentage bar

  print("[", end='')
  for j in range (1, M + 1):
    if percf >= (j/M)*100:
      print("=", end='')
    else:
      print(" ", end='')
  print("]", end=' ')
  print(f"Progress: {percf:3.2f}%", end="\r")

  return

############################################################

quantities = ['Coordinates','Density','ElectronAbundance','InternalEnergy','Masses','Metallicity','SmoothingLength','StarFormationRate','Velocities','StellarFormationTime']
part_types = ['PartType0','PartType1','PartType2','PartType3','PartType4']
components = ['gas','halo','disk','bulge','stars']

N = 56        # number of snapshots

path_in = r"data_hdf5\output_final" # Insert the path to the directory where your .hdf5 snapshot files, your simulation results' data, are stored
path_out = r""                       # Insert the path to the directory where you want to save your data in .csv format

perc(0, N+1)
for i in range (0,N+1):
    file_hdf5 = os.path.join(path_in, f'snapshot_{i:03d}.hdf5')  # Constructs the path to the single simulation's snapshot

    with h5py.File(file_hdf5, 'r') as f:
        for part in part_types:
            for quantity in quantities:
    ######################################################
                if (part + '/' + quantity) in f:
                    if (quantity=='Coordinates'):

                        data = f[part + '/' + quantity][:]

                        header = ['X', 'Y', 'Z']
                        rows = data.tolist()

                        path_temp = os.path.join(path_out, 'data', f'snapshot_{i:03d}', f'{components[part_types.index(part)]}')
                        if not os.path.exists(path_temp):
                            os.makedirs(path_temp)

                        with open(os.path.join(path_temp, 'Coordinates.csv'), 'w', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(header)
                            writer.writerows(rows)

                    elif (quantity=='Velocities'):

                        data = f[part + '/' + quantity][:]

                        header = ['X', 'Y', 'Z']
                        rows = data.tolist()

                        path_temp = os.path.join(path_out, 'data', f'snapshot_{i:03d}', f'{components[part_types.index(part)]}')
                        if not os.path.exists(path_temp):
                            os.makedirs(path_temp)
                        
                        with open(os.path.join(path_temp, 'Velocities.csv'), 'w', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(header)
                            writer.writerows(rows)

                    else:
                        data = f[part + '/' + quantity][:]
                        header = [quantity]

                        path_temp = os.path.join(path_out, 'data', f'snapshot_{i:03d}', f'{components[part_types.index(part)]}')
                        if not os.path.exists(path_temp):
                            os.makedirs(path_temp)

                        with open(os.path.join(path_temp, f'{quantity}.csv'), 'w', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(header)
                            for value in data:
                                writer.writerow([value])
    ######################################################

    perc(i+1, N+1)

print('\nDone!')
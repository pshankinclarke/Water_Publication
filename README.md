# Water Publication Backup
This repository stores the codebase,database, and experimental photographs for the "Effects of Wildfires and Ash Leaching on Stream Chemistry
in the Santa Ynez Mountains of Southern California" Water journal publication. The following files and directories are contained in this repository :

- CN_analyzer_measurement_photos: photographs of measurements taken during the CN combustion analysis
- waterCodebase : codebase and corresponding files for water publication 
  - CN_Measurements_Original.csv : CN combustion data before correction (identical to CN_Combustion.csv)
  - CN_corrections.py : script that applies correction to data, finds detection limit, and creates error bars for CN combustion data
  - C_corrections.csv : C data after correction
  - EL_Cap_Rain_Data.csv : Rain gauge data from El Capitan
  - FiguresAndCorrections.ipynb : Notebook that creates figures (not figure 1) + corrections used in the publication
  - LeachingData.py : script that takes stream water and ash leaching data and exports it as pandas dataframes
  - N_corrections.csv : C data after correction
  - RS_RAIN_DATA.csv : RattleSnake canyon rain data
- Ash_Leaching.csv : data for ash leaching experiment
- CN_Combustion.csv : data for CN combustion data before correction (identical to CN_Measurements_Original.csv)
- Creek_Water_Cations.csv : creek water major cation data from leaching experiment 
- Normalized_Creek_Water_Cations.csv : creek water major cation data normalized to baseline
- RattleSnake_Creek_Water_Cations.csv : cation data from RattleSnake canyon


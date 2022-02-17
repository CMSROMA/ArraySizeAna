

Clone the repository in a new folder:
```
git clone git@github.com:CMSROMA/ArraySizeAna.git
cd ArraySizeAna
```

Raw data files are available in the "data" folder.
For the moment, the file name is just the array number. Es.
```
796.txt	799.txt	800.txt	803.txt	805.txt	809.txt
```
Note: It should be changed in future with unique run number and date.

Run analysis on all raw data available:
```
python3 runAll.py --inputdir data/
```

Several .csv files are created in the current directory. Es.:
```
796.csv	799.csv	800.csv	803.csv	805.csv	809.csv
```

Merge all files into a single csv file:
```
cat *.csv > all.csv
```

The final file will look like this:
```
796,56.243,0.011,0.052,0.057,0.014,0.017,0.022,56.298,56.239,0.004,56.268,0.016,0.044,0.125,0.014,0.043,0.045,51.508,51.431,0.014,51.47,0.04,0.08,0.019,3.368,3.333,0.002,3.333,0.019
799,56.286,0.002,0.059,0.041,0.014,0.009,0.017,56.344,56.286,0.003,56.315,0.015,0.052,0.032,0.014,0.012,0.018,51.478,51.442,0.006,51.46,0.014,0.08,0.016,3.394,3.358,0.002,3.358,0.016
800,56.252,0.017,0.125,0.103,0.034,0.03,0.045,56.352,56.232,0.009,56.292,0.033,0.079,0.081,0.027,0.031,0.041,51.48,51.395,0.012,51.438,0.029,0.12,0.024,3.352,3.292,0.002,3.292,0.024
803,56.23,0.036,0.124,0.076,0.037,0.019,0.042,56.351,56.249,0.008,56.3,0.031,0.09,0.074,0.028,0.023,0.036,51.39,51.305,0.011,51.347,0.026,0.104,0.023,3.389,3.311,0.002,3.311,0.023
805,56.296,0.006,0.022,0.049,0.007,0.015,0.017,56.348,56.304,0.003,56.326,0.016,0.158,0.104,0.053,0.031,0.061,51.856,51.71,0.019,51.783,0.048,0.168,0.043,3.491,3.4,0.004,3.4,0.043
809,56.279,0.008,0.068,0.1,0.021,0.029,0.036,56.346,56.264,0.007,56.305,0.027,0.213,0.122,0.083,0.034,0.09,51.852,51.672,0.027,51.762,0.068,0.165,0.037,3.402,3.281,0.003,3.281,0.037
```

where the column names are defined/described inside the "Dimensions.py" code and they are:
```
l_results_names = ["array",
                       "L_bar_mu","L_bar_std",
                       "L_maxVar_LS","L_maxVar_LN","L_std_LS","L_std_LN","L_std_tot","L_max","L_mean","L_mean_std","L_mean_mitu","L_std_mitu",
                       "W_maxVar_LO","W_maxVar_LE","W_std_LO","W_std_LE","W_std_tot","W_max","W_mean","W_mean_std","W_mean_mitu","W_std_mitu",
                       "T_maxVar_FS","T_std_FS","T_max","T_mean","T_mean_std","T_mean_mitu","T_std_mitu"]
```


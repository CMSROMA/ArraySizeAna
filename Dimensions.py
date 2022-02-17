## ROOT stuff
import ROOT as R
R.gROOT.SetBatch(1)
#set the tdr style
import tdrstyle
tdrstyle.setTDRStyle()

## Python stuff
from array import array
import os
import math as mt
import numpy as np
import re
import argparse
from collections import defaultdict
import pandas as pd
import sys
import csv

#--- Options

parser = argparse.ArgumentParser(usage="python3 Dimensions.py --data data/809 --array 809")
parser.add_argument('--data',dest='data',required=True)
parser.add_argument('--array',dest='array',required=True,type=int)
#parser.add_argument('--type',dest='type',required=True,type=int)
args = parser.parse_args()

'''
##--- Tolerances and ranges
length_m = 56.30 #mm
e_low_length = 0.02 #mm
e_high_length = 0.02 #mm
length_min = 56.2 #for plot only
length_max = 56.4 #for plot only
length_bin = 40 #for plot only

width_m = 51.50 #mm
e_low_width = 0.10 #mm
e_high_width = 0.10 #mm
width_min = 51.10 #for plot only
width_max = 51.90 #for plot only
width_bin = 80 #for plot only

thickness_m = 0. #mm
e_low_thickness = 0. #mm
e_high_thickness = 0. #mm
thickness_min = 0. #for plot only
thickness_max = 0. #for plot only
thickness_bin = 0. #for plot only

if(args.type==1):
    thickness_m = 4.05 #mm
    e_low_thickness = 0.10 #mm
    e_high_thickness = 0.10 #mm
    thickness_min = 3.65 #for plot only
    thickness_max = 4.45 #for plot only
    thickness_bin = 80 #for plot only

if(args.type==2):
    thickness_m = 3.30 #mm
    e_low_thickness = 0.10 #mm
    e_high_thickness = 0.10 #mm
    thickness_min = 2.90 #for plot only
    thickness_max = 3.70 #for plot only
    thickness_bin = 80 #for plot only

if(args.type==3):
    thickness_m = 2.70 #mm
    e_low_thickness = 0.10 #mm
    e_high_thickness = 0.10 #mm
    thickness_min = 2.30 #for plot only
    thickness_max = 3.10 #for plot only
    thickness_bin = 80 #for plot only
'''

##--- Read data

df_LS = pd.DataFrame(columns=['X', 'Y', 'Z'])
counter_LS = 0

df_LN = pd.DataFrame(columns=['X', 'Y', 'Z'])
counter_LN = 0

df_FS = pd.DataFrame(columns=['X', 'Y', 'Z'])
counter_FS = 0

df_LO = pd.DataFrame(columns=['X', 'Y', 'Z'])
counter_LO = 0

df_LE = pd.DataFrame(columns=['X', 'Y', 'Z'])
counter_LE = 0

for line in open(args.data,errors='ignore'):
    line = line.rstrip()
    #line.strip()
    #print (line)
    splitline = line.split()
    n_elements = len(splitline)
    if(n_elements<5):
        continue    
    
    n = x = y = z = 0
    n = splitline[0]
    x = splitline[1]
    y = splitline[2]
    z = splitline[3]

    side = splitline[0]

    #if(side=="32_LS" or side=="32_LN" or side=="32_FS" or side=="32_LO" or side=="32_LE"):
    if( ("_LS" in side) or ("_LN" in side) or ("_FS" in side) or ("_LO" in side) or ("_LE" in side) ):
        n = splitline[1]
        x = float(splitline[2])
        y = float(splitline[3])
        z = float(splitline[4])

    if("_LS" in side):
        counter_LS = 1
    if("_LN" in side):
        counter_LN = 1
    if("_FS" in side):
        counter_FS = 1
    if("_LO" in side):
        counter_LO = 1
    if("_LE" in side):
        counter_LE = 1

    if(counter_LS>0 and counter_LS<27):
        values_to_add = {'X': x, 'Y': y, 'Z': z}
        row_to_add = pd.Series(values_to_add, name=n)
        df_LS = df_LS.append(row_to_add)
        counter_LS = counter_LS + 1

    if(counter_LN>0 and counter_LN<27):
        values_to_add = {'X': x, 'Y': y, 'Z': z}
        row_to_add = pd.Series(values_to_add, name=n)
        df_LN = df_LN.append(row_to_add)
        counter_LN = counter_LN + 1

    if(counter_FS>0 and counter_FS<113):
        values_to_add = {'X': x, 'Y': y, 'Z': z}
        row_to_add = pd.Series(values_to_add, name=n)
        df_FS = df_FS.append(row_to_add)
        counter_FS = counter_FS + 1

    if(counter_LO>0 and counter_LO<12):
        values_to_add = {'X': x, 'Y': y, 'Z': z}
        row_to_add = pd.Series(values_to_add, name=n)
        df_LO = df_LO.append(row_to_add)
        counter_LO = counter_LO + 1

    if(counter_LE>0 and counter_LE<12):
        values_to_add = {'X': x, 'Y': y, 'Z': z}
        row_to_add = pd.Series(values_to_add, name=n)
        df_LE = df_LE.append(row_to_add)
        counter_LE = counter_LE + 1
        
df_LS = df_LS.astype({"X": float, "Y": float, "Z": float})
df_LN = df_LN.astype({"X": float, "Y": float, "Z": float})
df_FS = df_FS.astype({"X": float, "Y": float, "Z": float})
df_LO = df_LO.astype({"X": float, "Y": float, "Z": float})
df_LE = df_LE.astype({"X": float, "Y": float, "Z": float})

#print (df_LS.dtypes)
#print (df_LN.dtypes)
#print (df_FS.dtypes)
#print (df_LO.dtypes)
#print (df_LE.dtypes)

#print (df_LS)
#print (df_LN)
#print (df_FS)
#print (df_LO)
#print (df_LE)

# ==============
# === Length ===
# ==============

#1 19=20-1 even 
#2 20=22-2 odd
#3 17=20-3 even
#4 18=22-4 odd
#...
#...

l_lenght = []

for point in range(1,21):
    y_LS = float(df_LS.loc[str(point)]['Y'])
    if (point % 2) == 0: #even
        y_LN = float(df_LN.loc[str(22-point)]['Y'])        
    else: #odd
        y_LN = float(df_LN.loc[str(20-point)]['Y'])
    length = y_LN - y_LS
    l_lenght.append(length)
    #print ("point, y_LS, y_LN, length :",point, y_LS, y_LN, length)

np_length_all = np.asarray(l_lenght)
np_length = np.mean(np_length_all.reshape(-1, 2), axis=1)
np_length = np_length.round(3)

length_mean = np_length.mean().round(3)
length_std = np_length.std().round(3)

#n_length_outOfPlotRange = np.count_nonzero( (np_length < length_min) | (np_length > length_max) )
#n_length_outOfTolerance = np.count_nonzero( (np_length < length_m-e_low_length) | (np_length > length_m+e_high_length) )
#print (n_length_outOfPlotRange, n_length_outOfTolerance)

#print (np_length_all.size)
#print (np_length.size)
#print (np_length_all)
#print (np_length_all.reshape(-1, 2))
#print (np_length)

'''
h_length = R.TH1F("h_length","h_length",length_bin,length_min,length_max)
h_length.SetNdivisions(505)
h_length.GetXaxis().SetTitle("Bar length [mm]")
for bar in range(0,np_length.size):
    #print (np_length[bar])
    h_length.Fill(np_length[bar])

l_mid = R.TLine(length_m,0.,length_m,h_length.GetMaximum())
l_low = R.TLine(length_m-e_low_length,0.,length_m-e_low_length,h_length.GetMaximum())
l_high = R.TLine(length_m+e_high_length,0.,length_m+e_high_length,h_length.GetMaximum())
l_mid.SetLineStyle(2)
l_mid.SetLineColor(2)
l_low.SetLineColor(2)
l_high.SetLineColor(2)

pt = R.TPaveText(0.67,0.63,0.92,0.88,"ndc")
pt.SetFillColor(0)
pt.SetBorderSize(1)
pt.AddText("Array "+str(args.array))
pt.AddText("Mean = "+str(length_mean)+" mm")
pt.AddText(" #sigma = "+str(length_std)+ " mm")
#pt.AddText("N. bars out of plot range = "+str(n_length_outOfPlotRange))
#pt.AddText("N. bars out of tolerance = "+str(n_length_outOfTolerance))

c1 = R.TCanvas()
h_length.Draw()
l_mid.Draw()
l_low.Draw()
l_high.Draw()
pt.Draw()

#c1.SaveAs("array_"+str(args.array)+"_length_bar.pdf")
'''

# === Max. Y variation on north/sud side (length)

max_y_LS = np.amax(df_LS["Y"].to_numpy())
min_y_LS = np.amin(df_LS["Y"].to_numpy())
delta_y_LS = (max_y_LS - min_y_LS).round(3)

max_y_LN = np.amax(df_LN["Y"].to_numpy())
min_y_LN = np.amin(df_LN["Y"].to_numpy())
delta_y_LN = (max_y_LN - min_y_LN).round(3)

# === Mean on Y on north/sud side (length)

mean_y_LS = (df_LS["Y"].to_numpy()).mean().round(3)
mean_y_LN = (df_LN["Y"].to_numpy()).mean().round(3)

# === Spread on Y on north/sud side (length)

std_y_LS = (df_LS["Y"].to_numpy()).std().round(3)
std_y_LN = (df_LN["Y"].to_numpy()).std().round(3)
std_deltay = round(mt.sqrt(std_y_LS**2+std_y_LN**2),3)

# === Max. array size along Y (length)

array_length_max = (max_y_LN - min_y_LS).round(3)
'''
array_length_max_pass = 1

if (array_length_max > length_m+e_low_length or array_length_max < length_m-e_low_length ):
    array_length_max_pass = 0
'''

# === Average array size along Y (length)

array_length_mean = (mean_y_LN - mean_y_LS).round(3)
array_length_mean_std = round(mt.sqrt( (std_y_LS/ mt.sqrt((df_LS["Y"].to_numpy()).size) )**2
                               + (std_y_LN/mt.sqrt((df_LN["Y"].to_numpy()).size) )**2  ) , 3)
'''
array_length_mean_pass = 1
if (array_length_mean > length_m+e_low_length or array_length_mean < length_m-e_low_length ):
    array_length_mean_pass = 0
'''

# === Simulating Mitutoyo (length)

np_mitutoyo_length_LS = max_y_LN - df_LS["Y"].to_numpy()
np_mitutoyo_length_LN = df_LN["Y"].to_numpy() - min_y_LS
np_mitutoyo_length = np_mitutoyo_length_LS
np_mitutoyo_length = np.concatenate([np_mitutoyo_length,np_mitutoyo_length_LN])

mitutoyo_array_length_mean = (np_mitutoyo_length.mean()).round(3)
mitutoyo_array_length_std = (np_mitutoyo_length.std()).round(3)
'''
mitutoyo_array_length_mean_pass = 1
if (mitutoyo_array_length_mean > length_m+e_low_length or mitutoyo_array_length_mean < length_m-e_low_length ):
    mitutoyo_array_length_mean_pass = 0
'''

# =============
# === Width ===
# =============

# === Max. X variation on "ovest"/east side (width)

max_x_LO = np.amax(df_LO["X"].to_numpy())
min_x_LO = np.amin(df_LO["X"].to_numpy())
delta_x_LO = (max_x_LO - min_x_LO).round(3)

max_x_LE = np.amax(df_LE["X"].to_numpy())
min_x_LE = np.amin(df_LE["X"].to_numpy())
delta_x_LE = (max_x_LE - min_x_LE).round(3)

# === Mean on X on "ovest"/east side (width)

mean_x_LO = (df_LO["X"].to_numpy()).mean().round(3)
mean_x_LE = (df_LE["X"].to_numpy()).mean().round(3)

# === Std. dev. on X on "ovest"/east side (width)

std_x_LO = (df_LO["X"].to_numpy()).std().round(3)
std_x_LE = (df_LE["X"].to_numpy()).std().round(3)
std_deltax = round(mt.sqrt(std_x_LO**2+std_x_LE**2),3)

# === Max. array size along X (width)

array_width_max = (max_x_LE - min_x_LO).round(3)
'''
array_width_max_pass = 1
if (array_width_max > width_m+e_low_width or array_width_max < width_m-e_low_width):
    array_width_max_pass = 0
'''
# === Average array size along X (width)

array_width_mean = (mean_x_LE - mean_x_LO).round(3)
array_width_mean_std = round(mt.sqrt( (std_x_LO/mt.sqrt((df_LO["X"].to_numpy()).size))**2
                               + (std_x_LE/mt.sqrt((df_LE["X"].to_numpy()).size))**2  ) , 3)
'''
array_width_mean_pass = 1
if (array_width_mean > width_m+e_low_width or array_width_mean < width_m-e_low_width ):
    array_width_mean_pass = 0
'''
# === Simulating Mitutoyo (width)

np_mitutoyo_width_LO = max_x_LE - df_LO["X"].to_numpy()
np_mitutoyo_width_LE = df_LE["X"].to_numpy() - min_x_LO
np_mitutoyo_width = np_mitutoyo_width_LO
np_mitutoyo_width = np.concatenate([np_mitutoyo_width,np_mitutoyo_width_LE])

mitutoyo_array_width_mean = (np_mitutoyo_width.mean()).round(3)
mitutoyo_array_width_std = (np_mitutoyo_width.std()).round(3)
'''
mitutoyo_array_width_mean_pass = 1
if (mitutoyo_array_width_mean > width_m+e_low_width or mitutoyo_array_width_mean < width_m-e_low_width ):
    mitutoyo_array_width_mean_pass = 0
'''    
# =================
# === Thickness ===
# =================

np_thickness = df_FS["Z"].to_numpy()
np_thickness = np_thickness.round(3)

thickness_mean = np_thickness.mean().round(3)
thickness_std = np_thickness.std().round(3)

#n_thickness_outOfPlotRange = np.count_nonzero( (np_thickness < thickness_min) | (np_thickness > thickness_max) )
#n_thickness_outOfTolerance = np.count_nonzero( (np_thickness < thickness_m-e_low_thickness) | (np_thickness > thickness_m+e_high_thickness) )

'''
h_thickness = R.TH1F("h_thickness","h_thickness",thickness_bin,thickness_min,thickness_max)
h_thickness.SetNdivisions(505)
h_thickness.GetXaxis().SetTitle("Array thickness [mm]")
for bar in range(0,np_thickness.size):
    #print (np_thickness[bar])
    h_thickness.Fill(np_thickness[bar])

l_mid = R.TLine(thickness_m,0.,thickness_m,h_thickness.GetMaximum())
l_low = R.TLine(thickness_m-e_low_thickness,0.,thickness_m-e_low_thickness,h_thickness.GetMaximum())
l_high = R.TLine(thickness_m+e_high_thickness,0.,thickness_m+e_high_thickness,h_thickness.GetMaximum())
l_mid.SetLineStyle(2)
l_mid.SetLineColor(2)
l_low.SetLineColor(2)
l_high.SetLineColor(2)

pt = R.TPaveText(0.67,0.63,0.92,0.88,"ndc")
pt.SetFillColor(0)
pt.SetBorderSize(1)
pt.AddText("Array "+str(args.array))
pt.AddText("Mean = "+str(thickness_mean)+" mm")
pt.AddText(" #sigma = "+str(thickness_std)+ " mm")
#pt.AddText("N. meas. out of plot range = "+str(n_thickness_outOfPlotRange))
#pt.AddText("N. meas. out of tolerance = "+str(n_thickness_outOfTolerance))

c1 = R.TCanvas()
h_thickness.Draw()
l_mid.Draw()
l_low.Draw()
l_high.Draw()
pt.Draw()

#c1.SaveAs("array_"+str(args.array)+"_thickness_array.pdf")
'''

# === Max. Z variation on front side (thickness)

max_z_FS = np.amax(df_FS["Z"].to_numpy())
min_z_FS = np.amin(df_FS["Z"].to_numpy())
delta_z_FS = (max_z_FS - min_z_FS).round(3)

# === Mean on Z on front side (thickness)

mean_z_FS = (df_FS["Z"].to_numpy()).mean().round(3)

# === Std. dev. on Z on front side (thickness)

std_z_FS = (df_FS["Z"].to_numpy()).std().round(3)

# === Max. array size along Z (thickness)

array_thickness_max = (max_z_FS - 0).round(3)
'''
array_thickness_max_pass = 1
if (array_thickness_max > thickness_m+e_low_thickness or array_thickness_max < thickness_m-e_low_thickness):
    array_thickness_max_pass = 0
'''
# === Average array size along Z (thickness)

array_thickness_mean = (mean_z_FS - 0).round(3)
array_thickness_mean_std = round( std_z_FS / mt.sqrt( (df_FS["Z"].to_numpy()).size ), 3 )
'''
array_thickness_mean_pass = 1
if (array_thickness_mean > thickness_m+e_low_thickness or array_thickness_mean < thickness_m-e_low_thickness ):
    array_thickness_mean_pass = 0
'''
# === Simulating Mitutoyo (thickness)

np_mitutoyo_thickness = df_FS["Z"].to_numpy()

mitutoyo_array_thickness_mean = (np_mitutoyo_thickness.mean()).round(3)
mitutoyo_array_thickness_std = (np_mitutoyo_thickness.std()).round(3)
'''
mitutoyo_array_thickness_mean_pass = 1
if (mitutoyo_array_thickness_mean > thickness_m+e_low_thickness or mitutoyo_array_thickness_mean < thickness_m-e_low_thickness ):
    mitutoyo_array_thickness_mean_pass = 0
'''    
# =================
# === Final results
# =================

print ("")

print ("===")
print ("Array "+ str(args.array))

print ("--- Length ---")
print ("* Bar Length: "+"Mean = "
           +str(length_mean)+" mm"
           +" , Std. dev. = "+str(length_std)+ " mm"
           )
#+" , N. bars out of tolerance = "+str(n_length_outOfTolerance)+ " / "+str(np_length.size)
print ("* Max. Y variation low-high (LS) = "+ str(delta_y_LS)+" mm")
print ("* Max. Y variation low-high (LN) = "+ str(delta_y_LN)+" mm")
print ("* Std. dev. on Y (LS) = "+ str(std_y_LS)+" mm")
print ("* Std. dev. on Y (LN) = "+ str(std_y_LN)+" mm")
print ("* Std. dev. on DeltaY (LN-LS) [sum in quadrature] = "+ str(std_deltay)+" mm")
print ("* Max. array size along Y (LN - LS): length = "+ str(array_length_max)+" mm")
#           + " --> Pass criteria = "+ str(array_length_max_pass) )
print ("* Mean array size along Y (LN - LS): length +/- std. dev. on mean = ("+ str(array_length_mean)
           + " +/- "+ str(array_length_mean_std) + ") mm")
#           + " --> Pass criteria = "+ str(array_length_mean_pass) )
print ("* Mitutoyo Simulation - Length +/- std. dev. = ("+ str(mitutoyo_array_length_mean)
           + " +/- "+ str(mitutoyo_array_length_std) + ") mm")
#           + " --> Pass criteria = "+ str(mitutoyo_array_length_mean_pass) )

print ("--- Width ---")
print ("* Max. X variation low-high (LO) = "+ str(delta_x_LO)+" mm")
print ("* Max. X variation low-high (LE) = "+ str(delta_x_LE)+" mm")
print ("* Std. dev. on X (LO) = "+ str(std_x_LO)+" mm")
print ("* Std. dev. on X (LE) = "+ str(std_x_LE)+" mm")
print ("* Std. dev. on DeltaX (LE-LO) [sum in quadrature] = "+ str(std_deltax)+" mm")
print ("* Max. array size along X (LE - LO): width = "+ str(array_width_max)+" mm")
#           + " --> Pass criteria = "+ str(array_width_max_pass) )
print ("* Mean array size along X (LE - LO): width +/- std. dev. on mean = ("+ str(array_width_mean)
           + " +/- "+ str(array_width_mean_std) + ") mm")
#           + " --> Pass criteria = "+ str(array_width_mean_pass) )
print ("* Mitutoyo Simulation - Width +/- std. dev. = ("+ str(mitutoyo_array_width_mean)
           + " +/- "+ str(mitutoyo_array_width_std) + ") mm")
#           + " --> Pass criteria = "+ str(mitutoyo_array_width_mean_pass) )

print ("--- Thickness ---")
#print ("* Array Thickness: "+"Mean = "
#           +str(thickness_mean)+" mm"
#           +" , Std. dev. = "+str(thickness_std)+ " mm"
#           +" , N. meas. out of tolerance = "+str(n_thickness_outOfTolerance)+ " / "+str(np_thickness.size)
#           )
print ("* Max. Z variation low-high (FS) = "+ str(delta_z_FS)+" mm")
print ("* Std. dev. on Z (FS) = "+ str(std_z_FS)+" mm")
print ("* Max. array size along Z (FS - 0): thickness = "+ str(array_thickness_max)+" mm")
#           + " --> Pass criteria = "+ str(array_thickness_max_pass) )
print ("* Mean array size along Z (FS - 0): thickness +/- std. dev. on mean = ("+ str(array_thickness_mean)
           + " +/- "+ str(array_thickness_mean_std) + ") mm")
#           + " --> Pass criteria = "+ str(array_thickness_mean_pass) )
print ("* Mitutoyo Simulation - Thickness +/- std. dev. = ("+ str(mitutoyo_array_thickness_mean)
           + " +/- "+ str(mitutoyo_array_thickness_std) + ") mm")
#           + " --> Pass criteria = "+ str(mitutoyo_array_thickness_mean_pass) )

print ("===")

l_results_names = ["array",
                       "L_bar_mu","L_bar_std",
                       "L_maxVar_LS","L_maxVar_LN","L_std_LS","L_std_LN","L_std_tot","L_max","L_mean","L_mean_std","L_mean_mitu","L_std_mitu",
                       "W_maxVar_LO","W_maxVar_LE","W_std_LO","W_std_LE","W_std_tot","W_max","W_mean","W_mean_std","W_mean_mitu","W_std_mitu",
                       "T_maxVar_FS","T_std_FS","T_max","T_mean","T_mean_std","T_mean_mitu","T_std_mitu"]
l_results = [args.array,
                 length_mean,length_std,
                 delta_y_LS,delta_y_LN,std_y_LS,std_y_LN,std_deltay,array_length_max,array_length_mean,array_length_mean_std,mitutoyo_array_length_mean,mitutoyo_array_length_std,
                 delta_x_LO,delta_x_LE,std_x_LO,std_x_LE,std_deltax,array_width_max,array_width_mean,array_width_mean_std,mitutoyo_array_width_mean,mitutoyo_array_width_std,
                 delta_z_FS,std_z_FS,array_thickness_max,array_thickness_mean,array_thickness_mean_std,mitutoyo_array_thickness_mean,mitutoyo_array_thickness_std]

with open(str(args.array)+".csv", "w") as file:
    writer = csv.writer(file, delimiter=',')
    #writer.writerow(l_results_names)
    writer.writerow(l_results)










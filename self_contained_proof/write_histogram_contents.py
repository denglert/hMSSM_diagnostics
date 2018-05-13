#!/usr/bin/env python

import ROOT

hMSSM_ROOT_histo_path = "./hMSSM_13TeV.root"

tf = ROOT.TFile(hMSSM_ROOT_histo_path)
xs_gg_H_histo = tf.Get('xs_gg_H')


mA = 250.0
tanbs = [1.01, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]


out_file_path = "duplicated_pairs.dat"
out_file = open(out_file_path, "w")

header = "mA tanb xs_gg_H\n"
out_file.write(header)

for tanb in tanbs:
    
    global_bin = xs_gg_H_histo.FindBin(mA, tanb)
    xs_gg_H = xs_gg_H_histo.GetBinContent(global_bin)

    row = "{} {} {}\n".format(mA, tanb, xs_gg_H)
    out_file.write(row)

#!/usr/bin/env python

import ROOT
from ROOT import TCanvas

hMSSM_ROOT_histo_path = "./data/root/hMSSM_13TeV.root"

tf = ROOT.TFile(hMSSM_ROOT_histo_path)

xs_gg_H = tf.Get('xs_gg_H')
m_H = tf.Get('m_H')
Gamma_H = tf.Get('width_H')
br_H_hh = tf.Get('br_H_hh')
br_h_tautau = tf.Get('br_h_tautau')
br_h_bb = tf.Get('br_h_bb')
br_h_gamgam = tf.Get('br_h_gamgam')


def save_binning(histo, out_file_path):

    ax_x = histo.GetXaxis();
    ax_y = histo.GetYaxis();
    
    bins_x = ax_x.GetXbins()
    bins_y = ax_y.GetXbins()
    
    bins_x_n = bins_x.GetSize()
    bins_y_n = bins_y.GetSize()
    
    x_binning = []
    y_binning = []
    
    for i in range(bins_x_n):
        bin = bins_x.GetAt(i)
        x_binning.append(bin)
    
    for i in range(bins_y_n):
        bin = bins_y.GetAt(i)
        y_binning.append(bin)
    
    with open(out_file_path, "w") as f_out:
        f_out.write("mA binning:\n")
        f_out.write("{}\n".format(x_binning))
        f_out.write("tanb binning:\n")
        f_out.write("{}\n".format(y_binning))


def plot_histo(histo, out_fig_path):
    
    canv = TCanvas("canv", ";;", 1024, 768)
    histo.GetXaxis().SetTitle("m_{A} [GeV]")
    histo.GetYaxis().SetTitle(r"\tan #beta")
    
    histo.GetXaxis().SetRangeUser(150.0, 600.0)
    histo.GetYaxis().SetRangeUser(0.8, 5.0)
    histo.Draw("COLZ")
    canv.SaveAs(out_fig_path)


def write_histo_contents(h, out_file_path):

    n_x = h.GetNbinsX()
    n_y = h.GetNbinsY()

    ax_x = h.GetXaxis();
    ax_y = h.GetYaxis();
    
    bins_x = ax_x.GetXbins()
    bins_y = ax_y.GetXbins()

    f_out = open(out_file_path, 'w')

    x_nbins, x_min,x_max = ax_x.GetNbins(), ax_x.GetXmin(), ax_x.GetXmax()
    y_nbins, y_min,y_max = ax_y.GetNbins(), ax_y.GetXmin(), ax_y.GetXmax()

    print("x: [{} - {}] nBins: {}".format(x_min, x_max, x_nbins))
    print("y: [{} - {}] nBins: {}".format(y_min, y_max, y_nbins))

    for i in range(n_x):
        for j in range(n_y):

            bin_x = (bins_x.GetAt(i)+bins_x.GetAt(i+1))/2.0
            bin_y = (bins_y.GetAt(j)+bins_y.GetAt(j+1))/2.0

            global_bin = h.GetBin(i,j)
            bin_content = h.GetBinContent(global_bin)
            row = "{} {} {}".format(bin_x, bin_y, bin_content)
            f_out.write(row+'\n')



write_histo_contents(xs_gg_H,     './data/ascii/directly_from_root_file_xs_gg_H.dat')
write_histo_contents(br_H_hh,     './data/ascii/directly_from_root_file_br_H_hh.dat')
write_histo_contents(br_h_tautau, './data/ascii/directly_from_root_file_br_h_tautau.dat')
write_histo_contents(br_h_bb,     './data/ascii/directly_from_root_file_br_h_bb.dat')
write_histo_contents(br_h_gamgam, './data/ascii/directly_from_root_file_br_h_gamgam.dat')
write_histo_contents(m_H,         './data/ascii/directly_from_root_file_m_H.dat')
write_histo_contents(Gamma_H,     './data/ascii/directly_from_root_file_Gamma_H.dat')

save_binning(xs_gg_H, './data/ascii/directly_from_root_file_xs_gg_H_binning.dat')
save_binning(br_H_hh, './data/ascii/directly_from_root_file_br_H_hh_binning.dat')
save_binning(br_h_tautau, './data/ascii/directly_from_root_file_br_h_tautau_binning.dat')

#plot_histo(xs_gg_H, 'xs_gg_H.pdf')
#plot_histo(br_H_hh, 'br_H_hh.pdf')
#plot_histo(br_h_tautau, 'br_h_tautau.pdf')

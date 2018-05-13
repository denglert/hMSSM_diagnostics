#!/usr/bin/env bash


hMSSM_13TeV_histogam_link=https://twiki.cern.ch/twiki/pub/LHCPhysics/HXSWG3LowTanB/hMSSM_13TeV.root
wget ${hMSSM_13TeV_histogam_link}


python write_histogram_contents.py

cat duplicated_pairs.dat

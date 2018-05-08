#!/usr/bin/env python

from mssm_xs_tools import mssm_xs_tools

hMSSM_ROOT_histo_path = "./data/root/hMSSM_13TeV.root"
output_file_path = "./hMSSM_xsec.dat"



def linspace(min, binwidth, n):

    list = []
    
    for i in range(n):
        element = min + binwidth*i
        list.append(element)
    return list



def write_to_file(mA_min, mA_binwidth, mA_n, tanb_min, tanb_binwidth, tanb_n, output_file_path, interpolation=False):

    
    t = mssm_xs_tools(hMSSM_ROOT_histo_path, interpolation, 0)

    mAs = linspace(mA_min, mA_binwidth, mA_n)
    tanbs = linspace(tanb_min, tanb_binwidth, tanb_n)
    
    with open(output_file_path, "w") as f_out:
    
        # - Header
        f_out.write("mA tanb xsec_gg_H")
    
        for mA in mAs:
            for tanb in tanbs:
                xsec_gg_H = t.xsec("gg->H", mA, tanb)
                row = "{} {} {}".format(mA, tanb, xsec_gg_H)
                f_out.write(row+'\n')
        


write_to_file(180.0, 5.0, 84, 1.0, 0.1, 40, "./data/ascii/hMSSM_mA_5.0_tanb_0.1_int_on.dat",  interpolation=True)
write_to_file(180.0, 5.0, 84, 1.0, 0.1, 40, "./data/ascii/hMSSM_mA_5.0_tanb_0.1_int_off.dat", interpolation=False)

write_to_file(180.0, 5.0, 84, 1.0, 0.2, 40, "./data/ascii/hMSSM_mA_5.0_tanb_0.2_int_on.dat",  interpolation=True)
write_to_file(180.0, 5.0, 84, 1.0, 0.2, 40, "./data/ascii/hMSSM_mA_5.0_tanb_0.2_int_off.dat", interpolation=False)

write_to_file(180.0, 5.0, 84, 1.0, 0.11, 40, "./data/ascii/hMSSM_mA_5.0_tanb_0.11_int_on.dat",  interpolation=True)
write_to_file(180.0, 5.0, 84, 1.0, 0.11, 40, "./data/ascii/hMSSM_mA_5.0_tanb_0.11_int_off.dat", interpolation=False)

write_to_file(180.0, 5.0, 84, 1.0, 1.0, 40, "./data/ascii/hMSSM_mA_5.0_tanb_1.0_int_on.dat",  interpolation=True)
write_to_file(180.0, 5.0, 84, 1.0, 1.0, 40, "./data/ascii/hMSSM_mA_5.0_tanb_1.0_int_off.dat", interpolation=False)

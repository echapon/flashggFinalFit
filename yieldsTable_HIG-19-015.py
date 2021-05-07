#!/bin/python

import ROOT as r

basedir="/eos/user/e/echapon/work/HGG/hig-19-015/Models/signal"
normfactor=1.#41.5#35.9

# list of open RooDatasets, to be deleted when we close a file
open_rds = []

def gghyield(proc, cat, catgen, ws):
   """
   Get the yield for a given processus proc and a givery category cat
   """
   # print("sig_%s_%s_2017_mass_m125_RECO_%s" % (proc, catgen, cat))
   rds = ws.data("sig_%s_2017_mass_m125_RECO_%s" % (catgen, cat))
   
   result = 0
   if rds:
      open_rds.append(rds)
      result = rds.sumEntries()
   else:
      print("not found: sig_%s_2017_mass_m125_RECO_%s" % (catgen, cat))

   return result

# main part of the script
# procs = ["ggh", "vbf", "wh", "zh", "tth", "thq"]
procs = ["GG2H", "VBF", "WH2HQQ", "ZH2HQQ", "TTH", "THQ"]
# procs = ["ggh", "vbf", "wh", "zh"]
# cats = ["NoTag", "UntaggedTag_0", "UntaggedTag_1", "UntaggedTag_2", "UntaggedTag_3", "VBFTag_0", "VBFTag_1", "VBFTag_2"]
cats = [
   "0J_PTH_0_10_Tag0",
   "0J_PTH_0_10_Tag1",
   "0J_PTH_0_10_Tag2",
   "0J_PTH_GT10_Tag0",
   "0J_PTH_GT10_Tag1",
   "0J_PTH_GT10_Tag2",
   "1J_PTH_0_60_Tag0",
   "1J_PTH_0_60_Tag1",
   "1J_PTH_0_60_Tag2",
   "1J_PTH_120_200_Tag0",
   "1J_PTH_120_200_Tag1",
   "1J_PTH_120_200_Tag2",
   "1J_PTH_60_120_Tag0",
   "1J_PTH_60_120_Tag1",
   "1J_PTH_60_120_Tag2",
   "GE2J_PTH_0_60_Tag0",
   "GE2J_PTH_0_60_Tag1",
   "GE2J_PTH_0_60_Tag2",
   "GE2J_PTH_120_200_Tag0",
   "GE2J_PTH_120_200_Tag1",
   "GE2J_PTH_120_200_Tag2",
   "GE2J_PTH_60_120_Tag0",
   "GE2J_PTH_60_120_Tag1",
   "GE2J_PTH_60_120_Tag2",
   "PTH_200_300_Tag0",
   "PTH_200_300_Tag1",
   "PTH_300_450_Tag0",
   "PTH_300_450_Tag1",
   "PTH_450_650_Tag0",
   "PTH_GT650_Tag0",
   "THQ_LEP",
   "TTH_HAD_PTH_0_60_Tag0",
   "TTH_HAD_PTH_0_60_Tag1",
   "TTH_HAD_PTH_0_60_Tag2",
   # "TTH_HAD_PTH_0_60_Tag3",
   "TTH_HAD_PTH_120_200_Tag0",
   "TTH_HAD_PTH_120_200_Tag1",
   "TTH_HAD_PTH_120_200_Tag2",
   "TTH_HAD_PTH_120_200_Tag3",
   "TTH_HAD_PTH_60_120_Tag0",
   "TTH_HAD_PTH_60_120_Tag1",
   "TTH_HAD_PTH_60_120_Tag2",
   # "TTH_HAD_PTH_60_120_Tag3",
   "TTH_HAD_PTH_200_300_Tag0",
   "TTH_HAD_PTH_200_300_Tag1",
   "TTH_HAD_PTH_200_300_Tag2",
   "TTH_LEP_PTH_0_60_Tag0",
   "TTH_LEP_PTH_0_60_Tag1",
   "TTH_LEP_PTH_0_60_Tag2",
   # "TTH_LEP_PTH_0_60_Tag3",
   "TTH_LEP_PTH_120_200_Tag0",
   "TTH_LEP_PTH_120_200_Tag1",
   "TTH_LEP_PTH_60_120_Tag0",
   "TTH_LEP_PTH_60_120_Tag1",
   # "TTH_LEP_PTH_GT200_Tag0",
   # "TTH_LEP_PTH_GT200_Tag1",
   "VBFLIKEGGH_Tag0",
   "VBFLIKEGGH_Tag1",
   # "VBFTOPO_BSM_Tag0",
   # "VBFTOPO_BSM_Tag1",
   "VBFTOPO_JET3VETO_HIGHMJJ_Tag0",
   "VBFTOPO_JET3VETO_HIGHMJJ_Tag1",
   "VBFTOPO_JET3VETO_LOWMJJ_Tag0",
   "VBFTOPO_JET3VETO_LOWMJJ_Tag1",
   "VBFTOPO_JET3_HIGHMJJ_Tag0",
   "VBFTOPO_JET3_HIGHMJJ_Tag1",
   "VBFTOPO_JET3_LOWMJJ_Tag0",
   "VBFTOPO_JET3_LOWMJJ_Tag1",
   # "VBFTOPO_VHHAD_Tag0",
   # "VBFTOPO_VHHAD_Tag1",
   "VH_MET_Tag0",
   "VH_MET_Tag1",
   "WH_LEP_PTV_75_150_Tag0",
   "WH_LEP_PTV_75_150_Tag1",
   # "WH_LEP_PTV_75_150_Tag2",
   "WH_LEP_PTV_0_75_Tag0",
   "WH_LEP_PTV_0_75_Tag1",
   # "WH_LEP_PTV_0_75_Tag2",
   "ZH_LEP_Tag0",
   "ZH_LEP_Tag1"
         ]
# gen cats
gencats = [
"GG2HQQ_0J_PTH_GT10",
"THQ_FWDH",
"GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25",
"GG2HNUNU_PTV_0_75",
"GG2HLL_PTV_0_75",
"ZH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25",
"GG2HQQ_PTH_300_450",
"THW_FWDH",
"GG2HNUNU_PTV_150_250_GE1J",
"QQ2HLNU_PTV_75_150",
"QQ2HLL_PTV_150_250_0J",
"QQ2HLNU_PTV_0_75",
"ZH2HQQ_0J",
"WH2HQQ_GE2J_MJJ_60_120",
"GG2HNUNU_PTV_150_250_0J",
"GG2H_GE2J_MJJ_0_350_PTH_0_60",
"WH2HQQ_GE2J_MJJ_120_350",
"VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25",
"WH2HQQ_FWDH",
"VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25",
"ZH2HQQ_GE2J_MJJ_120_350",
"GG2HNUNU_FWDH",
"VBF_GE2J_MJJ_120_350",
"TTH_PTH_0_60",
"TTH_PTH_120_200",
"QQ2HLL_PTV_150_250_GE1J",
"GG2HLL_FWDH",
"GG2HQQ_FWDH",
"QQ2HLNU_PTV_150_250_0J",
"WH2HQQ_GE2J_MJJ_GT350_PTH_GT200",
"GG2H_0J_PTH_GT10",
"ZH2HQQ_1J",
"TTH_PTH_GT300",
"TTH_PTH_200_300",
"GG2H_PTH_GT650",
"GG2H_1J_PTH_60_120",
"VBF_FWDH",
"GG2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25",
"WH2HQQ_0J",
"GG2H_GE2J_MJJ_0_350_PTH_120_200",
"ZH2HQQ_GE2J_MJJ_0_60",
"QQ2HLL_PTV_0_75",
"GG2HLL_PTV_150_250_0J",
"VBF_GE2J_MJJ_60_120",
"GG2H_PTH_300_450",
"WH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25",
"ZH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25",
"GG2HLL_PTV_GT250",
"GG2HQQ_PTH_200_300",
"GG2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25",
"ZH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25",
"GG2HQQ_0J_PTH_0_10",
"GG2H_GE2J_MJJ_0_350_PTH_60_120",
"VBF_GE2J_MJJ_GT350_PTH_GT200",
"GG2HQQ_1J_PTH_60_120",
"GG2HQQ_GE2J_MJJ_0_350_PTH_0_60",
"GG2HNUNU_PTV_75_150",
"GG2HLL_PTV_150_250_GE1J",
"BBH_FWDH",
"GG2H_PTH_450_650",
"VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25",
"GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25",
"ZH2HQQ_GE2J_MJJ_GT350_PTH_GT200",
"GG2HQQ_1J_PTH_0_60",
"QQ2HLNU_PTV_150_250_GE1J",
"WH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25",
"WH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25",
"GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25",
"TTH_PTH_60_120",
"QQ2HLL_PTV_GT250",
"THW",
"ZH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25",
"GG2HQQ_GE2J_MJJ_0_350_PTH_120_200",
"VBF_1J",
"GG2HNUNU_PTV_GT250",
"QQ2HLNU_FWDH",
"GG2H_1J_PTH_0_60",
"GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25",
"WH2HQQ_1J",
"WH2HQQ_GE2J_MJJ_0_60",
"WH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25",
"GG2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25",
"GG2HLL_PTV_75_150",
"TTH_FWDH",
"GG2H_FWDH",
"VBF_GE2J_MJJ_0_60",
"GG2H_1J_PTH_120_200",
"GG2H_0J_PTH_0_10",
"GG2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25",
"VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25",
"GG2HQQ_PTH_GT650",
"QQ2HLNU_PTV_GT250",
"BBH",
"QQ2HLL_PTV_75_150",
"ZH2HQQ_GE2J_MJJ_60_120",
"GG2HQQ_1J_PTH_120_200",
"VBF_0J",
"THQ",
"GG2HQQ_GE2J_MJJ_0_350_PTH_60_120",
"GG2H_PTH_200_300",
"QQ2HLL_FWDH",
"GG2HQQ_PTH_450_650",
"ZH2HQQ_FWDH",
      ]
dic = {}

# read all the yields
for c in cats:
   dd = {}
   f = "%s/CMS-HGG_sigfit_packaged_RECO_%s.root" % (basedir, c)
   tf = r.TFile(f)
   ws = tf.Get("wsig_13TeV")
   for p in procs:
      theyield = 0
      for c2 in gencats:
         if p in c2:
            theyield = theyield + gghyield(p, c, c2, ws)
      dd[p] = theyield
      print("yield for (%s, %s): %f" % (p, c, dd[p]))
   dic[c] = dd

   # clean the memory
   for rds in open_rds:
      if rds:
         del rds
   open_rds = []
   del ws
   tf.Close()
   del tf

tot = {}
for c in cats:
   tot[c] = sum([dic[c][p] for p in procs if p != "data"])

# print table in dirty format
# header
line = "\tTotal\t"
for p in procs: line = line + p + "\t"
print(line)

# total / process
line = "Total \t" + "{:.2f}".format(sum([tot[c]*normfactor for c in cats])) + "\t"
for p in procs: line = line + "{:.2f}".format(sum([dic[c][p]*normfactor for c in cats])) + "\t"
print(line)

# categories
for c in cats:
   if tot[c] == 0:
      continue
   line = c + "\t" + "{:.2f}".format(tot[c]*normfactor) + "\t"
   for p in procs:
      line = line + "{:.2f}".format(dic[c][p] / tot[c] * 100) + "%\t"
   print(line)

# and now the LaTeX version
print("\n\n")

# header
line = "& Total &"
for p in procs: line = line + p + (" & " if p != procs[-1] else r"\\")
print(line)

# total / process
line = "Total &" + "{:.2f}".format(sum([tot[c]*normfactor for c in cats])) + " & "
for p in procs: line = line + "{:.2f}".format(sum([dic[c][p]*normfactor for c in cats])) + (" & " if p != procs[-1] else r"\\")
print(line)

# categories
for c in cats:
   if tot[c] == 0:
      continue
   line = c + " & " + "{:.2f}".format(tot[c]*normfactor) + " & "
   for p in procs:
      line = line + "{:.2f}".format(dic[c][p] / tot[c] * 100) + "\% " + ("& " if p != procs[-1] else r"\\")
   print(line)

#!/bin/python

import ROOT as r

# basedir="/afs/cern.ch/work/e/echapon/private/Higgs/CMSSW_10_6_8/src/flashgg/Systematics/MassTest/2016_all"
basedir="/eos/user/e/echapon/work/HGG/2017UL_HIG19015like/STXStags/all"
normfactor=41.5#35.9

def gghyield(proc, cat, ws):
   """
   Get the yield for a given processus proc and a givery category cat
   """
   if proc != "data":
      rds = ws.data("%s_125_13TeV_RECO_%s" % (proc, cat))
   else:
      rds = ws.data("Data_13TeV_%s" % (cat))
   
   result = 0
   if rds:
      result = rds.sumEntries()

   return result

# main part of the script
procs = ["ggh", "vbf", "wh", "zh", "tth", "thq"]
# procs = ["ggh", "vbf", "wh", "zh"]
# cats = ["NoTag", "UntaggedTag_0", "UntaggedTag_1", "UntaggedTag_2", "UntaggedTag_3", "VBFTag_0", "VBFTag_1", "VBFTag_2"]
cats = [
   "NOTAG",
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
   "TTH_HAD_PTH_0_60_Tag3",
   "TTH_HAD_PTH_120_200_Tag0",
   "TTH_HAD_PTH_120_200_Tag1",
   "TTH_HAD_PTH_120_200_Tag2",
   "TTH_HAD_PTH_120_200_Tag3",
   "TTH_HAD_PTH_60_120_Tag0",
   "TTH_HAD_PTH_60_120_Tag1",
   "TTH_HAD_PTH_60_120_Tag2",
   "TTH_HAD_PTH_60_120_Tag3",
   "TTH_HAD_PTH_GT200_Tag0",
   "TTH_HAD_PTH_GT200_Tag1",
   "TTH_HAD_PTH_GT200_Tag2",
   "TTH_HAD_PTH_GT200_Tag3",
   "TTH_LEP_PTH_0_60_Tag0",
   "TTH_LEP_PTH_0_60_Tag1",
   "TTH_LEP_PTH_0_60_Tag2",
   "TTH_LEP_PTH_0_60_Tag3",
   "TTH_LEP_PTH_120_200_Tag0",
   "TTH_LEP_PTH_120_200_Tag1",
   "TTH_LEP_PTH_60_120_Tag0",
   "TTH_LEP_PTH_60_120_Tag1",
   "TTH_LEP_PTH_GT200_Tag0",
   "TTH_LEP_PTH_GT200_Tag1",
   "VBFLIKEGGH_Tag0",
   "VBFLIKEGGH_Tag1",
   "VBFTOPO_BSM_Tag0",
   "VBFTOPO_BSM_Tag1",
   "VBFTOPO_JET3VETO_HIGHMJJ_Tag0",
   "VBFTOPO_JET3VETO_HIGHMJJ_Tag1",
   "VBFTOPO_JET3VETO_LOWMJJ_Tag0",
   "VBFTOPO_JET3VETO_LOWMJJ_Tag1",
   "VBFTOPO_JET3_HIGHMJJ_Tag0",
   "VBFTOPO_JET3_HIGHMJJ_Tag1",
   "VBFTOPO_JET3_LOWMJJ_Tag0",
   "VBFTOPO_JET3_LOWMJJ_Tag1",
   "VBFTOPO_VHHAD_Tag0",
   "VBFTOPO_VHHAD_Tag1",
   "VH_MET_Tag0",
   "VH_MET_Tag1",
   "WH_LEP_HIGH_Tag0",
   "WH_LEP_HIGH_Tag1",
   "WH_LEP_HIGH_Tag2",
   "WH_LEP_LOW_Tag0",
   "WH_LEP_LOW_Tag1",
   "WH_LEP_LOW_Tag2",
   "ZH_LEP_Tag0",
   "ZH_LEP_Tag1"
         ]
dic = {}

# read all the yields
for p in procs:
   if p != "data":
      f = "%s/output_%s_125.root" % (basedir, p)
      tf = r.TFile.Open(f)
      ws = tf.Get("tagsDumper/cms_hgg_13TeV")
   else:
      f = "%s/allData.root" % (basedir)
      tf = r.TFile.Open(f)
      ws = tf.Get("tagsDumper/cms_hgg_13TeV")
   dd = {}
   for c in cats:
      dd[c] = gghyield(p, c, ws)
      print("yield for (%s, %s): %f" % (p, c, dd[c]))
   dic[p] = dd

   del ws
   tf.Close()
   del tf

tot = {}
for c in cats:
   tot[c] = sum([dic[p][c] for p in procs if p != "data"])

# print table in dirty format
# header
line = "\tTotal\t"
for p in procs: line = line + p + "\t"
print(line)

# total / process
line = "Total \t" + "{:.2f}".format(sum([tot[c]*normfactor for c in cats])) + "\t"
for p in procs: line = line + "{:.2f}".format(sum([dic[p][c]*normfactor for c in cats])) + "\t"
print(line)

# categories
for c in cats:
   if tot[c] == 0:
      continue
   line = c + "\t" + "{:.2f}".format(tot[c]*normfactor) + "\t"
   for p in procs:
      line = line + "{:.2f}".format(dic[p][c] / tot[c] * 100) + "%\t"
   print(line)

# and now the LaTeX version
print("\n\n")

# header
line = "& Total &"
for p in procs: line = line + p + (" & " if p != procs[-1] else r"\\")
print(line)

# total / process
line = "Total &" + "{:.2f}".format(sum([tot[c]*normfactor for c in cats])) + " & "
for p in procs: line = line + "{:.2f}".format(sum([dic[p][c]*normfactor for c in cats])) + (" & " if p != procs[-1] else r"\\")
print(line)

# categories
for c in cats:
   if tot[c] == 0:
      continue
   line = c + " & " + "{:.2f}".format(tot[c]*normfactor) + " & "
   for p in procs:
      line = line + "{:.2f}".format(dic[p][c] / tot[c] * 100) + "\% " + ("& " if p != procs[-1] else r"\\")
   print(line)

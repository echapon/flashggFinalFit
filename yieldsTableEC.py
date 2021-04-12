#!/bin/python

import ROOT as r

basedir="/afs/cern.ch/work/e/echapon/private/Higgs/CMSSW_10_6_8/src/flashgg/Systematics/MassTest/2016_all"

def gghyield(proc, cat):
   """
   Get the yield for a given processus proc and a givery category cat
   """
   if proc != "data":
      f = "%s/output_%s_125.root" % (basedir, proc)
      tf = r.TFile.Open(f)
      ws = tf.Get("tagsDumper/cms_hgg_13TeV")
      rds = ws.data("%s_125_13TeV_%s" % (proc, cat))
   else:
      f = "%s/allData.root" % (basedir)
      tf = r.TFile.Open(f)
      ws = tf.Get("tagsDumper/cms_hgg_13TeV")
      rds = ws.data("Data_13TeV_%s" % (cat))
   return rds.sumEntries()

# main part of the script
procs = ["ggh", "vbf", "wh", "zh", "tth"]
# procs = ["ggh"]
cats = ["NoTag", "UntaggedTag_0", "UntaggedTag_1", "UntaggedTag_2", "UntaggedTag_3", "VBFTag_0", "VBFTag_1", "VBFTag_2"]
dic = {}

# read all the yields
for p in procs:
   dd = {}
   for c in cats:
      dd[c] = gghyield(p, c)
      print("yield for (%s, %s): %f" % (p, c, dd[c]))
   dic[p] = dd

tot = {}
for c in cats:
   tot[c] = sum([dic[p][c] for p in procs if p != "data"])

# print table in dirty format
line = "\tTotal\t"
for p in procs: line = line + p + "\t"
print(line)
for c in cats:
   line = c + "\t" + "{:.2f}".format(tot[c]) + "\t"
   for p in procs:
      line = line + "{:.2f}".format(dic[p][c] / tot[c] * 100) + "%\t"
   print(line)

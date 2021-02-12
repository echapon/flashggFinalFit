# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/afs/cern.ch/user/e/echapon/workspace/private/Higgs/CMSSW_10_6_8/src/flashgg/Systematics/MassTest/2016_data', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'MassTest_EC_20210208', # extension to add to output directory
  'year':'2016', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'condor', # [condor,SGE,IC,local]
  'queue':'espresso' # for condor e.g. microcentury
  
}

# Config file: options for signal fitting

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/afs/cern.ch/user/e/echapon/workspace/private/Higgs/CMSSW_10_6_8/src/flashgg/Systematics/MassTest/2016_Sig', 
  'procs':'ggh,wh,vbf,tth,zh', # if auto: inferred automatically from filenames
  # 'cats':'auto', # if auto: inferred automatically from (0) workspace
  'cats':'UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,VBFTag_0,VBFTag_1,VBFTag_2', # if auto: inferred automatically from (0) workspace
  'ext':'MassTest_EC_20210208',
  'analysis':'mass', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'2016', # Use 'combined' if merging all years: not recommended
  'beamspot':'3.4', # Beamspot in data
  'numberOfBins':'320',
  'massPoints':'120,125,130',

  # Use DCB in fit
  'useDCB':0,

  #Photon shape systematics  
  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB', # separate nuisance per year
  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB', # correlated across years
  'scalesGlobal':'NonLinearity,Geant4', # affect all processes equally, correlated across years
  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho', # separate nuisance per year

  # Job submission options
  # 'batch':'IC', # ['condor','SGE','IC','local']
  # 'queue':'hep.q'
  'batch':'condor', # ['condor','SGE','IC','local']
  'queue':'espresso',

}

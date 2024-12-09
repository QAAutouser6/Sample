def lanuchOutLook():
  
  p = TestedApps.OUTLOOK.Run()
  Delay(10000)
  wndOutlook = NameMapping.Sys.OUTLOOK.wndrctrl_renwnd32
  wndOutlook.Maximize()
  
def closeOutlook():
  wndOutlook = NameMapping.Sys.OUTLOOK.wndrctrl_renwnd32
  wndOutlook.Close()
  Delay(5000)
  
  
  

import outlook

def lanuchAndCloseOutlook():
  aqTestCase.Begin("Launch Outlook")
  outlook.lanuchOutLook()
  aqTestCase.End()
  aqTestCase.Begin("Launch Outlook")
  outlook.closeOutlook()
  aqTestCase.End()
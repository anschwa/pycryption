#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PyCryption is an "simple" RSA encryption program with a GUI built from wxPython.
Made by Adam Schwartz, April 2013
'''

import wx
import panels

class AppFrame (wx.Frame):
    
    def __init__(self, *args, **kw):
        super(AppFrame, self).__init__(*args, **kw)
        self.InitUI()
                
    def InitUI(self):
        
        # Establish Frame sizers.
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        ###
        
        self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        self.splitter.SetMinimumPaneSize(15)
        self.splitter.Bind(wx.EVT_SPLITTER_DCLICK, self.OnSplitClick)
        self.mainSizer.Add(self.splitter, 1, wx.EXPAND)
        
        # Add Panels for Splitter Window
        self.mainPnl = panels.TheMainPnl(self.splitter, -1)        
        self.helpPnl = panels.HelpMenuPnl(self.splitter, -1)
        ###        
        
        self.splitter.SplitVertically(self.mainPnl, self.helpPnl)
        self.splitter.Unsplit()
        
        self.SetSizer(self.mainSizer)
        

        # ALL "GLOBAL" PANEL EVENT BINDINGS
        # Bind Buttons from TheMainPnl's child panels to events.
        #--------------------------------
        self.mainPnl.pnl1.customBtn.Bind(wx.EVT_BUTTON, self.OnCustom)
        self.mainPnl.pnl1.quickBtn.Bind(wx.EVT_BUTTON, self.OnQuick)
        #--------------------------------
        self.mainPnl.pnl2.getKeys.Bind(wx.EVT_BUTTON, self.OnCustomKey)
        self.mainPnl.pnl2.encryptBtn.Bind(wx.EVT_BUTTON, self.OnCustomEn)
        self.mainPnl.pnl2.decryptBtn.Bind(wx.EVT_BUTTON, self.OnCustomDe)
        #--------------------------------
        self.mainPnl.pnl6.encryptBtn.Bind(wx.EVT_BUTTON, self.OnQuickEn)
        self.mainPnl.pnl6.decryptBtn.Bind(wx.EVT_BUTTON, self.OnQuickDe)
        #--------------------------------
        self.mainPnl.navPnl.backBtn.Bind(wx.EVT_BUTTON, self.OnBack)
        self.mainPnl.navPnl.helpBtn.Bind(wx.EVT_BUTTON, self.OnHelp)
        ###
        ###


        self.SetMinSize((250,220))
        self.SetSize((250,220))     # this is the size for pnl1
        self.SetTitle('PyCryption')
        self.Center()
        self.Show(True)
        
    #-------------------------------------------------------------
    # On Panel Button Funcitons
    
    def OnBack(self, e):
        # hide and show appropriate pnl based on ID
    
        #--------------------------------
        if self.mainPnl.pnl2.IsShown() == True:
            self.mainPnl.pnl2.Hide()
            self.mainPnl.pnl1.Show()
            self.SetTitle("PyCryption")
            self.SetSize((250,220))
            self.SetMinSize((250,220))
        #--------------------------------
        elif self.mainPnl.pnl3.IsShown() == True:
            self.mainPnl.pnl3.Hide()
            self.mainPnl.pnl2.Show()
            self.SetTitle("Custom Mode")
            self.SetSize((250,295))
            self.SetMinSize((250,295))
        #--------------------------------
        elif self.mainPnl.pnl4.IsShown() == True:
            self.mainPnl.pnl4.Hide()
            self.mainPnl.pnl2.Show()
            self.SetTitle("Custom Mode")
            self.SetSize((250,295))
            self.SetMinSize((250,295))
         #--------------------------------   
        elif self.mainPnl.pnl5.IsShown() == True:
            self.mainPnl.pnl5.Hide()
            self.mainPnl.pnl2.Show()
            self.SetTitle("Custom Mode")
            self.SetSize((250,295))
            self.SetMinSize((250,295))
        #--------------------------------    
        elif self.mainPnl.pnl6.IsShown() == True:
            self.mainPnl.pnl6.Hide()
            self.mainPnl.pnl1.Show()
            self.SetTitle("PyCryption")
            self.SetSize((250,220))
            self.SetMinSize((250,220))
         #--------------------------------   
        elif self.mainPnl.pnl7.IsShown() == True:
            self.mainPnl.pnl7.Hide()
            self.mainPnl.pnl6.Show()
            self.SetTitle("Quick Mode")
            self.SetSize((250,220))
            self.SetMinSize((250,220))
        #--------------------------------    
        elif self.mainPnl.pnl8.IsShown() == True:
            self.mainPnl.pnl8.Hide()
            self.mainPnl.pnl6.Show()
            self.SetTitle("Quick Mode")
            self.SetSize((250,220))
            self.SetMinSize((250,220))
       #--------------------------------
        # Main Panel and Frame sizers must be "refreshed" to prevent invisible panels.
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()
    
    #-------------------------------------------------------------
    def OnHelp(self, e):
        if self.splitter.IsSplit() == True:
            a,b = self.GetSize()
            self.SetSize((a-200,b))
            self.splitter.Unsplit()
        else:
            a,b = self.GetSize()
            self.SetSize((a+200,b))
            self.splitter.SplitVertically(self.mainPnl, self.helpPnl)
            
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()
    #--------------------------------
    
    def OnCustom(self, e):
        self.mainPnl.pnl1.Hide()
        self.mainPnl.pnl2.Show()
        self.SetSize((250,295))
        self.SetMinSize((250,295))
        self.SetTitle("Custom Mode")
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()     
        
    def OnCustomKey(self, e):
        self.mainPnl.pnl2.Hide()
        self.mainPnl.pnl3.Show()
        self.SetTitle("Generate Keys")
        self.SetSize((260,220))
        self.SetMinSize((260,220))
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()

    def OnCustomEn(self, e):
        self.mainPnl.pnl2.Hide()
        self.mainPnl.pnl4.Show()
        self.SetSize((565,462))
        self.SetMinSize((565,462))
        self.SetTitle("Custom Encrypt")
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()

    def OnCustomDe(self, e):
        self.mainPnl.pnl2.Hide()
        self.mainPnl.pnl5.Show()
        self.SetSize((565,462))
        self.SetMinSize((565,462))
        self.SetTitle("Custom Decrypt")
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()
    #--------------------------------
        
    def OnQuick(self, e):
        self.mainPnl.pnl1.Hide()
        self.mainPnl.pnl6.Show()
        self.SetTitle("Quick Mode")
        self.SetSize((250,220))
        self.SetMinSize((250,220))
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()     
        
    def OnQuickEn(self, e):
        self.mainPnl.pnl6.Hide()
        self.mainPnl.pnl7.Show()
        self.SetSize((340,462))
        self.SetMinSize((340,462))
        self.SetTitle("Quick Encrypt")
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()
        
    def OnQuickDe(self, e):
        self.mainPnl.pnl6.Hide()
        self.mainPnl.pnl8.Show()
        self.SetSize((340,462))
        self.SetMinSize((340,462))
        self.SetTitle("Quick Decrypt")
        self.mainPnl.mainSizer.Layout()
        self.mainSizer.Layout()
    #--------------------------------
    
    def OnSplitClick(self, e):
        # Resets split to center
        size =  self.GetSize()
        self.splitter.SetSashPosition(size.x / 2)
        
    #-------------------------------------------------------------
    
def main():
    ex = wx.App()
    AppFrame(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
    
###################################################################################################
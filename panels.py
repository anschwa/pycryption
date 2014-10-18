'''
The panels belonging to wxgui
'''

import wx
import wx.html as html
import encryptor as crypt
import pyperclip


###################################################################################################
class NavPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(NavPanel, self).__init__(*args, **kw)
        self.SetSize((-1, 32))

        navSizer = wx.BoxSizer(wx.HORIZONTAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
         
        bmp1 = wx.Bitmap("images/back.png", wx.BITMAP_TYPE_ANY)
        bmp2 = wx.Bitmap("images/help.png", wx.BITMAP_TYPE_ANY)
        
        self.trap = wx.Button(self, size=(0,0))  # this 'traps' the focus to an invisible button
        hbox1.Add(self.trap, 0)
        self.backBtn = wx.BitmapButton(self, -1, bitmap=bmp1,style=wx.NO_BORDER)
        hbox1.Add(self.backBtn, 0)
        
        self.helpBtn = wx.BitmapButton(self, bitmap=bmp2, style=wx.NO_BORDER)
        hbox2.Add(self.helpBtn)
        
        navSizer.Add(hbox1, 1, wx.EXPAND)
        navSizer.Add(hbox2, 0, wx.EXPAND)
        self.SetSizer(navSizer)
               
###################################################################################################
class MainMenuPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(MainMenuPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("RED")
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Menu Buttons
        self.customBtn = wx.Button(self, label="\nCustom\n")
        vbox.Add(self.customBtn, 1, wx.EXPAND|wx.BOTTOM, 5)
        self.quickBtn = wx.Button(self, label="\nQuick\n")
        vbox.Add(self.quickBtn, 1, wx.EXPAND|wx.TOP, 5)
        ###
        
        sizer.Add(vbox, 1, wx.CENTER)
        self.SetSizer(sizer)
                        
###################################################################################################
class CustomMenuPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(CustomMenuPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("BLUE")
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.encryptBtn = wx.Button(self, label="\nEncrypt\n")
        vbox.Add(self.encryptBtn, 1, wx.EXPAND|wx.BOTTOM, 5)
        self.decryptBtn = wx.Button(self, label="\nDecrypt\n")
        vbox.Add(self.decryptBtn, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        self.getKeys = wx.Button(self, label="\nGet Keys\n")
        vbox.Add(self.getKeys, 1, wx.EXPAND|wx.TOP, 5)
        
        sizer.Add(vbox, 1, wx.CENTER)
        self.SetSizer(sizer)
                
###################################################################################################
class GetKeysPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(GetKeysPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("GREEN")
        
        keyVbox = wx.BoxSizer(wx.VERTICAL)
        
        #--------------------------------        
        keyGridSizer = wx.FlexGridSizer(rows=4, cols=2, vgap=5, hgap=5)
                
        prmtyl = wx.StaticText(self, -1, label="Primes:")
        self.prmval = wx.TextCtrl(self, -1, value="", style=wx.TE_CENTER)
        self.prmbtn = wx.Button(self, -1, label="Generate Keys")
        
        ekeytle = wx.StaticText(self, -1, label="Public Key:")
        self.ekeyval = wx.TextCtrl(self, -1, value="", style=wx.TE_CENTER|wx.TE_READONLY)
        
        dkeytle = wx.StaticText(self, -1, label="Private Key:")
        self.dkeyval = wx.TextCtrl(self, -1, value="", style=wx.TE_CENTER|wx.TE_READONLY)
        ###
        
        title1 = wx.StaticText(self, label="Enter Two Prime Numbers:")
        keyVbox.Add(title1, 0, wx.TE_CENTER|wx.BOTTOM, 10)
                
        keyGridSizer.AddMany([
            (prmtyl),
            (self.prmval, 1, wx.EXPAND), ((0,0)),
            (self.prmbtn, 0, wx.TE_CENTER|wx.TOP|wx.BOTTOM, 2),
            (ekeytle),
            (self.ekeyval, 1, wx.EXPAND),
            (dkeytle),
            (self.dkeyval, 1, wx.EXPAND)])
                
                
        keyGridSizer.AddGrowableCol(1)
        
        keyVbox.Add(keyGridSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 5)
        
        #--------------------------------
                
        self.SetSizer(keyVbox)
            
###################################################################################################
class CustomEncryptPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(CustomEncryptPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("PURPLE")
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        # Key display Sizer
        keyHbox = wx.BoxSizer(wx.HORIZONTAL)
        keyGrid = wx.FlexGridSizer(rows=3, cols=1, vgap=5, hgap=0)
        ###
        
        eKeyTitle = wx.StaticText(self, label="Enter Public Key")
        self.eKey = wx.TextCtrl(self, -1, value="", style=wx.TE_CENTER)
        self.keyBtn = wx.Button(self, label="Submit")
        self.keyBtn.Bind(wx.EVT_BUTTON, self.OnSubmit)
        
        keyGrid.AddMany([
            (eKeyTitle, 0, wx.TE_CENTER),
            (self.eKey, 0, wx.TE_CENTER),
            (self.keyBtn, 0, wx.TE_CENTER)])
        
        
        keyHbox.Add(keyGrid, 1, wx.CENTER)
        hbox.Add(keyHbox, 0, wx.EXPAND|wx.CENTER|wx.BOTTOM, 10)
        ###
        
        # Encryption Sizer
        messageFlexBox = wx.FlexGridSizer(rows=7, cols=1, vgap=10, hgap=0)
        
        messageTitle = wx.StaticText(self, -1, label="Enter a Message to Encrypt:")
        self.messageInput = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)
        self.messageBtn = wx.Button(self, -1, label="Encrypt Message")
        self.messageBtn.Bind(wx.EVT_BUTTON, self.OnEncrypt)
        
        divider = wx.StaticLine(self, -1)
        
        enmessageTitle = wx.StaticText(self, -1, label="This is your Encrypted Message:")
        self.enmessageInput = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.enmessageBtn = wx.Button(self, -1, label="Copy to Clipboard")
        self.enmessageBtn.Bind(wx.EVT_BUTTON, self.OnCopy)
        
        
        messageFlexBox.AddMany([
            (messageTitle, 0, wx.ALIGN_CENTER),
            (self.messageInput, 1, wx.EXPAND),
            (self.messageBtn, 0, wx.TE_CENTER),
            (divider, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 4),
            (enmessageTitle, 0, wx.ALIGN_CENTER),
            (self.enmessageInput, 1, wx.EXPAND),
            (self.enmessageBtn, 0, wx.TE_CENTER)])
        
        messageFlexBox.AddGrowableRow(1)
        messageFlexBox.AddGrowableRow(5)
        messageFlexBox.AddGrowableCol(0)
        
        hbox.Add(messageFlexBox, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 10)
        ###
        
        self.SetSizer(hbox)
        
    def OnSubmit(self, e):
        pass
        
    def OnEncrypt(self, e):
        pubKey = self.eKey.GetValue()
        message = self.messageInput.GetValue()
        enMessage = crypt.encrypt_message(pubKey, message)
        self.enmessageInput.SetValue(enMessage)

    def OnCopy(self, e):
        enMessage = self.enmessageInput.GetValue()
        pyperclip.copy(enMessage)
        
        
###################################################################################################
class CustomDecryptPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(CustomDecryptPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("YELLOW")
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        # Key display Sizer
        keyHbox = wx.BoxSizer(wx.HORIZONTAL)
        keyGrid = wx.FlexGridSizer(rows=3, cols=1, vgap=5, hgap=0)
        ###
        
        dKeyTitle = wx.StaticText(self, label="Enter Private Key")
        self.dKey = wx.TextCtrl(self, -1, style=wx.TE_CENTER)
        self.keyBtn = wx.Button(self, label="Submit")
        self.keyBtn.Bind(wx.EVT_BUTTON, self.OnSubmit)
        
        keyGrid.AddMany([
            (dKeyTitle, 0, wx.TE_CENTER),
            (self.dKey, 0, wx.TE_CENTER),
            (self.keyBtn, 0, wx.TE_CENTER)
        ])
        
        
        keyHbox.Add(keyGrid, 1, wx.CENTER)
        hbox.Add(keyHbox, 0, wx.EXPAND|wx.CENTER|wx.BOTTOM, 10)
        ###
        
        
        # Encryption Sizer
        messageFlexBox = wx.FlexGridSizer(rows=7, cols=1, vgap=10, hgap=0)
        
        messageTitle = wx.StaticText(self, -1, label="Enter a Message to Decrypt:")
        self.messageInput = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)
        self.messageBtn = wx.Button(self, -1, label="Decrypt Message")
        self.messageBtn.Bind(wx.EVT_BUTTON, self.OnDecrypt)
        
        divider = wx.StaticLine(self, -1)
        
        demessageTitle = wx.StaticText(self, -1, label="This is your Decrypted Message:")
        self.demessageInput = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.demessageBtn = wx.Button(self, -1, label="Copy to Clipboard")
        self.demessageBtn.Bind(wx.EVT_BUTTON, self.OnCopy)
        
        
        messageFlexBox.AddMany([
            (messageTitle, 0, wx.ALIGN_CENTER),
            (self.messageInput, 1, wx.EXPAND),
            (self.messageBtn, 0, wx.TE_CENTER),
            (divider, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 4),
            (demessageTitle, 0, wx.ALIGN_CENTER),
            (self.demessageInput, 1, wx.EXPAND),
            (self.demessageBtn, 0, wx.TE_CENTER)])
        
        messageFlexBox.AddGrowableRow(1)
        messageFlexBox.AddGrowableRow(5)
        messageFlexBox.AddGrowableCol(0)
        
        hbox.Add(messageFlexBox, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 10)
        ###
        
        self.SetSizer(hbox)
        
    def OnSubmit(self, e):
        pass
    
    def OnDecrypt(self, e):
        priKey = self.dKey.GetValue()
        enMessage = self.messageInput.GetValue()
        deMessage = crypt.decrypt_message(priKey, enMessage)
        self.demessageInput.SetValue(deMessage)
        
    def OnCopy(self, e):
        deMessage = self.demessageInput.GetValue()
        pyperclip.copy(deMessage)
        
###################################################################################################
class QuickMenuPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(QuickMenuPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("WHITE")
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.encryptBtn = wx.Button(self, label="\nEncrypt\n")
        vbox.Add(self.encryptBtn, 1, wx.EXPAND|wx.BOTTOM, 5)
        self.decryptBtn = wx.Button(self, label="\nDecrypt\n")
        vbox.Add(self.decryptBtn, 1, wx.EXPAND|wx.TOP, 5)
        
        sizer.Add(vbox, 1, wx.CENTER)
        self.SetSizer(sizer)
        
###################################################################################################
class QuickEncryptPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(QuickEncryptPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("BLACK")
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        messageFlexBox = wx.FlexGridSizer(rows=7, cols=1, vgap=10, hgap=0)
        
        messageTitle = wx.StaticText(self, -1, label="Enter a Message to Encrypt:")
        self.messageInput = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)
        self.messageBtn = wx.Button(self, -1, label="Encrypt Message")
        self.messageBtn.Bind(wx.EVT_BUTTON, self.OnEncrypt)
        
        
        divider = wx.StaticLine(self, -1)
        
        enmessageTitle = wx.StaticText(self, -1, label="This is your Encrypted Message:")
        self.enmessageInput = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.enmessageBtn = wx.Button(self, -1, label="Copy to Clipboard")
        self.enmessageBtn.Bind(wx.EVT_BUTTON, self.OnCopy)
        
        
        messageFlexBox.AddMany([
            (messageTitle, 0, wx.ALIGN_CENTER),
            (self.messageInput, 1, wx.EXPAND),
            (self.messageBtn, 0, wx.TE_CENTER),
            (divider, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 4),
            (enmessageTitle, 0, wx.ALIGN_CENTER),
            (self.enmessageInput, 1, wx.EXPAND),
            (self.enmessageBtn, 0, wx.TE_CENTER)])
        
        messageFlexBox.AddGrowableRow(1)
        messageFlexBox.AddGrowableRow(5)
        messageFlexBox.AddGrowableCol(0)
        
        vbox.Add(messageFlexBox, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 10)
        
        self.SetSizer(vbox)
    
    def OnEncrypt(self, e):
        pubKey = '3233, 17'
        message = self.messageInput.GetValue()
        enMessage = crypt.encrypt_message(pubKey, message)
        self.enmessageInput.SetValue(enMessage)
        
    def OnCopy(self, e):
        enMessage = self.enmessageInput.GetValue()
        pyperclip.copy(enMessage)
        
###################################################################################################
class QuickDecryptPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(QuickDecryptPnl, self).__init__(*args, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("GREY")
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        messageFlexBox = wx.FlexGridSizer(rows=7, cols=1, vgap=10, hgap=0)
        
        messageTitle = wx.StaticText(self, -1, label="Enter a Message to Decrypt:")
        self.messageInput = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)
        self.messageBtn = wx.Button(self, -1, label="Decrypt Message")
        self.messageBtn.Bind(wx.EVT_BUTTON, self.OnDecrypt)
        
        divider = wx.StaticLine(self, -1)
        
        demessageTitle = wx.StaticText(self, -1, label="This is your Decrypted Message:")
        self.demessageInput = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.demessageBtn = wx.Button(self, -1, label="Copy to Clipboard")
        self.demessageBtn.Bind(wx.EVT_BUTTON, self.OnCopy)
        
        
        messageFlexBox.AddMany([
            (messageTitle, 0, wx.ALIGN_CENTER),
            (self.messageInput, 1, wx.EXPAND),
            (self.messageBtn, 0, wx.TE_CENTER),
            (divider, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 4),
            (demessageTitle, 0, wx.ALIGN_CENTER),
            (self.demessageInput, 1, wx.EXPAND),
            (self.demessageBtn, 0, wx.TE_CENTER)])
        
        messageFlexBox.AddGrowableRow(1)
        messageFlexBox.AddGrowableRow(5)
        messageFlexBox.AddGrowableCol(0)
        
        vbox.Add(messageFlexBox, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 10)
        
        self.SetSizer(vbox)
        
    def OnDecrypt(self, e):
        priKey = '3233, 2753'
        enMessage = self.messageInput.GetValue()
        deMessage = crypt.decrypt_message(priKey, enMessage)
        self.demessageInput.SetValue(deMessage)
        
    def OnCopy(self, e):
        deMessage = self.demessageInput.GetValue()
        pyperclip.copy(deMessage)
        
###################################################################################################
class HelpMenuPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(HelpMenuPnl, self).__init__(*args, style=wx.SUNKEN_BORDER, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        #self.SetBackgroundColour("TAN")
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        helpWindow = html.HtmlWindow(self, -1, style=wx.NO_BORDER)
        helpWindow.LoadPage('help.html')
        
        sizer.Add(helpWindow, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
###################################################################################################
class ExtraPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(ExtraPnl, self).__init__(*args, style=wx.SUNKEN_BORDER, **kw)
        self.InitPnl()
    
    def InitPnl(self):
        self.SetBackgroundColour("PINK")
        
###################################################################################################
class TheMainPnl (wx.Panel):
    def __init__(self, *args, **kw):
        super(TheMainPnl, self).__init__(*args, **kw)
        self.InitPnl()
        
    def InitPnl(self):
        
        # Main sizers #
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainVbox = wx.BoxSizer(wx.VERTICAL)
        mainHobx = wx.BoxSizer(wx.HORIZONTAL)
        mainFlexBox = wx.FlexGridSizer(rows=2, cols=5, vgap=0, hgap=0)
        ###
        
        # Items to add to sizers
        #--------------------------------
        self.pnl1 = MainMenuPnl(self, -1)
        self.pnl1.Show()
        #--------------------------------
        self.pnl2 = CustomMenuPnl(self, -1)
        self.pnl2.Hide()
        #--------------------------------
        self.pnl3 = GetKeysPnl(self, -1)
        self.pnl3.Hide()
        #--------------------------------
        self.pnl4 = CustomEncryptPnl(self, -1)
        self.pnl4.Hide()
        #--------------------------------
        self.pnl5 = CustomDecryptPnl(self, -1)
        self.pnl5.Hide()
        #--------------------------------
        self.pnl6 = QuickMenuPnl(self, -1)
        self.pnl6.Hide()
        #--------------------------------
        self.pnl7 = QuickEncryptPnl(self, -1)
        self.pnl7.Hide()
        #--------------------------------
        self.pnl8 = QuickDecryptPnl(self, -1)
        self.pnl8.Hide()
        #--------------------------------
        #self.pnl9 = HelpMenuPnl(self, -1)
        #self.pnl9.Hide()
        #--------------------------------
        self.pnl10 = ExtraPnl(self, -1)
        self.pnl10.Hide()
        #--------------------------------
        self.navPnl = NavPanel(self, -1)
        #--------------------------------
        
        mainFlexBox.AddMany([
            (self.pnl1, 1, wx.EXPAND),
            (self.pnl2, 1, wx.EXPAND),
            (self.pnl3, 1, wx.EXPAND),
            (self.pnl4, 1, wx.EXPAND),
            (self.pnl5, 1, wx.EXPAND),
            (self.pnl6, 1, wx.EXPAND),
            (self.pnl7, 1, wx.EXPAND),
            (self.pnl8, 1, wx.EXPAND),
            #(self.pnl9, 1, wx.EXPAND),
            (self.pnl10, 1, wx.EXPAND)])
        ###
        # Make all rows / cols growable
        mainFlexBox.AddGrowableRow(0)
        mainFlexBox.AddGrowableRow(1)
        mainFlexBox.AddGrowableCol(0)
        mainFlexBox.AddGrowableCol(1)
        mainFlexBox.AddGrowableCol(2)
        mainFlexBox.AddGrowableCol(3)
        mainFlexBox.AddGrowableCol(4)
        ###
        
        # Add to main sizers #
        mainHobx.Add(mainFlexBox, 1, wx.EXPAND|wx.CENTER)
        #mainHobx.Add(self.pnl9, 2, wx.EXPAND|wx.CENTER)
        mainVbox.Add(mainHobx, 1, wx.EXPAND|wx.CENTER)
        
        self.mainSizer.Add(self.navPnl, 0, wx.EXPAND|wx.ALL, 4)
        self.mainSizer.Add(mainVbox, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 20) # adds 10px padding between Frame and mainSizer
        ###
        
        # Bind Events for linking encryption
        self.pnl3.prmbtn.Bind(wx.EVT_BUTTON, self.OnGen)
        ###
        
                
        # Set mainSizer to Frame
        self.SetSizer(self.mainSizer)
        
    #------------------------------------
    # Bind "linking" crypt event handlers
    
    def OnGen(self, e):
        primes = self.pnl3.prmval.GetValue()
        try:
            genKeys = crypt.gen_keys(primes)
            pubKey = str(genKeys[0][0])+', '+str(genKeys[0][1])     # removes parentheses from key tuple
            self.pnl3.ekeyval.SetValue(pubKey)
            self.pnl4.eKey.SetValue(pubKey)  # sets value in custom encrypt
            
            priKey = str(genKeys[1][0])+', '+str(genKeys[1][1])
            self.pnl3.dkeyval.SetValue(priKey)
            self.pnl5.dKey.SetValue(priKey)  # sets value in custom decrypt
                                            
        except (IndexError, ValueError) as e:
            #print "Enter two prime numbers separated with a comma"
            pass
        
###################################################################################################
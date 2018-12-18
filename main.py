#Twitter Bot
import wx
class MainFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(400,400))
        self.CreateStatusBar()

        #Menu Bar (Local on Windows, Linux, Global on Mac, of course.)
        fileMenu =wx.Menu()
        fileMenu.AppendSeparator()
        newTweetEntry = fileMenu.Append(wx.ID_ANY, "New Tweet"," Compose a new Tweet.")
        self.Bind(wx.EVT_MENU, self.newTweet, newTweetEntry)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&File")
        self.SetMenuBar(menuBar)
        self.Show(True)
    def newTweet(self, event):
        print("Lol have fun")
app=wx.App(False)
frame = MainFrame(None, 'Pancho\'s Twitter Bot')
app.MainLoop()


"""
#WX Example
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu= wx.Menu()

        aboutMenuEntry = filemenu.Append(wx.ID_ABOUT, "&About"," Info regarding this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutMenuEntry)
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Kill the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        self.Show(True)
    def OnAbout(self, event):
        dlg = wx.MessageDialog( self, "A small txt editor","About Sample Editor",wx.OK)
        dlg.ShowModal()
        dlg.Destroy
    def OnExit(self, event):
        self.Close(true)
app=wx.App(False)
frame = MyFrame(None, 'Editor piqui~no')
app.MainLoop()
"""

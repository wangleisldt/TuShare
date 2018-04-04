import wx


def setupMenuBar(self):
    self.CreateStatusBar()
    menubar = wx.MenuBar()
    menufile = wx.Menu()
    mnuabout = menufile.Append(wx.ID_ABOUT, u'&关于', 'about this shit')
    mnuexit = menufile.Append(wx.ID_EXIT, u'&退出', 'end program')
    menubar.Append(menufile, u'&操作')
    self.Bind(wx.EVT_MENU, self.onAbout, mnuabout)
    self.Bind(wx.EVT_MENU, self.onExit, mnuexit)
    self.SetMenuBar(menubar)

class App(wx.App):
    def OnInit(self):
       self.frame = wx.Frame(parent=None, title='量化')
       self.frame.Show()
       self.SetTopWindow(self.frame)

       return True

class MainWindow(wx.Frame):
    '''定义一个窗口类'''

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(10600, 10600))
        self.setupMenuBar()
        self.Centre()
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))

#程序入口
if __name__ == '__main__':
    app = App()
    app.MainLoop()



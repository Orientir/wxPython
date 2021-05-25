import wx.adv
import wx
import requests

TRAY_TOOLTIP = 'Курс валют - Приват Банк' 
TRAY_ICON = 'images/logo_exchange_rates.png' 



def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")

def get_buy(obj):
    return obj.get('buy')

def get_sell(obj):
    return obj.get('sale')


class Example(wx.Frame): 
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title, size = (300, 140))
        self.SetIcon(wx.Icon("images/logo_exchange_rates.ico"))
             
        self.InitUI()
        self.Centre() 
        self.Show() 
    

    def InitUI(self): 
        panel = wx.Panel(self)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        fgs = wx.FlexGridSizer(4, 3, 10,40)
        
        title = wx.StaticText(panel, label = "КУРС К ГРИВНЕ")
        title.SetForegroundColour((255,255,255)) # set text color
        title.SetBackgroundColour((85,85,85)) # set text back color 
        buy = wx.StaticText(panel, label = "Покупка") 
        buy.SetForegroundColour((255,255,255)) # set text color
        buy.SetBackgroundColour((85,85,85)) # set text back color 
        sell = wx.StaticText(panel, label = "Продажа")
        sell.SetForegroundColour((255,255,255)) # set text color
        sell.SetBackgroundColour((85,85,85)) # set text back color 
        usd = wx.StaticText(panel, label = "ДОЛЛАР")
        usd.SetForegroundColour((255,255,255)) # set text color
        # usd.SetBackgroundColour((85,85,85)) # set text back color 
        usd_buy = wx.StaticText(panel, label = get_buy(response.json()[0]))
        usd_buy.SetForegroundColour((255,255,255)) # set text color
        # usd_buy.SetBackgroundColour((85,85,85)) # set text back color 
        usd_sell = wx.StaticText(panel, label = get_sell(response.json()[0]))
        usd_sell.SetForegroundColour((255,255,255)) # set text color
        # usd_sell.SetBackgroundColour((85,85,85)) # set text back color 
        eur = wx.StaticText(panel, label = "ЕВРО")
        eur.SetForegroundColour((255,255,255)) # set text color
        # eur.SetBackgroundColour((85,85,85)) # set text back color 
        eur_buy = wx.StaticText(panel, label = get_buy(response.json()[1]))
        eur_buy.SetForegroundColour((255,255,255)) # set text color
        # eur_buy.SetBackgroundColour((85,85,85)) # set text back color 
        eur_sell = wx.StaticText(panel, label = get_sell(response.json()[1]))
        eur_sell.SetForegroundColour((255,255,255)) # set text color
        # eur_sell.SetBackgroundColour((85,85,85)) # set text back color 
        rub = wx.StaticText(panel, label = "РУБЛЬ")
        rub.SetForegroundColour((255,255,255)) # set text color
        # rub.SetBackgroundColour((85,85,85)) # set text back color 
        rub_buy = wx.StaticText(panel, label = get_buy(response.json()[2]))
        rub_buy.SetForegroundColour((255,255,255)) # set text color
        # rub_buy.SetBackgroundColour((85,85,85)) # set text back color 
        rub_sell = wx.StaticText(panel, label = get_sell(response.json()[2]))
        rub_sell.SetForegroundColour((255,255,255)) # set text color
        # rub_sell.SetBackgroundColour((85,85,85)) # set text back color 
        
        fgs.AddMany([(title), (buy), (sell),  
                    (usd), (usd_buy), (usd_sell),
                    (eur), (eur_buy), (eur_sell),
                    (rub), (rub_buy), (rub_sell)])  

        fgs.AddGrowableRow(2, 1) 
        fgs.AddGrowableCol(1, 1)  
        hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 5) 
        panel.SetSizer(hbox)
        panel.SetBackgroundColour( ( 43, 43, 43 ) ) 


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)


    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Reload', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        self.frame = Example(None, title = 'Курс валют')
        dw, dh = wx.DisplaySize()
        w, h = self.frame.GetSize()
        x = dw - w
        y = dh - h - 35
        self.frame.SetPosition((x, y))
        self.frame.Show(True) 


    def on_hello(self, event):
        print ('Hello, world!')

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()
        

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    app = App(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
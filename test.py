import wx
import requests


response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")

def get_buy(obj):
    return obj.get('buy')

def get_sell(obj):
    return obj.get('sale')

  
class Example(wx.Frame): 
   
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title, size = (300, 140))
             
        self.InitUI()
        self.Centre() 
        self.Show() 
    

    def InitUI(self): 
        panel = wx.Panel(self)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        fgs = wx.FlexGridSizer(4, 3, 10,40)
        
        title = wx.StaticText(panel, label = "КУРС К ГРИВНЕ") 
        buy = wx.StaticText(panel, label = "Покупка") 
        sell = wx.StaticText(panel, label = "Продажа")
        usd = wx.StaticText(panel, label = "ДОЛЛАР")
        usd_buy = wx.StaticText(panel, label = get_buy(response.json()[0]))
        usd_sell = wx.StaticText(panel, label = get_sell(response.json()[0]))
        eur = wx.StaticText(panel, label = "ЕВРО")
        eur_buy = wx.StaticText(panel, label = get_buy(response.json()[1]))
        eur_sell = wx.StaticText(panel, label = get_sell(response.json()[1]))
        rub = wx.StaticText(panel, label = "РУБЛЬ")
        rub_buy = wx.StaticText(panel, label = get_buy(response.json()[2]))
        rub_sell = wx.StaticText(panel, label = get_sell(response.json()[2]))
        
        fgs.AddMany([(title), (buy), (sell),  
                    (usd), (usd_buy), (usd_sell),
                    (eur), (eur_buy), (eur_sell),
                    (rub), (rub_buy), (rub_sell)])  

        fgs.AddGrowableRow(2, 1) 
        fgs.AddGrowableCol(1, 1)  
        hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 5) 
        panel.SetSizer(hbox) 
        
app = wx.App() 
Example(None, title = 'Курс валют') 
app.MainLoop()
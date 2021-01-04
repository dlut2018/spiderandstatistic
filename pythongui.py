#coding : utf-8
import wx

input_goods_info = ""
input_data_num = 0
input_project_name = ""
input_else = ""

class MyWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"")
        self.panel = wx.Panel(self)


        self.topLbl = wx.StaticText(self.panel,-1,"自动获取京东商城信息工具")
        self.topLbl.SetFont(wx.Font(18,wx.SWISS,wx.NORMAL,wx.BOLD))

        self.nameLbl = wx.StaticText(self.panel,-1,"搜索词条:")
        self.name1 = wx.TextCtrl(self.panel,-1,"");

        self.addrLb1 = wx.StaticText(self.panel,-1,"爬取次数:")
        self.addr1 = wx.TextCtrl(self.panel,-1,"")


        self.phoneLbl = wx.StaticText(self.panel,-1,"项目名称:")
        self.phone = wx.TextCtrl(self.panel,-1,"");

        self.emailLbl = wx.StaticText(self.panel,-1,"备注:")
        self.email = wx.TextCtrl(self.panel,-1,"");

        #垂直的Sizer
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.topLbl,0,wx.ALL,5)
        mainSizer.Add(wx.StaticLine(self.panel),0,
                      wx.EXPAND|wx.TOP|wx.BOTTOM,5)

        #地址列
        addrSizer = wx.FlexGridSizer(cols = 2,hgap = 5,vgap = 5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(self.nameLbl,0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.name1,0,wx.EXPAND)
        addrSizer.Add(
            self.addrLb1,0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL
        )
        addrSizer.Add(self.addr1,0,wx.EXPAND)


        #水平嵌套


        #电话和电子邮箱
        addrSizer.Add(self.phoneLbl,0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.phone,0,wx.EXPAND)
        addrSizer.Add(self.emailLbl,0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.email,0,wx.EXPAND)

        #添加FLEX sizer
        mainSizer.Add(addrSizer,0,wx.EXPAND|wx.ALL,10)


        #按钮行
        self.button1 = wx.Button(self.panel,-1,"开始")
        self.button2 = wx.Button(self.panel,-1,"结束")
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20),1)
        btnSizer.Add(self.button1)
        btnSizer.Add((20,20),1)
        btnSizer.Add(self.button2)
        btnSizer.Add((20,20),1)

        mainSizer.Add(btnSizer,0,wx.EXPAND|wx.BOTTOM,10)

        self.panel.SetSizer(mainSizer)


        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

        self.Bind(wx.EVT_BUTTON,self.OnStart,self.button1)
        self.Bind(wx.EVT_TEXT,self.OnInput1,self.name1)
        self.Bind(wx.EVT_TEXT,self.OnInput2,self.addr1)
        self.Bind(wx.EVT_TEXT,self.OnInput3,self.phone)
        self.Bind(wx.EVT_TEXT,self.OnInput4,self.email)

    def OnStart(self,event):
        print("hello")

    def OnInput1(self,event):
        global input_goods_info
        input_goods_info = self.name1.GetValue()
        print(input_goods_info)

    def OnInput2(self,event):
        global input_data_num
        if type(eval(self.addr1.GetValue())) == int:
            input_data_num = (int)(eval(self.addr1.GetValue()))
        print(input_data_num)

    def OnInput3(self,event):
        global input_project_name
        input_project_name = self.phone.GetValue()
        print(input_project_name)

    def OnInput4(self,event):
        global input_else
        input_else = self.email.GetValue()
        print(input_else)


app = wx.PySimpleApp()
MyWindow().Show()
app.MainLoop()

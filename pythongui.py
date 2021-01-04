
#coding : utf-8
import wx

class MyWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"")
        panel = wx.Panel(self)


        topLbl = wx.StaticText(panel,-1,"自动获取京东商城信息工具")
        topLbl.SetFont(wx.Font(18,wx.SWISS,wx.NORMAL,wx.BOLD))

        nameLbl = wx.StaticText(panel,-1,"搜索词条:")
        name = wx.TextCtrl(panel,-1,"");

        addrLb1 = wx.StaticText(panel,-1,"爬取次数:")
        addr1 = wx.TextCtrl(panel,-1,"")


        phoneLbl = wx.StaticText(panel,-1,"项目名称:")
        phone = wx.TextCtrl(panel,-1,"");

        emailLbl = wx.StaticText(panel,-1,"备注:")
        email = wx.TextCtrl(panel,-1,"");

        #垂直的Sizer
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl,0,wx.ALL,5)
        mainSizer.Add(wx.StaticLine(panel),0,
                      wx.EXPAND|wx.TOP|wx.BOTTOM,5)

        #地址列
        addrSizer = wx.FlexGridSizer(cols = 2,hgap = 5,vgap = 5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(nameLbl,0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name,0,wx.EXPAND)
        addrSizer.Add(
            addrLb1,0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL
        )
        addrSizer.Add(addr1,0,wx.EXPAND)




        #水平嵌套


        #电话和电子邮箱
        addrSizer.Add(phoneLbl,0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(phone,0,wx.EXPAND)
        addrSizer.Add(emailLbl,0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(email,0,wx.EXPAND)

        #添加FLEX sizer
        mainSizer.Add(addrSizer,0,wx.EXPAND|wx.ALL,10)


        #按钮行
        button1 = wx.Button(panel,-1,"开始")
        button2 = wx.Button(panel,-1,"结束")
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20),1)
        btnSizer.Add(button1)
        btnSizer.Add((20,20),1)
        btnSizer.Add(button2)
        btnSizer.Add((20,20),1)

        mainSizer.Add(btnSizer,0,wx.EXPAND|wx.BOTTOM,10)

        panel.SetSizer(mainSizer)


        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)



app = wx.PySimpleApp()
MyWindow().Show()
app.MainLoop()

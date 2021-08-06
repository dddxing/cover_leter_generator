import wx
import datetime
import config
from fpdf_gen import PDF
from fpdf import FPDF
import fpdf
import os


class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # init frame
        self.init_frame()

    def init_frame(self):
        frame = MyFrame(parent=None, title='Cover Letter Generator', pos=(100, 100))
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX):
        super().__init__(parent=parent, title=title, pos=pos, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.on_init()

    def on_init(self):
        panel = MyPanel(parent=self)


class MyPanel(wx.Panel):
    p, c, t = config.position, config.company, config.type_

    def __init__(self, parent):
        super().__init__(parent=parent)

        # add a hello message to the panel
        company_name_text = wx.StaticText(self, id=wx.ID_ANY, pos=(20, 20), label="Company Name")
        # ID_ANY means that we don't care about the id

        self.company_textbox = wx.TextCtrl(parent=self, id=wx.ID_ANY, value="", pos=(20, 40))

        pos_name_text = wx.StaticText(self, id=wx.ID_ANY, pos=(20, 80), label="Position")
        # ID_ANY means that we don't care about the id

        self.position_textbox = wx.TextCtrl(parent=self, id=wx.ID_ANY, value="", pos=(20, 100))

        button = wx.Button(parent=self, label="Export PDF", pos=(20, 150))
        button.Bind(event=wx.EVT_BUTTON, handler=self.on_submit)

        self.radio_box = wx.RadioBox(parent=self, label="Focus", style=wx.RA_SPECIFY_ROWS,
                                     choices=["Robotics", "Data", "Manufacturing", "Mechanical"], pos=(200, 20))

    def on_close(self, event):
        self.Close()

    def on_submit(self, event):

        # {self.company_textbox.GetValue()} selects {self.radio_box.GetItemLabel(self.radio_box.GetSelection())}
        position = self.position_textbox.GetValue()
        company = self.company_textbox.GetValue()
        type_ = self.radio_box.GetItemLabel(self.radio_box.GetSelection())

        try:
            path = os.path.expanduser('~/Desktop/cover_letter/')
            print(path)
            filename = os.path.join(path, f'{datetime.date.today()}_{company}_{position}.pdf')
            p = PDF()
            PDF().create_cover_letter(filename, position, company, type_)
            ok = wx.MessageBox(f'Save as {filename}', 'Info', wx.OK | wx.ICON_INFORMATION)

        except fpdf.errors.FPDFException:
            wx.MessageBox('Cannot work twice', 'Error', wx.OK | wx.ICON_ERROR)

        except FileNotFoundError:
            wx.MessageBox('Cannot find path', 'Error', wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

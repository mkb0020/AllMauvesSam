#COLOR PALLETES FROM https://creativebooster.net/blogs/colors/mauve-color-palettes
# DUE TO DUPLICATES, SOME OF THE COLOR NAMES HAVE BEEN CHANGED

import sys
import os
import subprocess
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, ttk, messagebox, simpledialog, Label, Entry, Button, Tk
from tkinter import *

print("LOADED:", __name__)


AllMauves = [
    {"COLOR NAME":"Amethyst","HEX CODE":"#A55AFF","RGB":"165,90,255"},
    {"COLOR NAME":"AfricanViolet","HEX CODE":"#A786BF","RGB":"167,134,191"},
    {"COLOR NAME":"AfricanViolet2","HEX CODE":"#AA75AA","RGB":"170,117,170"},
    {"COLOR NAME":"HeatherPurple","HEX CODE":"#9779AB","RGB":"151,121,171"},
    {"COLOR NAME":"AirForceBlue","HEX CODE":"#5D8099","RGB":"93,128,153"},
    {"COLOR NAME":"BlueGray","HEX CODE":"#7098C0","RGB":"112,152,192"},
    {"COLOR NAME":"BlueMunsell","HEX CODE":"#388CA0","RGB":"56,140,160"},
    {"COLOR NAME":"ChineseViolet","HEX CODE":"#745B84","RGB":"116, 91, 132"},
    {"COLOR NAME":"Cinereous","HEX CODE":"#A99A93","RGB":"169,154,147"},
    {"COLOR NAME":"Claret","HEX CODE":"#730132","RGB":"115,1,50"},
    {"COLOR NAME":"CoolGray","HEX CODE":"#938FB7","RGB":"147,143,183"},
    {"COLOR NAME":"DarkPurple","HEX CODE":"#3D264C","RGB":"61,38,76"},
    {"COLOR NAME":"EnglishViolet","HEX CODE":"#523466","RGB":"82,52,102"},
    {"COLOR NAME":"EnglishViolet2","HEX CODE":"#5C406F","RGB":"92,64,111"},
    {"COLOR NAME":"FairyTale","HEX CODE":"#F3BED6","RGB":"243,190,214"},
    {"COLOR NAME":"FedBlue","HEX CODE":"#101460","RGB":"16,20,96"},
    {"COLOR NAME":"HookersGreen","HEX CODE":"#428076","RGB":"66,128,118"},
    {"COLOR NAME":"LavenderBlush","HEX CODE":"#EBE0EB","RGB":"235,224,235"},
    {"COLOR NAME":"LavenderFloral","HEX CODE":"#A279CD","RGB":"162,121,205"},
    {"COLOR NAME":"LavenderPink","HEX CODE":"#FFB0DA","RGB":"255,176,218"},
    {"COLOR NAME":"LavenderWeb","HEX CODE":"#D8D0DD","RGB":"216,208,221"},
    {"COLOR NAME":"Licorice","HEX CODE":"#100716","RGB":"16,7,22"},
    {"COLOR NAME":"Lilac","HEX CODE":"#D8ABD8","RGB":"216,171,216"},
    {"COLOR NAME":"Mauve","HEX CODE":"#E0B0FF","RGB":"224,176,255"},
    {"COLOR NAME":"Mauve1","HEX CODE":"#C89EFF","RGB":"200,158,255"},
    {"COLOR NAME":"Mauve2","HEX CODE":"#D1AEFC","RGB":"209,174,252"},
    {"COLOR NAME":"Mauve3","HEX CODE":"#D9BDF8","RGB":"217,189,248"},
    {"COLOR NAME":"MidnightBlue","HEX CODE":"#1D1F6B","RGB":"29,31,107"},
    {"COLOR NAME":"MountbattenPink","HEX CODE":"#A27E82","RGB":"162,126,130"},
    {"COLOR NAME":"OldRose","HEX CODE":"#BA7D85","RGB":"186,125,133"},
    {"COLOR NAME":"PaleDogwood","HEX CODE":"#E9CDCE","RGB":"233,205,206"},
    {"COLOR NAME":"PalePurple","HEX CODE":"#EADCF0","RGB":"234,220,240"},
    {"COLOR NAME":"PaynesGray","HEX CODE":"#365E6E","RGB":"54,94,110"},
    {"COLOR NAME":"Periwinkle","HEX CODE":"#B0B4FF","RGB":"176,180,255"},
    {"COLOR NAME":"Pink","HEX CODE":"#FFC0CB","RGB":"255,192,203"},
    {"COLOR NAME":"PinkLavender","HEX CODE":"#F0B8E5","RGB":"240,184,229"},
    {"COLOR NAME":"Plum","HEX CODE":"#8B3D80","RGB":"139,61,128"},
    {"COLOR NAME":"PlumWeb","HEX CODE":"#D393D3","RGB":"211,147,211"},
    {"COLOR NAME":"PompPower","HEX CODE":"#88659F","RGB":"136,101,159"},
    {"COLOR NAME":"RosyBrown","HEX CODE":"#D19FA7","RGB":"209,159,167"},
    {"COLOR NAME":"RoseQuartz","HEX CODE":"#A89DAE","RGB":"168,157,174"},
    {"COLOR NAME":"SlateBlue","HEX CODE":"#686FFC","RGB":"104,111,252"},
    {"COLOR NAME":"Teal","HEX CODE":"#008080","RGB":"0,128,128"},
    {"COLOR NAME":"Thistle","HEX CODE":"#C3B6CC","RGB":"195,182,204"},
    {"COLOR NAME":"TropicalIndigo","HEX CODE":"#918BFC","RGB":"145,139,252"},
    {"COLOR NAME":"UltraViolet","HEX CODE":"#725387","RGB":"114,83,135"},
    {"COLOR NAME":"Wisteria","HEX CODE":"#B697CB","RGB":"182,151,203"},
    {"COLOR NAME":"TeaRose","HEX CODE":"#F6C6C6","RGB":"246,198,198"},
    {"COLOR NAME":"MutedOrchid","HEX CODE":"#896E9B","RGB":"137,110,155"},
    {"COLOR NAME":"DeepAmethyst","HEX CODE":"#644A8B","RGB":"100,74,139"},
    {"COLOR NAME":"SoftCarnation","HEX CODE":"#FFC7FF","RGB":"255,199,255"},
    {"COLOR NAME":"LavenderMist","HEX CODE":"#D5B4EB","RGB":"213,180,235"},
    {"COLOR NAME":"LilacHaze","HEX CODE":"#C99CE6","RGB":"201,156,230"},
    {"COLOR NAME":"PaleIris","HEX CODE":"#F0BFFF","RGB":"240,191,255"},
    {"COLOR NAME":"DustyMauve2","HEX CODE":"#CDADC9","RGB":"205,173,201"},
    {"COLOR NAME":"VioletRose","HEX CODE":"#A978C9","RGB":"169,120,201"},
    {"COLOR NAME":"BlushPeony","HEX CODE":"#FCAEDD","RGB":"252,174,221"},
    {"COLOR NAME":"SmokyMauve","HEX CODE":"#70596F","RGB":"112,89,111"},
    {"COLOR NAME":"ThymeLilac","HEX CODE":"#92789B","RGB":"146,120,155"},
    {"COLOR NAME":"WarmWisteria","HEX CODE":"#B496C7","RGB":"180,150,199"},
    {"COLOR NAME":"SoftLilac","HEX CODE":"#D0BBD9","RGB":"208,187,217"},
    {"COLOR NAME":"WispPurple","HEX CODE":"#D2A7EE","RGB":"210,167,238"},
    {"COLOR NAME":"MutedLilac","HEX CODE":"#C2B7C9","RGB":"194,183,201"},
    {"COLOR NAME":"RoseDust","HEX CODE":"#D8A2A6","RGB":"216,162,166"},
    {"COLOR NAME":"PetalShadow","HEX CODE":"#DFB6D3","RGB":"223,182,211"},
    {"COLOR NAME":"MauveGlow","HEX CODE":"#C8A5DF","RGB":"200,165,223"},
    {"COLOR NAME":"PlumShadow","HEX CODE":"#967BB6","RGB":"150,123,182"},
    {"COLOR NAME":"PaleLavender","HEX CODE":"#E0C8F9","RGB":"224,200,249"},
    {"COLOR NAME":"GhostLilac","HEX CODE":"#DFDFF2","RGB":"223,223,242"},
    {"COLOR NAME":"IcyPeriwinkle","HEX CODE":"#CDC6FF","RGB":"205,198,255"},
    {"COLOR NAME":"SoftPeriwinkle","HEX CODE":"#A8A4E0","RGB":"168,164,224"},
    {"COLOR NAME":"BrightLilac","HEX CODE":"#B879E2","RGB":"184,121,226"},
    {"COLOR NAME":"ElectricLilac","HEX CODE":"#D396FC","RGB":"211,150,252"},
    {"COLOR NAME":"PaleOrchid","HEX CODE":"#E5C7E5","RGB":"229,199,229"},
    {"COLOR NAME":"MistyLavender","HEX CODE":"#E2CDF4","RGB":"226,205,244"},
    {"COLOR NAME":"DustyPeriwinkle","HEX CODE":"#8F93BA","RGB":"143,147,186"},
    {"COLOR NAME":"VintageLilac","HEX CODE":"#C0A5DA","RGB":"192,165,218"},
    {"COLOR NAME":"RoseHaze","HEX CODE":"#D7B3CE","RGB":"215,179,206"},
    {"COLOR NAME":"PeachMauve","HEX CODE":"#EEC0C2","RGB":"238,192,194"},
    {"COLOR NAME":"AquaMist","HEX CODE":"#C2FEFF","RGB":"194,254,255"},
    {"COLOR NAME":"LemonChiffon","HEX CODE":"#F5FFC2","RGB":"245,255,194"},
    {"COLOR NAME":"CottonCandyLilac","HEX CODE":"#E8C2FF","RGB":"232,194,255"},
    {"COLOR NAME":"PeachBlush","HEX CODE":"#FFD9C2","RGB":"255,217,194"},
    {"COLOR NAME":"MintGlow","HEX CODE":"#B5FFA8","RGB":"181,255,168"},
]


MauvesDF = pd.DataFrame(AllMauves)


MauveWedding = ["EnglishViolet", "Mauve", "Periwinkle", "LavenderPink", "Thistle"]
DarkMauve = ["Licorice", "DarkPurple", "EnglishViolet2", "UltraViolet", "PompPower"]
DustyMauve = ["ChineseViolet", "MutedOrchid", "HeatherPurple", "Wisteria", "LavenderMist"]
MauveNavy = ["MidnightBlue", "DeepAmethyst", "AfricanViolet", "SoftCarnation", "HookersGreen"]
MauvePink = ["MountbattenPink", "RosyBrown", "Pink", "PinkLavender", "Mauve"]
MauvePurple = ["Claret", "Plum", "LavenderFloral", "LilacHaze", "PaleIris"]
VintageMauve = ["PaynesGray", "CoolGray", "PaleIris", "DustyMauve2", "Cinereous"]
BlueMauve = ["FedBlue", "Mauve", "Amethyst", "Periwinkle", "SlateBlue"]
MauveBlush = ["VioletRose", "PlumWeb", "BlushPeony", "FairyTale", "PaleDogwood"]
MutedMauve = ["SmokyMauve", "ThymeLilac", "WarmWisteria", "SoftLilac", "LavenderBlush"]
MauveGrey = ["AfricanViolet", "WispPurple", "LavenderWeb", "MutedLilac", "RoseQuartz"]
MauveRose = ["OldRose", "RoseDust", "TeaRose", "PetalShadow", "MauveGlow"]
MauveLavender = ["PlumShadow", "Mauve", "PaleLavender", "GhostLilac", "IcyPeriwinkle"]
MauveTeal = ["Teal", "BlueMunsell", "BlueGray", "SoftPeriwinkle", "Mauve"]
MauveLilac = ["BrightLilac", "ElectricLilac", "TropicalIndigo", "Lilac", "PaleOrchid"]
LightMauve = ["Mauve1", "Mauve2", "Mauve3", "MistyLavender", "PalePurple"]
MauveSummer = ["AirForceBlue", "DustyPeriwinkle", "VintageLilac", "RoseHaze", "PeachMauve"]
PastelMauve = ["AquaMist", "LemonChiffon", "CottonCandyLilac", "PeachBlush", "MintGlow"]

PaletteMap = {
    "Mauve Wedding": MauveWedding,
    "Dark Mauve": DarkMauve,
    "Dusty Mauve": DustyMauve,
    "Mauve Navy": MauveNavy,
    "Mauve Pink": MauvePink,
    "Mauve Purple": MauvePurple,
    "Vintage Mauve": VintageMauve,
    "Blue Mauve": BlueMauve,
    "Mauve Blush": MauveBlush,
    "Muted Mauve": MutedMauve,
    "Mauve Grey": MauveGrey,
    "Mauve Rose": MauveRose,
    "Mauve Lavender": MauveLavender,
    "Mauve Teal": MauveTeal,
    "Mauve Lilac": MauveLilac,
    "Light Mauve": LightMauve,
    "Mauve Summer": MauveSummer,
    "Pastel Mauve": PastelMauve,
}

# ================================ HELPER TO CONVERT RGB TO HEX FOR TKINTER ================================
def RGB2Hex(RGBString):
    try:
        r, g, b = map(int, RGBString.split(","))
        return f"#{r:02x}{g:02x}{b:02x}"
    except Exception:
        return "#FFFFFF"

# ================================ MATCH PALETTE COLORS WITH HEX OR RGB CODES ================================
def GetPaletteCodes(PaletteName, ColorCode = "HEX"): # ARGUMENTS: PALETTE AND EITHER "HEX" OR "RGB" (CASE-INSENSITIVE) / RETURNS PANDAS DF WITH COLUMNS: COLOR NAME, CODE / CODE COLUMN WILL BE A STRING
    ColorNames = PaletteMap.get(PaletteName, [])
    CodeColumn = ColorCode.strip().upper()
    if CodeColumn not in {"HEX", "RGB"}:
        raise ValueError("ColorCode must be 'HEX' or 'RGB'")
    
    if CodeColumn == "HEX":
        LookupColumn = "HEX CODE"
    else:
        LookupColumn = "RGB"
    LookupColors = MauvesDF.set_index("COLOR NAME")[LookupColumn] #CREATE LOOKUP SERIES

    PaletteRows = []
    for Color in ColorNames:
        ColorValue = None
        if Color in LookupColors.index:
            ColorValue = LookupColors.loc[Color]
            if pd.isna(ColorValue):
                ColorValue = None
        PaletteRows.append({"COLOR NAME": Color, "CODE": ColorValue})
    
    PaletteDF = pd.DataFrame(PaletteRows)
    return PaletteDF

# ================================ DESKTOP APP ================================
class UserForm (tk.Tk):
    def __init__(self):
        super().__init__()  #  INITIALIZE TK WINDOW
        self.BackgroundDrip = "#C2CAE8" # BG COLOR
        self.title("MAUVE-lous")
        self.configure(bg=self.BackgroundDrip)
        self.LabelDrip = {"bg": "#C2CAE8", "fg": "#000000", "font": ("Arial", 12)} #LABEL STYLE
        self.ButtonDrip = {"bg": "#FFFFFF", "fg": "#000000", "font": ("Arial", 11)} #BUTTON STYLE

    def GetFormData(self): #INPUT FORM
        Input = {} # BLANK CONTAINER FOR INPUT / FILE THAT YOU WANT TO SEE
        def ClickSubmit(): #SUBMIT BUTTON
            Input["PaletteName"] = PaletteName.get() #SELECT WHICH FILE: CONTACT ME SUBMISSIONS, ORDERS SUBMISSIONS, SUGGESTIONS BOX, GUESTBOOK
            Input["ColorCode"] = ColorCode.get()
            self.withdraw()
            self.ShowPalette(Input)

        def ClickCancel(): #CANCEL BUTTON
            Input["cancelled"] = True
            self.quit()
            self.destroy()

        self.geometry("295x180")

        Label(self, text="Select Palette:", **self.LabelDrip).grid(row=0, column=0, pady=(15, 5), sticky="n") # LABEL

        PaletteName = ttk.Combobox( #DROP DOWN FOR PALETTES
            self,
            values=list(PaletteMap.keys()),
            state="readonly",
            font=("Arial", 11),
            width=20
        )
        PaletteName.grid(row=1, column=0, pady=5)
        PaletteName.current(0)

        ColorCode = ttk.Combobox( #DROP DOWN FOR HEX /RGB
            self,
            values=["HEX", "RGB"],
            state="readonly",
            font=("Arial", 11),
            width=20
        )
        ColorCode.grid(row=2, column=0, pady=5)
        ColorCode.current(0)

        ButtonFrame = tk.Frame(self, bg=self.BackgroundDrip)
        ButtonFrame.grid(row=3, column=0, pady=(15, 10))

        CancelButton = Button(ButtonFrame, text="CANCEL", width=12, command=ClickCancel, relief="raised", padx=10, pady=5, **self.ButtonDrip)
        CancelButton.pack(side="left", padx=6)

        SubmitButton = Button(ButtonFrame, text="SUBMIT", width=12, command=ClickSubmit, relief="raised", padx=10, pady=5, **self.ButtonDrip)
        SubmitButton.pack(side="left", padx=6)

        self.eval('tk::PlaceWindow . center')
        self.mainloop()
        return Input
    
    def ShowPalette(self, Input): # POPUP MESSAGE AFTER PALETTE AND HEX/RGB IS SELECTED
        PaletteDF = GetPaletteCodes(Input["PaletteName"], Input["ColorCode"])
        
        def ClickGoBack():
            PalettePopup.destroy()
            self.deiconify()

        def ClickOK(): # EXIT
            PalettePopup.destroy()
            sys.exit(0)
        
        PalettePopup = tk.Toplevel(self)
        PalettePopup.title(f"{Input['PaletteName']} Palette")
        PalettePopup.configure(bg=self.BackgroundDrip)
        PalettePopup.geometry("650x400")
        PalettePopup.resizable(True, True)

        PalettePopup.transient(self)   # NEW WINDOW APPEARS ON TOP OF PARENT
        PalettePopup.grab_set()        # BLOCK INTERACTION WITH MAIN WINDOW
        PalettePopup.focus_force()     # GRAB FOCUS
        PalettePopup.lift()            # RAISE ABOVE ALL WINDOWS

        MainFrame = tk.Frame(PalettePopup, bg=self.BackgroundDrip, padx=20, pady=20) #MAIN CONTAINER
        MainFrame.pack(fill="both", expand=False)

        tk.Label( # TITLE
            MainFrame,
            text=f"{Input['PaletteName']} - {Input['ColorCode']} Codes",
            bg=self.BackgroundDrip,
            fg="#000000",
            font=("Arial", 14, "bold")
        ).pack(pady=(0, 15))
        
        SwatchFrame = tk.Frame(MainFrame, bg=self.BackgroundDrip) # COLOR SWATCHES IN A ROW
        SwatchFrame.pack(pady=(0, 15), fill="none", expand=False)
        
        for idx, row in PaletteDF.iterrows():
            ColorFrame = tk.Frame(SwatchFrame, bg=self.BackgroundDrip)
            ColorFrame.pack(side="left", padx=8)
            if row["CODE"]:  # COLOR SWATCH
                ColorValue = row["CODE"]
                if Input["ColorCode"].upper() == "RGB": # CONVERT TO RGB TO HEX FOR TKINTER DISPLAY
                    ColorValue = RGB2Hex(ColorValue)
                ColorBox = tk.Frame(ColorFrame, bg=ColorValue, width=80, height=100, relief="solid", borderwidth=1)
                ColorBox.pack(fill="none", expand=False)
                ColorBox.pack_propagate(False)
        
        TextFrame = tk.Frame(MainFrame, bg="white", relief="solid", borderwidth=1) # TEXT AREA WITH COLOR INFO
        TextFrame.pack(fill="both", expand=False, pady=(0, 15))
        
        TextWidget = tk.Text(TextFrame, height=8, width=60, font=("Courier", 10), wrap="none", bg="white", fg="black")
        TextWidget.pack(side="left", fill="both", expand=False)
        
        Scrollbar = tk.Scrollbar(TextFrame, command=TextWidget.yview)
        Scrollbar.pack(side="right", fill="y")
        TextWidget.config(yscrollcommand=Scrollbar.set)
        
        for idx, row in PaletteDF.iterrows(): # FORMAT THE TEXT
            ColorName = row["COLOR NAME"]
            Code = row["CODE"] if row["CODE"] else "N/A"
            TextWidget.insert("end", f"{ColorName}: {Code}\n")
        
        TextWidget.config(state="normal")  # KEEP EDIT-ABLE FOR COPY/PASTE
 
        ButtonFrame = tk.Frame(MainFrame, bg=self.BackgroundDrip) # BUTTONS
        ButtonFrame.pack()
        
        GoBackButton = tk.Button(ButtonFrame, text="GO BACK", width=16, command=ClickGoBack, 
                                **self.ButtonDrip)
        GoBackButton.pack(side="left", padx=6)
        
        CloseButton = tk.Button(ButtonFrame, text="CLOSE", width=16, command=ClickOK, 
                               **self.ButtonDrip)
        CloseButton.pack(side="left", padx=6)
        
        self.eval('tk::PlaceWindow . center')
        PalettePopup.transient(self)
        PalettePopup.grab_set()

    def RunIt(self):
        FormData = self.GetFormData()
        if "cancelled" in FormData:
            sys.exit(0)


def GetColorsAPP(): # FOR DESKTOP APP
    PaletteColorCodes = UserForm()
    PaletteColorCodes.RunIt()


# ================================ FOR IMPORTING ================================
def GetColors(PaletteName: str, ColorFormat: str = "HEX"): # RETURNS AN OBJECT-LIKE RESULT WITH COLOR1, COLOR2, COLOR3, COLOR4, COLOR5 / CAN SELECT HEX OR RGB
    ColorFormat = ColorFormat.strip().upper()
    print(ColorFormat)
    if ColorFormat not in {"HEX", "RGB"}:
        raise ValueError("Color format must be 'HEX' or 'RGB'.")
    print(PaletteName)
    if PaletteName not in PaletteMap:
        raise KeyError(f"Palette '{PaletteName}' not found. Use ViewPaletteNames() to see available palettes.")

    # ✅ FIXED: Only 'HEX CODE' has the word 'CODE' in the column name
    LookUpColumn = "HEX CODE" if ColorFormat == "HEX" else "RGB"

    LookUp = MauvesDF.set_index("COLOR NAME")[LookUpColumn]

    PaletteColorList = []
    print(PaletteColorList)
    for Color in PaletteMap[PaletteName]:
        code = LookUp.get(Color)
        PaletteColorList.append(code)
    print(PaletteColorList)
    while len(PaletteColorList) < 5: # IF FEWER THAN 5 COLORS
        PaletteColorList.append(None)

    class PaletteColors:
        pass

    CodeResults = PaletteColors()
    for i, val in enumerate(PaletteColorList, start=1):
        setattr(CodeResults, f"Color{i}", val)
    return CodeResults


# ================================ GET PALETTE NAMES ================================
def ViewPaletteNames(): # PRINTS PALETTE NAMES
    print("\n Available Mauve Palettes:")
    for name in PaletteMap.keys():
        print("  •", name)
    print()


if __name__ == "__main__":
    GetColorsAPP()
    
    # ================================ TEST ================================
    #ViewPaletteNames()
    #example = GetColors("Mauve Wedding", "RGB")
    #print(example.Color1, example.Color2, example.Color3, example.Color4, example.Color5)

    # TO USE IN A SCRIPT: (EXAMPLE)
    #import sys
    #sys.path.append(r"C:\Users\mkb00\PROJECTS\GitRepos\AllColorsSam")
    #  from AllMauvesSam import GetPaletteColors, ViewPaletteNames
    # ViewPaletteNames() #VIEW ALL AVAILABLE PALETTES
    # colors = GetPaletteColors("Mauve Wedding", "RGB") # GRAB A PALETTE
    #print(colors.Color1)  # "82,52,102"
    #print(colors.Color2)  # "224,176,255"

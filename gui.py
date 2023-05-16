import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter import messagebox as mbox
from watermark import WatermarkAdder
import os


class UserInteract:
    def __init__(self):
        self.file_paths = None
        self.font_meter_value = 0
        self.text = None
        # ------------------------Window--------------------------------------------------#
        self.window = ttk.Window(title="Watermarker",
                                 size=(300,500),
                                 resizable=(False, False)
                                 )
        self.style = ttk.Style("superhero")

        # ------------------------Entry--------------------------------------------------#
        self.entry = ttk.Entry(self.window, font=("Segoe ui", 15),)
        self.entry.insert(0, "Enter text")
        self.entry.pack(pady=20)

        # ------------------------Meter--------------------------------------------------#
        self.font_meter = ttk.Meter(self.window,
                                    bootstyle="info",
                                    subtext="Font Size",
                                    interactive=True,
                                    amounttotal=400,
                                    amountused=20
                                    )

        self.font_meter.pack()

        # ------------------------Button--------------------------------------------------#
        self.import_button = ttk.Button(self.window,
                                        text="Select Files",
                                        command=self.import_files)
        self.import_button.pack(padx=50, pady=30)

        # ----------------------------------------------------------------------------------#
        # ----------------------------------------------------------------------------------#

        self.window.mainloop()

    def generator(self):
        '''Loops through the selected image files to add watermarks'''
        for filename in self.file_paths:
            if filename.endswith(".jpg") or filename.endswith("jpeg") or filename.endswith("png"):
                file = os.path.basename(filename)
                image_path_final= f"Images/{file}"
                image = WatermarkAdder(filename, self.text, self.font_meter_value, image_path_final)
        mbox.showinfo(title="Success", message="Watermark has been Successfully added")

    def import_files(self):
        '''Imports image files based on the users input'''
        self.font_meter_value = self.font_meter.amountusedvar.get()
        if self.entry.get().strip() != "" and self.font_meter_value !=0:
            self.file_paths = filedialog.askopenfilenames()  # Open the file dialog and return the selected file path
            self.text = self.entry.get()
            self.generator()
        else:

            mbox.showinfo(title="Invalid Entry", message="Text Field is empty")
            # Display error message if Text to be used for watermark isn't entered

# ------------------------------------------------------------------------------------------------------------------------------------------------------


window = UserInteract()





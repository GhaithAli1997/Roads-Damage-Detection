# image_viewer.py

import io
import os
import PySimpleGUI as sg
from PIL import Image
import torch

model = torch.hub.load( 'ultralytics/yolov5', 'custom', 'C:/Users/Madlen/Downloads/best.pt')
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
listimage=os.listdir(r'C:/Users/Madlen/Downloads/h')
i=len(listimage)
print(i)
def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [sg.Image(key="-IMAGE1-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
            sg.Button("road dedact")
        ],
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "road dedact":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                result=model(image)
                result.save()
                result.show()
               # global i
               # l=str(i)
               # listimage1=os.listdir(r'runs\detect')
               ## i1=len(listimage1)-1
               # l=str(i1)
               # image = Image.open(r'runs\detect\exp'+l+'\\China_MotorBike_001984.jpg')
                #i1+=1
              #  image.thumbnail((512, 512))
              #  bio = io.BytesIO()
              #  image.save(bio, format="png")
               # window["-IMAGE1-"].update(data=result)

    window.close()


if __name__ == "__main__":
    main()
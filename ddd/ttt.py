from PIL import Image
import matplotlib.pyplot as plt

def imggg():
    img = Image.open("./config/scanme.png")
    plt.figure(figsize=(4,4))
    plt.ion()
    plt.axis('off')
    plt.imshow(img)
    mnmn = plt.get_current_fig_manager()
    # mnmn.window.wm_geometry("+380+380")
    plt.pause(15)
    plt.ioff()
    plt.clf()
    plt.close()

if __name__ == "__main__" :
    imggg()
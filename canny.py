import cv2
from matplotlib import pyplot as plt

def main():
    #path="E:\Peru\engineering\Tecathlon 2018\data"
    frames=["10842","5518","4111","6905","4759"]
    for i in frames:
        imgpath="/home/pranava/frame"+i+".jpg"
        img=cv2.imread(imgpath,0)
        #img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    
        L1=cv2.Canny(img,35,280,L2gradient=False)
        L2=cv2.Canny(img,35,200,L2gradient=True)
    
        titles=['original image','L1 norm','L2 Norm']
        outputs=[img,L1,L2]
    
        for i in range(3):
            plt.subplot(1,3,i+1)
            plt.imshow(outputs[i],cmap='gray')
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
        plt.show()
main()

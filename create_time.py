import os, os.path, sys
from glob import glob
cPath = os.getcwd()
time_gap = 1.0/3.0
print("time gap: " + str(time_gap))
print("loading: "+ sys.argv[1])
relative_path = sys.argv[1]

images = glob(relative_path + "/image_lcam_front/*.png")
images.sort()

with open(relative_path + "/times.txt","w") as wfile:
    image_num = len([name for name in os.listdir(relative_path+'/image_lcam_front') if name.endswith(".png")])
    print(image_num)
    times = 0.0
    
    for i, path in enumerate(images):
        image_path = os.path.split(path)[-1]
        wfile.write(str(times)+"\t"+image_path+"\n")
        times += time_gap

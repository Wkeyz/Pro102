import cv2
import dropbox
import time
import random


def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result= False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def upload_files(img_name):
       
    access_token="sl.AhhIkrRw9wAFhmHjgxsBu1gP8ZqN-z26qhuweF5QQr_WQQjgUAwf1Cm3JaSPvhGaozgT-xGnyKY93-qwmmS2XbBam0Jr5opHn_vNx1HLSYlRDtgp-WbutmgsPrehYJ2Gl16a5fM"
    file = img_counter
    file_from = file
    file_to ="/newfolder/" + (img_name)
    dbx = dropbox.dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while (True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_files(name)
            
main()
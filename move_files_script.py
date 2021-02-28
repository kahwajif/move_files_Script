from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os, json, time, random

#directories
download_dir = "C:/Users/feras/Downloads" #folder we are tracking
picture_dir = "C:/Users/feras/OneDrive/Pictures"
video_dir = "C:/Users/feras/Videos"
music_dir = "C:/Users/feras/Music"
documents_dir = "C:/Users/feras/OneDrive/Documents"

#file extensions
pic_ext = ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".psd", ".PNG"
vid_ext = ".wmv", ".amv", ".mp4", ".mov", ".flv", ".webm", ".mkv"
mus_ext = ".wav", ".aa", ".aiff", ".alac", ".m4p", ".mp3", ".wma"
doc_ext = ".pdf", ".doc", ".docx", ".xlsx", ".xls", ".ppt", ".pptx", ".txt", ".html"

#responds to file changes in directory
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(download_dir):
            time.sleep(0.25)#without this time delay, downloaded files wont save
            #move pictures
            if any(ext in file_name for ext in pic_ext):
                new_name = self.file_exists(picture_dir,file_name)
                src = download_dir + "/" + file_name
                os.rename(src, picture_dir + "/" + new_name)
            
            #move videos
            elif any(ext in file_name for ext in vid_ext):
                new_name = self.file_exists(video_dir,file_name)
                src = download_dir + "/" + file_name
                os.rename(src, video_dir + "/" + new_name)
            #move music    
            elif any(ext in file_name for ext in mus_ext):
                new_name = self.file_exists(music_dir,file_name)
                src = download_dir + "/" + file_name
                os.rename(src, music_dir + "/" + new_name)
            
            '''
            #move documents
            elif any(ext in file_name for ext in doc_ext):
                src = download_dir + "/" + file_name
                os.rename(src, documents_dir + "/" + file_name)
            '''

    #if file name exists, generate random number & add before file name
    def file_exists(self, direct, file_name):
        file_exists = os.path.isfile(direct + "/" + file_name)
        if file_exists:
            new_name = str(random.randrange(100)) + "_" + file_name
            return new_name
        else:
            return file_name

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, download_dir, recursive = True)
observer.start()

try:
   while True:
            time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()

#have the script run on startup
import os
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *

PATH = "C:/Users/Adinar/Desktop/ytb project/Video"
# Fonction pour télécharger la vidéo depuis YouTube
def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first() 
    filename = stream.default_filename
    stream.download(PATH)
    return PATH+"/"+filename

# Fonction pour découper la vidéo en clips de 1 minute
def split_video(filename):
    clip = VideoFileClip(filename)
    duration = clip.duration
    start = 0
    end = 60
    counter = 1
    while start < duration:
        try:
            clip_name = os.path.splitext(filename)[0] + '_part' + str(counter) + '.mp4'
            subclip = clip.subclip(start, end)
            # Ajouter le texte de la partie
            txt_clip = (TextClip('Partie ' + str(counter), fontsize=30, color='white', bg_color='black')
                        .set_position(('center', 'bottom')).set_duration(end - start))
            result = CompositeVideoClip([subclip, txt_clip])
            result.write_videofile(clip_name, codec='libx264')
            start += 60
            end += 60
            if end > duration:
                end = duration
            counter += 1
        except:
            break
    clip.close()

# Exemple d'utilisation
url = input("Entrez l'URL de la vidéo YouTube : ")
filename = download_video(url)
split_video(filename)
print("La vidéo a été téléchargée et découpée en clips de 1 minute avec un texte de partie ajouté.")
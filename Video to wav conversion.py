import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

path = video_con
video = mp.VideoFileClip(path)
video.audio.write_audiofile("C:/xampp/htdocs/img/upload/videoplayback.mp3")

sound = AudioSegment.from_mp3("C:/xampp/htdocs/img/upload/videoplayback.mp3")
text=sound.export("C:/xampp/htdocs/img/upload/videoplayback.wav", format="wav")

#save the downloaded videos in desired folder.

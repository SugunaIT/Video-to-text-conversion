import pytube
SAVE_PATH = "C:/Users/intel/.spyder-py3/mp4-mp3" #to_do
print('Enter the URL')
link = input()
yt = pytube.YouTube(link)
stream = yt.streams.first()
video_con=stream.download()

try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Some modules are missing...{}".format(e))

url = input("Enter your url : ")
yt = YouTube(url)
y = yt.streams.filter(only_audio=True).first().download()


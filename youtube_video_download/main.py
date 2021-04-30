try:
    from pytube import YouTube
    
except Exception as e:
    print("Some modules are missing...{}".format(e))

url = input("Enter your url : ")

yt = YouTube(url).streams.first().download()
print(yt)



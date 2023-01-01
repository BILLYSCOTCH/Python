from pytube import YouTube
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There's been an error")
    print("The video has been downloaded")

link= input("Paste the youtube link here: ")
Download(link)
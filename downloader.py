from pytube import YouTube


link = input("Enter the link of YouTube video you want to download:  ")
link ='https://www.youtube.com/watch?v=668nUCeBHyY'
yt = YouTube(link)


print("Title: ",yt.title)
print("Length of video: ",yt.length)

ls = yt.streams.filter(progressive=True,file_extension='mp4').get_highest_resolution()

print("Downloading...")
ys.download()
print("Download completed!!")
x=input()

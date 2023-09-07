from pytube import YouTube

# where to save.
destination = r"C:\Users\snehs\OneDrive\Desktop\hackathon"
# link of the video to be downloaded
video_link = "https://www.youtube.com/watch?v=fdubeMFwuGs"

try:
    video = YouTube(video_link)
    # filtering the audio. File extension can be mp4/webm
    # You can see all the available streams by print(video.streams)
    #try changing file extension type to get the file of the disred fromat
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    audio.download(destination)
    print('Download Completed!')

except:
    print("Connection Error")  # to handle exception



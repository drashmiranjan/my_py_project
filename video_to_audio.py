
# hyy there today i coverting a video file into an audiofile

import moviepy.editor

vid_path = "D:/project/unique/Lyrics_- Is Dard-E-Dil Ki Sifarish Ab Karde Koi Yahan _ Mohammad I, Gajendra V _ Mithoon _ Yaariyan.mp4"

videos = moviepy.editor.VideoFileClip(vid_path)

# now we create a audio file and extract the audio from the video
audio_file = videos.audio
audio_file.write_audiofile("mysong.mp3")

print("Completed")


                                  # Thank You
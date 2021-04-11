from __future__ import unicode_literals
import youtube_dl
import moviepy.editor
from prompt_toolkit.shortcuts import message_dialog


def youtube_download():

    ydl_options = {}

    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=dP15zlyra3c'])


def audio_extract():

    video = moviepy.editor.VideoFileClip(input("Please enter the file of video to convert"))
    audio = video.audio
    audio.write_audiofile("output.mp3")


if __name__ == "__main__":
    message_dialog(title='Hi', text='Do you wanna click ok?\nPress ENTER to continue.').run()

import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import string
import whisper


class VideoTextExtractor:
    def __init__(self):
        self.text = ""

    @staticmethod
    def get_ytid(url):
        from urllib.parse import urlparse
        url_data = urlparse(url)
        ytid = url_data.query[2:]
        return ytid

    @staticmethod
    def clean_title(title):
        for char in string.punctuation:
            title = title.replace(char, ' ')
            title = title.replace(' ','_')
        return title

    def from_yt_transcript(self, url):
        yt = YouTube(url)
        title = str(yt.title)
        title = VideoTextExtractor.clean_title(title)
        ytid = VideoTextExtractor.get_ytid(url)
        transcript = YouTubeTranscriptApi.get_transcript(ytid)
        finale_text = ''
        for text in transcript:
            finale_text += text['text']
            finale_text += ' '
        self.text = finale_text
        return self.text

    def from_url_without_transcript(self, url):
        model = whisper.load_model('medium')
        yt = YouTube(url)
        title = str(yt.title)
        title = VideoTextExtractor.clean_title(title)
        streams = yt.streams.filter(only_audio=True)
        stream = streams.first()
        file_path = title + '.mp4'
        stream.download(filename=file_path)
        output = model.transcribe(file_path)
        self.text = output['text']
        return self.text

    def text_from_local(self, file_path):
        model = whisper.load_model('medium')
        output = model.transcribe(file_path)
        self.text = output['text']
        return self.text

    def save(self, file_path):
        with open(file_path, 'w') as f:
            f.write(self.text)


# extractor = VideoTextExtractor()
# transcript_text = extractor.from_yt_transcript("youtube_video_url")
# extractor.save("transcript_text.txt")

# # text_from_url = extractor.from_url_without_transcript("youtube_video_url")
# # extractor.save("text_from_url.txt")

# # text_from_local_file = extractor.text_from_local("local_video_file_path")
# # extractor.save("text_from_local.txt")

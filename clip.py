import os
import time

class Clip:
    start: time
    end: time
    link: str
    audio_file: str | None
    video_file: str | None
    merge_file: str | None

    def __init__(self, link: str, interval: [time, time]):
        """
        Represents a 'clip', a snippet of a video.
        link: The link to the complete YouTube video in question.
        interval: A continous time interval of the clip for the video.

        raises Exception: invalid time interval (start < 0, start >= end)
        """
        start, end = interval
        
        # basic sanity check: cannot check video length due to lack of YouTube API access
        if not start or not end or start >= end:
            raise Exception("Clip constructor: Invalid interval provided.")
        
        self.start = start
        self.end = end
        self.link = link
        
    def download_clip(self, audio_format: str, video_format: str) -> bool:  
        """
        Downloads clip in given quality and returns True if successful.
        """
        self.audio_file = self.__download_audio(self, audio_format)
        self.video_file = self.__download_video(self, video_format)

        if not self.audio_file:
            raise Exception("download_clip: Failed to download audio file.")
        
        if not self.video_file:
            raise Exception("download_clip: Failed to download video file.")

        return True
    
    def __download_audio(self, audio_format: str) -> str | None:
        return ""
    
    def __download_video(self, video_format: str) -> str | None:
        return ""
    
    def merge_clip(self) -> bool:
        if not (self.audio_file and os.path.isfile(self.audio_file)):
            raise Exception("merge_clip: No audio file found - audio file needed for merging clips.")

        if not (self.video_file and os.path.isfile(self.video_file)):
            raise Exception("merge_clip: No video file found - video file needed for merging clips.")
        
        if self.merge_file and os.path.isfile(self.merge_file):
            raise Exception("merge_clip: Clip is already merged. Merged clip is found at " + self.merge_file)
        
        return False
    
    def is_downloaded(self):
        return self.audio_file is not None and self.video_file is not None

    def is_merged(self):
        return self.merge_file is not None

"""Define useful objects to handle data
"""

class Video:
    """
    Class that contains information about a Youtube video.

    ATTRIBUTES
    ----------
    id: str
        The video id.
    title: str
        The video title.

    METHODS
    -------
    get_watch_url:
        Return the url to watch the video.
    get_embed_url:
        Return the url of the video for embedding. 
    """
    
    def __init__(self, id: str, title: str) -> None:
        self.id = id
        self.title = title

    __yt_watch_url = "https://youtube.com/watch?v="

    def get_watch_url(self) -> str:
        """
        RETURNS
        -------
        str
            The url to watch the video.
        """
        return self.__yt_watch_url + self.id

    __yt_embed_url = "https://youtube.com/embed/"

    def get_embed_url(self) -> str:
        """
        RETURNS
        -------
        str
            The url of the video for embedding.
        """
        return self.__yt_embed_url + self.id
    
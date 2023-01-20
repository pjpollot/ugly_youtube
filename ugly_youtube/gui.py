"""Define a simple GUI to watch the videos.
"""

from typing import List
from .objects import Video

def __save_string_to_file(filename: str, content: str) -> None:
    with open(filename, mode="w") as file:
            file.write(content)

def from_videos_to_ugly_html(videos: List[Video], filename: str = None, width: int = 600, height: int = 400) -> str:
    """
    PARAMETERS
    ----------
    videos: List[Video]
        The videos to embed in html.
    filename: str, optional
        Save the generated html into a file.
    width: int, optional
        The width of the window.
    height: int, optional
        The height of the window.

    RETURNS
    -------
    str
        The html script that prints the videos.
    """
    html = f"<h1>{len(videos)} search results</h1>\n"
    for video in videos:
        html += f'''
            <h2>{video.title}</h2>
            <iframe src="{video.get_embed_url()}" width={width} height={height}></iframe>
        '''
    if filename is not None:
        __save_string_to_file(filename, html)
    return html

def from_videos_to_ugly_markdown(videos: List[Video], filename: str = None) -> str:
    """
    PARAMETERS
    ----------
    videos: List[Video]
        The videos to embed in html.
    filename: str, optional
        Save the generated list into a file.

    RETURNS
    -------
    str
        The videos list (but in string format).
    """
    s = f"# {len(videos)} search results\n"
    for video in videos:
        s += f"## {video.title}\n*link:* {video.get_watch_url()}\n\n"
    if filename is not None:
        __save_string_to_file(filename, s)
    return s
import os
from ugly_youtube import UglyYoutube
from ugly_youtube.gui import from_videos_to_ugly_html, from_videos_to_ugly_markdown

youtube_api_key = "INSERT YOU API KEY HERE"

query = "INSERT A TOPIC YOU LIKE"
numer_of_queries = 10 # from 1 to 50

html_filename = "results.html"
md_filename = "results.md"

if __name__ == "__main__":
    yt = UglyYoutube(youtube_api_key)
    videos = yt.search(query)

    from_videos_to_ugly_html(videos, html_filename)
    from_videos_to_ugly_markdown(videos, md_filename)
    print(f'''
        Two files generated:
        - {os.path.abspath(html_filename)} 
        - {os.path.abspath(md_filename)}
        Pick the one you like!
    ''')
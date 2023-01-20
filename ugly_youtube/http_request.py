import requests
from requests.models import Response

from typing import List

class UglyYoutube:
    """
    The main class of the module. 
    
    Fetch research results of videos from Youtube API, but requires an API key to make it work.
    You can create your own key from https://console.cloud.google.com/.

    Attributes
    ----------
    api_key: str
        The key to use Youtube API v3.

    METHODS
    -------
    search
        Return videos based on a certain topic (= query).
    """

    def __init__(self, api_key: str) -> None:
        self.key = api_key

    @staticmethod
    def check_response_validity(response: Response) -> None:
        """Check whether or not the API call has been successful.

        Parameters
        ----------
        response: Response
            the response to the API call.
        
        RAISE
        -----
            HTTPError
        """
        if response.status_code // 100 != 2:
            # response code different from 2xx means an error occured
            # error_logs = json.dumps(response.json(), indent=1)
            raise Exception(
                f'''Status code {response.status_code} for {response.request.method} request at {response.url}.

                --> {response.json()["error"]["message"]}
                '''
            )


    def search(self, search_topic: str, max_results: int = 10) -> List[dict]:
        """GET https://www.googleapis.com/youtube/v3/search
        
        Parameters
        ----------
        search_topic: str
            The search topic. Example: "Pokemon Ruby Nuzlocke challenge"
        max_results: int
            The number of results to show. Must be between 1 and 50. 
            If higher than 50 the API will only return 50 results.

        Returns
        -------
        List[dict]
            List of search results.
        """
        request_url = "https://www.googleapis.com/youtube/v3/search"
        arguments = {
            "part": "id, snippet",
            "type": "video",
            "key": self.key,
            "q": search_topic,
            "maxResults": max_results,
        }
        results = requests.get(url=request_url, params=arguments)
        self.check_response_validity(results)
        videos = []
        for search_result in results.json()["items"]:
            videos.append(
                {
                    "id": search_result["id"]["videoId"],
                    "title": search_result["snippet"]["description"],
                }
            )
        return videos

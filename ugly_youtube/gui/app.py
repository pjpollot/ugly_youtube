from flask import Flask, render_template, request
from ..http_request import UglyYoutube

class UglyGUIInterface:
    """
    GUI interface for ugly Youtube.

    ATTRIBUTES
    ----------
    yt_api: UglyYoutube
        The youtube api.
    app: Flask
        The web application.

    METHODS
    -------
    launch_application: 
        Launch the web application.
    """

    def __init__(self, yt_api: UglyYoutube) -> None:
        self.yt_api = yt_api

        self.app = Flask(__name__)

        @self.app.route("/", methods=["GET", "POST"])
        def index():
            context = dict()
            if request.method == "POST":
                context["query"] = request.form["query"]
                context["videos"] = self.yt_api.search(
                    search_topic=context["query"], 
                    max_results=50
                )
            return render_template("index.html", **context)
    
    def launch_application(self, **options) -> None:
        """
        PARAMETERS
        ----------
        options: dict
            Are the same as Flask.run(**options)
        """
        self.app.run(**options)
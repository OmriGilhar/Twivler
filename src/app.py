from flask import Flask, render_template
from src import check_twitch

app = Flask(__name__)


@app.route('/')
def index():
    client_id, client_secret = check_twitch.get_client_id()
    client = check_twitch.create_client(client_id, client_secret)
    stream_detail = check_twitch.pull_live_streams_by_game(client, 'Dota 2', 1)
    return render_template(
        'index.html',
        channel_name=str(stream_detail[0]['channel']['name'])
    )

# opens on http://localhost:5000


if __name__ == "__main__":
    app.run(debug=True)

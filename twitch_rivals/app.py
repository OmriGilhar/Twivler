from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from twitch_rivals import twitchlib
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bushkape'

client_id, client_secret = twitchlib.get_client_id()
client_v5 = twitchlib.create_client_v5(client_id)
client_helix = twitchlib.create_client_helix(client_id)
top_games = twitchlib.get_top_games(client_v5, 10, 0)
top_games = [twitchlib.create_game_info(game_obj) for game_obj in top_games]
top_games_list = twitchlib.create_game_list(top_games)


class SearchForm(FlaskForm):
    game_name = StringField('')
    submit = SubmitField('Go')


@app.route('/')
def index(selected_game='FIFA 20'):
    streams = twitchlib.pull_live_streams_by_game(client_v5, selected_game, 1)
    # stream_info = twitchlib.create_stream_info(streams[0])
    channel_info = twitchlib.create_channel_info(streams[0]['channel'])

    return render_template(
        'index.html',
        channel_name=channel_info.display_name
    )


@app.route('/game/')
def game():
    channel_info = None
    game_name = request.args.get('game')
    try:
        streams = twitchlib.pull_live_streams_by_game(client_v5, game_name, 1)
        if not streams:
            channel_info = twitchlib.create_dummy_channel_info()
        else:
            # stream_info = twitchlib.create_stream_info(streams[0])
            channel_info = twitchlib.create_channel_info(streams[0]['channel'])
            if next((False for game_dict in top_games_list if game_dict["value"] == game_name), True):
                game_obj = client_helix.get_games(None, game_name)
                top_games_list.append({'value': game_obj[0]['name'], 'data': None})
    except AttributeError as e:
        print("except", e)
    return render_template(
        'index.html',
        channel_name=channel_info.display_name
    )


@app.route("/search/<string:box>")
def process(box):
    suggestions = []
    global top_games
    query = request.args.get('query')
    print(query)
    # TODO : https://opensource.google/projects/pygtrie Add prefix tree.
    if box == 'names':
        for game_dict in top_games_list:
            if re.search(query, game_dict['value'], re.IGNORECASE):
                suggestions.append(game_dict)
    return jsonify({"suggestions": suggestions})


@app.route('/search_game', methods=['GET', 'POST'])
def search_game():
    channel_info = twitchlib.create_dummy_channel_info()
    games = twitchlib.get_top_games(client_v5)
    games = [twitchlib.create_game_info(game_obj) for game_obj in games]
    games_info = [twitchlib.create_game_info(game_obj) for game_obj in games]
    game_names = [game_info.name for game_info in games_info]

    # Game search - updates stream_detail through POST method
    form = SearchForm()
    if form.validate_on_submit():
        streams = twitchlib.pull_live_streams_by_game(
            client_v5, form.game_name.data, 1)
        # stream_info = twitchlib.create_stream_info(streams[0])
        channel_info = twitchlib.create_channel_info(streams[0]['channel'])
    return render_template(
        'search_game.html',
        channel_name=channel_info.display_name,
        form=form,
        game_names=game_names
    )


@app.route("/select_game", methods=['GET', 'POST'])
def select_game():
    selected_game = request.form.get('game_select')
    return index(selected_game)


if __name__ == "__main__":
    app.run(debug=True)

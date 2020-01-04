from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from twitch_rivals import check_twitch

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bushkape'

client_id, client_secret = check_twitch.get_client_id()
client = check_twitch.create_client(client_id, client_secret)


class SearchForm(FlaskForm):
    game_name = StringField('')
    submit = SubmitField('Go')


@app.route('/')
def index(selected_game='FIFA 20'):
    streams = check_twitch.pull_live_streams_by_game(client, selected_game, 1)
    stream_info = check_twitch.create_stream_info(streams[0])
    channel_info = check_twitch.create_channel_info(streams[0]['channel'])

    return render_template(
        'index.html',
        channel_name=channel_info.display_name
    )


@app.route('/search_game', methods=['GET', 'POST'])
def search_game():
    channel_info = check_twitch.create_dummy_channel_info()
    games = check_twitch.get_top_games(client)
    games_info = [check_twitch.create_game_info(game) for game in games]
    game_names = [game_info.name for game_info in games_info]

    # Game search - updates stream_detail through POST method
    form = SearchForm()
    if form.validate_on_submit():
        streams = check_twitch.pull_live_streams_by_game(client, form.game_name.data, 1)
        stream_info = check_twitch.create_stream_info(streams[0])
        channel_info = check_twitch.create_channel_info(streams[0]['channel'])
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

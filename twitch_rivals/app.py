from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from twitch_rivals import check_twitch

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bushkape'


class SearchForm(FlaskForm):
    game_name = StringField('Game')
    submit = SubmitField('Go')


@app.route('/')
def index():
    client_id, client_secret = check_twitch.get_client_id()
    client = check_twitch.create_client(client_id, client_secret)
    stream_detail = check_twitch.pull_live_streams_by_game(client, 'FIFA 20', 1)

    return render_template(
        'index.html',
        channel_name=str(stream_detail[0]['channel']['name'])
    )


@app.route('/search_game', methods=['GET', 'POST'])
def search_game():
    client_id, client_secret = check_twitch.get_client_id()
    client = check_twitch.create_client(client_id, client_secret)
    stream_detail = [{'channel': {'name': 'None'}}]

    # Game search - updates stream_detail through POST method
    form = SearchForm()
    if form.validate_on_submit():
        stream_detail = check_twitch.pull_live_streams_by_game(client, form.game_name.data, 1)
    return render_template(
        'search_game.html',
        channel_name=str(stream_detail[0]['channel']['name']),
        form=form
    )
# opens on http://localhost:5000


if __name__ == "__main__":
    app.run(debug=True)

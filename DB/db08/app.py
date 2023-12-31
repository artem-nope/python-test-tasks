from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///besteveralbums_m2m.sqlite3'
app.config['SQLALCHEMY_ECHO'] = False
db.init_app(app)


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.Integer)
    charts = db.Column(db.Integer)
    img = db.Column(db.String)
    artist_id = db.Column(db.ForeignKey('artists.id'))
    artist = db.relationship('Artist', backref='albums')

    def __repr__(self):
        return self.name


assoc = db.Table(
    'artists_genres',
    db.Column('artist_id', db.ForeignKey('artists.id')),
    db.Column('genre_id', db.ForeignKey('genres.id'))
)


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    img = db.Column(db.String)
    # albums field
    genres = db.relationship('Genre', secondary=assoc, backref='artists')

    def __repr__(self):
        return self.name


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # artists field

    def __repr__(self):
        return self.name


@app.route("/")
def index():
    # artists = db.session.query(Artist).all()
    artists = (db.session.query(Artist,
                               func.count(Album.id),
                               func.avg(Album.charts).label('avg_charts'))
               .select_from(Artist)
               .join(Album.artist)
               .group_by(Artist.id)
               .order_by(desc('avg_charts'))
               .all())
    genres = db.session.query(Genre).order_by(Genre.name).all()
    top_albums = (db.session.query(Album, Artist)
                  .select_from(Album)
                  .join(Artist.albums)
                  .order_by(Album.charts.desc())
                  .limit(5))
    return render_template(
        template_name_or_list='index.html',
        artists=artists,
        genres=genres,
        top_albums=top_albums
    )


@app.route("/artist/<int:pk>")
def artist_detail(pk: int):
    artist = Artist.query.get(pk)

    return render_template(
        template_name_or_list='artist.html',
        artist=artist
    )


@app.route("/genre/<int:pk>")
def genre_detail(pk: int):
    genre = Genre.query.get(pk)

    return render_template(
        template_name_or_list='genre.html',
        genre=genre
    )


@app.route("/top-albums")
def top_albums():
    top_albums = (db.session.query(Album, Artist)
                  .select_from(Album)
                  .join(Artist.albums)
                  .order_by(Album.charts.desc())
                  .limit(5))

    return render_template(
        template_name_or_list='top-albums.html',
        top_albums=top_albums
    )


@app.route("/add-album", methods=['POST'])
def add_album():
    name = request.form.get('name')
    year = request.form.get('year')
    charts = request.form.get('charts')
    img = request.form.get('img')
    pk = request.form.get('pk')
    # print(request.form)
    # print([name, year, charts, img, pk])
    if name and year and charts and img:
        new_album = Album(
            name=name,
            year=year,
            charts=charts,
            img=img,
            artist_id=pk
        )
        db.session.add(new_album)
        db.session.commit()
    else:
        print("Not enough data to create a new album")
    # return redirect(url_for('index'))
    return redirect(url_for('artist_detail', pk=pk))


@app.route("/add-genre", methods=['POST'])
def add_genre():
    name = request.form.get('name')
    if name:
        new_genre = Genre(
            name=name
        )
        db.session.add(new_genre)
        db.session.commit()
    else:
        print("Not enough data to create a new genre")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)


# add new genre
# one python instance
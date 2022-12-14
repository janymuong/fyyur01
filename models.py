from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#Models-->Artist, Venue, Show:

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(120), nullable=False)
    shows = db.relationship('Show', backref='artists', lazy=True, cascade='all,delete')
    
    def __repr__(self):
        return f'<Artist ID: {self.id}, Artist name: {self.name}>'


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(120), nullable=False)
    shows = db.relationship('Show', backref='venues', lazy=True, cascade='all,delete')
    
    def __repr__(self):
        return f'<Venue ID: {self.id}, Venue name: {self.name}>'
    
    
class Show(db.Model):
    __tablename__ = 'show'
      
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    start_time = db.Column(db.DateTime())
    
    def __repr__(self):
        return f'<Show ID: {self.id}, Show Begins at: {self.start_time}>'
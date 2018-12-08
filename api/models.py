from api import db


class Project(db.Model):
    """This class represents the project table."""

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    email = db.Column(db.String(255))
    short_description = db.Column(db.String(255))
    description = db.Column(db.String(255))
    url = db.Column(db.String(255))
    creator_name = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    instagram = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    portfolio = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    status = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    page_views = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, title, email, short_description, description, url, creator_name, twitter, instagram, facebook, portfolio, slug):
        """initialize with name."""
        self.title = title
        self.email = email
        self.short_description = short_description
        self.description = description
        self.url = url
        self.creator_name = creator_name
        self.twitter = twitter
        self.instagram = instagram
        self.facebook = facebook
        self.portfolio = portfolio
        self.slug = slug
        self.status = 'submitted'
        self.page_views = 0

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Project.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Project: {}>".format(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'email': self.email,
            'short_description': self.short_description,
            'description': self.description,
            'url': self.url,
            'creator_name': self.creator_name,
            'twitter': self.twitter,
            'instagram': self.instagram,
            'facebook': self.facebook,
            'portfolio': self.portfolio,
            'image_url': self.image_url,
            'status': self.status,
            'slug': self.slug,
            'page_views': self.page_views,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }
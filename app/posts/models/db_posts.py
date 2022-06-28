from app.database import db
import datetime


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(500), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    comment_rel = db.relationship('Comment', backref='post',
                                  cascade="all, delete")

    def json(self):
        return {"article": self.article,
                "create_time": self.create_time}


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete='CASCADE'))
    comment = db.Column(db.String(200))

    def json(self):
        return {"comment": self.comment}

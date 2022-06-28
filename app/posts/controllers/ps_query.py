from dataclasses import dataclass
from ..models.db_posts import Post, Comment, db
import datetime


@dataclass
class PostResponse:
    id: int
    article: str
    create_time: datetime.datetime
    comment: str


class PostApiController:

    @classmethod
    def create_post(cls, data):
        new_post = Post(article=data['article'])
        db.session.add(new_post)
        return db.session.commit()

    @classmethod
    def create_comment(cls, data, pk):
        post = Post.query.get(pk)
        new_comment = Comment(post_id=post.id,
                              comment=data['comment'])
        db.session.add(new_comment)
        return db.session.commit()

    @classmethod
    def post_and_comment(cls):
        result = db.session.query(Post).join(Post.comment_rel).all()
        return cls.query_to_dict(result)

    @classmethod
    def query_to_dict(cls, result):
        general_dict = []
        for i in result:
            dict_query = i.json()
            dict_query['all_comments'] = tuple(
                [j.json() for j in i.comment_rel])
        return general_dict

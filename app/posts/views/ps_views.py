from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from ..controllers.ps_query import PostApiController

posts = Blueprint('posts', __name__)

prefix = 'api/v1/'


@posts.route(f'/{prefix}/posts', methods=['GET'])
def main_page():
    result = PostApiController.post_and_comment()
    return jsonify(tuple(result))


@posts.route(f'/{prefix}/create_post', methods=['POST'])
def create_post():
    if request.method == 'POST':
        data = request.get_json()
        PostApiController.create_post(data)
        return 'Post created'


@posts.route(f'/{prefix}/<int:pk>/create_comment', methods=['POST'])
def create_comment(pk: int):
    if request.method == 'POST':
        data = request.get_json()
        PostApiController.create_comment(data, pk)
        return 'Comment created'

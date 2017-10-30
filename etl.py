"""
Script for retrieving pages, posts, comments and reactions from
a facebook page.

SDK: http://facebook-sdk.readthedocs.io/
API Reference: https://developers.facebook.com/docs/graph-api/reference
"""

import dataset
import facebook

from . import config

access_token = '{}|{}'.format(config.app_id, config.app_secret)

graph = facebook.GraphAPI(access_token, version='2.4')

db = dataset.connect('postgresql://{}:{}@{}:5432/{}'.format(
    config.db_user,
    config.db_password,
    config.db_host,
    config.db_name,
))

pages = [
    'nytimes',
    'clickhole',
    'foxnews',
]


def get_page(page_name):
    print('getting page: {}'.format(page_name))
    page = graph.get_object(page_name)
    table = db['fb_page']
    table.upsert(page, keys=['id'])


def get_posts(page_id):
    print('getting posts for page: {}'.format(page_id))
    result = graph.get_object(page_id, fields='posts')
    posts = result['posts']['data']
    table = db['fb_post']
    try:
        for p in posts:
            table.upsert(dict(
                id=p['id'],
                created_time=p['created_time'],
                message=p['message'],
                page_id=page_id,
            ), keys=['id'])
    except:
        print('error')



def get_comments(post_id):
    print('getting comments for post: {}'.format(post_id))
    result = graph.get_object(post_id, fields='comments')
    comments = result['comments']['data']
    table = db['fb_comment']
    try:
        for c in comments:
            table.upsert(dict(
                id=c['id'],
                created_time=c['created_time'],
                post_id=post_id,
                user_id=c['from']['id'],
                message=c['message'],
            ), keys=['id'])
    except:
        print('error')


def get_reactions(post_id):
    print('getting reactions for post: {}'.format(post_id))
    result = graph.get_object(post_id, fields='reactions')
    reactions = result['reactions']['data']
    table = db['fb_reaction']
    try:
        for r in reactions:
            table.upsert(dict(
                id=r['id'],
                post_id=post_id,
                reaction_type=r['type'],
            ), keys=['id'])
    except:
        print('error')


def main():

    for p in pages:
        get_page(p)

    for page in db['fb_page'].all():
        get_posts(page['id'])

    for post in db['fb_post'].all():
        get_comments(post['id'])
        get_reactions(post['id'])


if __name__ == '__main__':
    main()

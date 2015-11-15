# article club

Article club is a Chrome extension for creating a suggested reading “bundle” of links related to the article you’re consuming. Others can view bundles to learn casually and/or deeply about a topic. Bundles expose readers to new and interesting content and can also serve readers who may be intimidated by an ongoing news story, such as ISIS or the significance of Missy Elliot. A link can belong to many bundles and is categorized as for the casual, engaged or expert reader.

Audience: News consumers, at all levels of engagement.

## Installation

1. Clone this repo into a fresh virtual environment
2. Install reqs via Pip

```shell
$ pip install -r requirements.txt
```

3. Create Postgres database

```shell
$ createdb articleclub
```

4. Set up `local_settings.py` with development environment specifics

```python
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'articleclub',
    }
}
```

5. Run `migrate` command (inside Django project) to terraform database

```shell
$ ./manage migrate
```

6. Start server

```shell
$ ./manage.py runserver
```

... and then visit [http://localhost:8000/](http://localhost:8000/)

## Next steps

A couple of features we've considered adding ...

- Bundles destination page
- Connect "This link belongs to ## bundles" to the destination page, linking to those bundles.
- Create a new bundle from the extension
- Connect curator username to the destination page, linking to that curator's bundles.
- Follow a curator
- Share a link to a bundle on other social media.
- Bundle moderation ... up/down voting to elevate the most relevant bundles that a link belongs to. Verified users who have proven to have expertise in a particular topic. Way for readers to indicate that a bundle needs updating or improvement.
- Display if a link is behind a paywall (lock icon).
- Display if a link is a video.



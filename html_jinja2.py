from jinja2 import Environment
from pelican import signals

import pelicanconf


def jinja_passthrough(article_generator):
    for article in article_generator.articles:
        if article.source_path.endswith('html'):
            env = Environment(trim_blocks=True, lstrip_blocks=True,
                              extensions=getattr(pelicanconf,
                                                'JINJA_EXTENSIONS', []))
            template = env.from_string(article.content)
            output = template.render()
            article._content = output


def register():
    signals.article_generator_finalized.connect(jinja_passthrough)

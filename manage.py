from app import create_app
from app import db
from app.models import Pages, Headers, Text, Tables
import click


app = create_app()


@click.group()
def cli():
    pass


@click.command('create-db')
def create_db():
    app.app_context().push()
    db.create_all()
    print('All tables created')


@click.command('drop-db')
def drop_db():
    app.app_context().push()
    db.drop_all()
    print('All tables deleted')


@click.command('run')
def run():
    app.run(debug=True)


cli.add_command(create_db)
cli.add_command(drop_db)
cli.add_command(run)


if __name__ == '__main__':
    cli()

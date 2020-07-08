import click
from pydoc2md.main import main


@click.command()
@click.argument("projectdir")
@click.argument("savedir")
def run(projectdir, savedir):
    main(projectdir, savedir)

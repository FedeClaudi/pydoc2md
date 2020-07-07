import click
from pydoc2md.main import main


@click.command()
@click.argument("projectdir")
@click.argument("savedir")
@click.option("-s", "--structure", is_flag=True, default=True)
def run(projectdir, savedir, structure=True):
    main(projectdir, savedir, keep_structure=structure)

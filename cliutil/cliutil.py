import click
import pkg_resources 

@click.group()
def cli():
    pass

@cli.command()
def operation():
    '''Run Operation'''
    click.echo('Running Operation')

@cli.command()
def clean():
    '''Run Cleanup'''
    click.echo('Run Cleanup')
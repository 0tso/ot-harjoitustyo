from invoke import task

@task
def start(ctx):
    ctx.run("python -m tilemap_editor.app", pty=True)
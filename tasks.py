from invoke import task

@task
def start(ctx):
    ctx.run("python src/app.py", pty=True)
from invoke import task

@task
def start(ctx):
    ctx.run("python -m tilemap_editor.app", pty=True)

@task
def test(ctx):
    ctx.run("pytest tilemap_editor/", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest tilemap_editor/")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint tilemap_editor")
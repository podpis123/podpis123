from fabric import task

my_hosts = ["p01.podpis123.cz"]

@task(hosts=my_hosts)
def test(c):
    c.local("py manage.py test", warn=True)

@task(hosts=my_hosts)
def dev(c):
    c.local("py manage.py migrate", warn=True)
    c.local("py manage.py runserver", warn=True)

@task(hosts=my_hosts)
def deploy(c):
    code_dir = "/srv/django/maureen"
    if not c.run("test -d {}".format(code_dir), warn=True):
        cmd = "git clone https://github.com/podpis123/podpis123.git {}"
        c.run(cmd.format(code_dir))
    c.run("cd {} && git pull".format(code_dir))
    #c.run("cd {} && touch app.wsgi".format(code_dir))
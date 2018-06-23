# -*- coding: utf-8 -*-

from fabric.api import lcd, local


def deploy():
    local("curl http://jd.hehanlin.cn:6800/delproject.json -d project=spider")
    with lcd('..'):
        local("scrapyd-deploy")
        local("rm -rf build project.egg-info setup.py")



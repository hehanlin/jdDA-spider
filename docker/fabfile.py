# -*- coding: utf-8 -*-

from fabric.api import env, put, cd, run, lcd, local

env.hosts = ['Chaos@zc.hehanlin.cn:9999']
env.password = 'liuzhichao_1203'


def rebuild():
    with cd('/home/Chaos/hehanlin'):
        put('./docker-compose.yml', 'docker-compose.yml')
        put('./nginx.conf', 'nginx/nginx.conf', use_sudo=True)
        run('docker-compose down')
        run('docker-compose up -d')


def deploy():
    local("curl http://zc.hehanlin.cn:6800/delproject.json -d project=spider")
    with lcd('..'):
        local("scrapyd-deploy")
        local("rm -rf build project.egg-info setup.py")



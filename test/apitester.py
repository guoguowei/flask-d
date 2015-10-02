# -*- coding: utf-8 -*-

__author__ = 'wills'

from apidriver import APIDriver
import hashlib
import json
import jsonschema



class APITester(object):

    SIGNIN_URL = '/account/sign_in'

    def __init__(self):
        self.host = None
        self.env = {'app': 1, 'version': 101}
        self.user = None
        self.tests = []
        self.reports = []
        self.fail_number = 0
        self.fails = []

    def add_report(self, msg):
        self.reports.append(msg)

    def load(self, filename):
        try:
            db_file = file(filename)
            data = json.load(db_file)
            self.host = data.get('host')
            self.user = data.get('user')
            if self.user and self.user.get('password'):
                self.user['password'] = hashlib.md5(hashlib.md5(
                    self.user.get('password')).hexdigest()).hexdigest()
            self.env.update(data.get('env'))
            self.tests = data.get('tests')

            if not self.host:
                self.add_report('MSG: no host in json')
            if not self.tests:
                self.add_report('MSG: no tests to run')

        except:
            self.add_report('MSG: File not found or json error')

    def run(self):
        if not self.host:
            self.add_report('MSG: host not set')
            return

        self.signin()

        for test in self.tests:
            url = self.host + test.get('api')
            params = test.get('params') or {}
            method = test.get('method') or 'get'
            self.add_report('MSG: request %s with %s' % (url, str(params)))
            params = self.prepare(params, method, test.get('api'))

            resp = APIDriver(url, params, test.get('method')).run()
            self.add_report('RESPONSE: \n %s' % json.dumps(resp, indent=2))

            if not self.validate(resp, test.get('except')):
                self.fail_number += 1
                self.fails.append('MSG: request %s with %s' %
                                  (url, str(params)))
                self.fails.append('RESPONSE: \n %s' %
                                  json.dumps(resp, indent=2))

    def signin(self):
        if self.user:
            signin_msg = {
                'user_name': self.user.get('phone'),
                'user_token': self.user.get('password'),
                'user_type': 1
            }
            signin_msg.update(self.env)
            signin_msg = APIDriver(
                self.host + self.SIGNIN_URL, signin_msg).run()

            if signin_msg and signin_msg.get('code') == 0:
                self.user['session'] = signin_msg.get(
                    'data').get('session')
                self.user['uid'] = signin_msg.get(
                    'data').get('uid')
                self.add_report('signin_success')
            else:
                self.add_report('signin_error')

    def prepare(self, params, method, path):
        if path.startswith('/'):
            path = path[1:]
        method = method.upper()
        new_param = params
        new_param.update(self.env)
        if self.user:
            new_param.update(self.user)
        keys = new_param.keys()
        keys.sort()

        params_str = ''.join(
            [('%s=%s' % (key, new_param[key])) for key in keys])
        sign_src = ''.join((method, path, params_str))

        new_param['sign'] = hashlib.md5(sign_src).hexdigest().lower()
        return new_param

    def validate(self, resp, schema):
        try:
            jsonschema.validate(resp, schema)
            return True
        except:
            return False

    def summary(self):
        print "%s Test case, %s failed" % (len(self.tests), self.fail_number)
        if self.fail_number:
            print '\n\n'.join(self.fails)

    def report(self):
        print '\n\n'.join(self.reports)

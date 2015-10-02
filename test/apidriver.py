# -*- coding: utf-8 -*-

__author__ = 'wills'

import json
import sys
import urllib
import urllib2


class APIDriver(object):

    def __init__(self, url, params=None, method='get'):
        self.url = url
        self.method = method
        self.params = params

    def run(self, timeout=5):
        if self.method and self.method.lower() == 'post':
            return self._run_post(timeout)
        else:
            return self._run_get(timeout)

    def _run_post(self, timeout):
        try:
            data = urllib.urlencode(self.params)
            resp_data = urllib2.urlopen(
                self.url, data=data, timeout=timeout).read()
            return json.loads(resp_data)
        except Exception, e:
            print '%s. POST %s with %s' % (e, self.url, self.url)
            return None

    def _run_get(self, timeout):
        try:
            query = urllib.urlencode(self.params)
            request = urllib2.Request('%s?%s' % (self.url, query))
            data = urllib2.urlopen(request, timeout=timeout).read()
            return json.loads(data)
        except Exception, e:
            print '%s. GET %s with %s' % (e, self.url, self.params)
            return None

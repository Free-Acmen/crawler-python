#! /usr/bin/env python
# -*- coding: utf-8 -*-
# name HtmlDownloader.py

class HtmlDownloader(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
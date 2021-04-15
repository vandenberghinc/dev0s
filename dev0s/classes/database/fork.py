#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, ast, dev0s
webserver = dev0s.database.WebServer(serialized=ast.literal_eval(dev0s.cli.get_argument("--serialized")[1:-1]))
webserver.start()
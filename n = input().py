from abc import *
from aifc import *
from argparse import *
from array import *
from ast import *
from asyncio import *
from atexit import *
from audioop import *
from base64 import *
from bdb import *
from binhex import *
from bisect import *
from bz2 import *
from cProfile import *
from calendar import *
from cgi import *
from cgitb import *
from chunk import *
from cmd import *
from code import *
from codecs import *
from codeop import *
from collections import *
from colorsys import *
from compileall import *
from concurrent import *
from configparser import *
from contextlib import *
from contextvars import *
from copy import *
from copyreg import *
from crypt import *
from csv import *
from ctypes import *
from curses import *
from dataclasses import *
from datetime import *
from dbm import *
from decimal import *
from difflib import *
from dis import *
from distutils import *
from doctest import *
from email import *
from encodings import *
from ensurepip import *
from enum import *
from errno import *
from faulthandler import *
from fcntl import *
from filecmp import *
from fileinput import *
from fnmatch import *
from formatter import *
from fractions import *
from ftplib import *
from functools import *
from gc import *
from getopt import *
from getpass import *
from gettext import *
from glob import *
from grp import *
from gzip import *
from hashlib import *
from heapq import *
from hmac import *
from http import *
from imaplib import *
from imghdr import *
from importlib import *
from inspect import *
from io import *
from ipaddress import *
from itertools import *
from json import *
from keyword import *
from linecache import *
from locale import *
from logging import *
from lzma import *
from mailbox import *
from mailcap import *
from marshal import *
from math import *
from mimetypes import *
from mmap import *
from modulefinder import *
from msilib import *
from multiprocessing import *
from netrc import *
from nntplib import *
from numbers import *
from operator import *
from optparse import *
from os import *
from parser import *
from pathlib import *
from pdb import *
from pickle import *
from pickletools import *
from pipes import *
from pkgutil import *
from platform import *
from plistlib import *
from poplib import *
from posix import *
from pprint import *
from profile import *
from pstats import *
from pty import *
from pwd import *
from py_compile import *
from pyclbr import *
from pydoc import *
from queue import *
from quopri import *
from random import *
from re import *
from readline import *
from reprlib import *
from resource import *
from rlcompleter import *
from runpy import *
from sched import *
from secrets import *
from select import *
from selectors import *
from shelve import *
from shlex import *
from shutil import *
from signal import *
from site import *
from smtpd import *
from smtplib import *
from sndhdr import *
from socket import *
from socketserver import *
from sqlite3 import *
from ssl import *
from stat import *
from statistics import *
from string import *
from stringprep import *
from struct import *
from subprocess import *
from sunau import *
from symtable import *
from sys import *
from sysconfig import *
from tabnanny import *
from tarfile import *
from telnetlib import *
from tempfile import *
from termios import *
from test import *
from textwrap import *
from threading import *
from time import *
from timeit import *
from tkinter import *
from token import *
from tokenize import *
from trace import *
from traceback import *
from tracemalloc import *
from tty import *
from turtle import *
from types import *
from typing import *
from unittest import *
from urllib import *
from uu import *
from uuid import *
from venv import *
from warnings import *
from wave import *
from weakref import *
from webbrowser import *
from winreg import *
from winsound import *
from wsgiref import *
from xdrlib import *
from xml import *
from xmlrpc import *
from zipapp import *
from zipfile import *
from zipimport import *
from zlib import *
modules = [
    'abc', 'aifc', 'argparse', 'array', 'ast', 'asyncio', 'atexit', 'audioop',
    'base64', 'bdb', 'binhex', 'bisect', 'bz2', 'cProfile', 'calendar', 'cgi',
    'cgitb', 'chunk', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorsys',
    'compileall', 'concurrent', 'configparser', 'contextlib', 'contextvars', 'copy',
    'copyreg', 'crypt', 'csv', 'ctypes', 'curses', 'dataclasses', 'datetime', 'dbm',
    'decimal', 'difflib', 'dis', 'distutils', 'doctest', 'email', 'encodings',
    'ensurepip', 'enum', 'errno', 'faulthandler', 'fcntl', 'filecmp', 'fileinput',
    'fnmatch', 'formatter', 'fractions', 'ftplib', 'functools', 'gc', 'getopt',
    'getpass', 'gettext', 'glob', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'http',
    'imaplib', 'imghdr', 'importlib', 'inspect', 'io', 'ipaddress', 'itertools',
    'json', 'keyword', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap',
    'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'msilib', 'multiprocessing',
    'netrc', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'parser', 'pathlib',
    'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib',
    'poplib', 'posix', 'pprint', 'profile', 'pstats', 'pty', 'pwd', 'py_compile',
    'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 're', 'readline', 'reprlib',
    'resource', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors',
    'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr',
    'socket', 'socketserver', 'sqlite3', 'ssl', 'stat', 'statistics', 'string',
    'stringprep', 'struct', 'subprocess', 'sunau', 'symtable', 'sys', 'sysconfig',
    'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'termios', 'test', 'textwrap',
    'threading', 'time', 'timeit', 'tkinter', 'token', 'tokenize', 'trace', 'traceback',
    'tracemalloc', 'tty', 'turtle', 'types', 'typing', 'unittest', 'urllib', 'uu',
    'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'winreg', 'winsound',
    'wsgiref', 'xdrlib', 'xml', 'xmlrpc', 'zipapp', 'zipfile', 'zipimport', 'zlib'
]

for module in modules:
    try:
        exec(f'from {module} import *')
    except ImportError:
        pass
#It won't bug if there's a wrong modules ,that code from line 190 to line 222
#Your turn to code!

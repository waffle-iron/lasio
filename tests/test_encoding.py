import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import codecs

import pytest

from lasio import read

egfn = lambda fn: os.path.join(os.path.dirname(__file__), "examples", fn)

def test_utf8_default():
    fn = egfn("sample_extended_chars_utf8.las")
    l = read(fn)

def test_utf8wbom_default():
    fn = egfn("sample_extended_chars_utf8wbom.las")
    l = read(fn)

def test_cp1252_default():
    fn = egfn("sample_extended_chars_cp1252.las")
    l = read(fn)

def test_utf8_autodetect():
    fn = egfn("sample_extended_chars_utf8.las")
    l = read(fn, autodetect_encoding=True)

def test_utf8wbom_autodetect():
    fn = egfn("sample_extended_chars_utf8wbom.las")
    l = read(fn, autodetect_encoding=True)

def test_cp1252_autodetect():
    fn = egfn("sample_extended_chars_cp1252.las")
    l = read(fn, autodetect_encoding=True)

def test_utf8_encoding_specified():
    fn = egfn("sample_extended_chars_utf8.las")
    l = read(fn, encoding="utf-8")

def test_utf8wbom_encoding_specified():
    fn = egfn("sample_extended_chars_utf8wbom.las")
    l = read(fn, encoding="utf-8-sig")

def test_cp1252_encoding_specified():
    fn = egfn("sample_extended_chars_cp1252.las")
    l = read(fn, encoding="cp1252")

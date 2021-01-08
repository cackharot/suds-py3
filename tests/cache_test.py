import datetime
import os
import os.path
import subprocess
import sys
import tempfile
import unittest

import suds
import suds.cache


def _is_empty_cache_folder(folder):
    assert os.path.isdir(folder)

    def walkError(error):
        unittest.TestCase.fail(
            "Error attempting to walk through cache folder contents.")
    count = 0
    for root, folders, files in os.walk(folder, onerror=walkError):
        assert root == folder
        return len(folders) == 0 and len(files) == 1 and files[0] == 'version'
    return False

class DummyObjectForTesting:
    """Dummy class used for pickling related tests."""

    def __init__(self, x):
        self.x = x

class TestFileCache(unittest.TestCase):
    def test_basic_custom_cache_location(self):
        cache_folder = os.path.join(
            tempfile.gettempdir(), "custom-cache-loc-test")
        cache = suds.cache.FileCache(cache_folder)
        assert isinstance(cache, suds.cache.Cache)
        value = "some value".encode()
        cache.put("test_key", value)
        assert cache.get("test_key") == value
        assert not _is_empty_cache_folder(cache_folder)

    def test_basic_default_cache_location(self):
        cache = suds.cache.FileCache()
        assert isinstance(cache, suds.cache.Cache)
        value = "some value".encode()
        cache.put("test_key", value)
        assert cache.get("test_key") == value
        assert not _is_empty_cache_folder(cache.location)

    def test_close_leaves_cached_files_behind(self):
        val1 = "123523".encode()
        val2 = u"€ 的 čćžšđČĆŽŠĐ".encode()
        cache_folder1 = os.path.join(tempfile.gettempdir(), "f1")
        cache1 = suds.cache.FileCache(cache_folder1)
        cache1.put("key1", val1)
        cache1.put("key2", val2)

        cache_folder2= os.path.join(tempfile.gettempdir(), "f2")
        cache2 = suds.cache.FileCache(cache_folder2)
        cache2.put("key3", val1)
        cache2.put("key4", val2)

        del cache1

        cache11 = suds.cache.FileCache(cache_folder1)
        assert cache11.get("key1") == val1
        assert cache11.get("key2") == val2
        assert cache2.get("key3") == val1
        assert cache2.get("key4") == val2

class TestObjectCache(unittest.TestCase):
    def test_basic(self):
        cache_folder = os.path.join(
            tempfile.gettempdir(), "custom-cache-loc-object-test")
        cache = suds.cache.ObjectCache(cache_folder)
        assert isinstance(cache, suds.cache.FileCache)
        cache.put("key1", DummyObjectForTesting(1))
        cache.put("key2", DummyObjectForTesting(2))
        read1 = cache.get("key1")
        read2 = cache.get("key2")
        assert read1.__class__ is DummyObjectForTesting
        assert read2.__class__ is DummyObjectForTesting
        assert read1.x == 1
        assert read2.x == 2

class TestDocumentCache(unittest.TestCase):
    def test_basic(self):
        cache_folder = os.path.join(
            tempfile.gettempdir(), "custom-cache-loc-document-test")
        cache = suds.cache.DocumentCache(cache_folder)
        assert isinstance(cache, suds.cache.FileCache)
        doc = suds.sax.document.Document()
        doc.append(suds.sax.element.Element("TestEle1"))
        cache.put("key1", doc)
        read1 = cache.get("key1")
        assert read1.__class__ is suds.sax.document.Document

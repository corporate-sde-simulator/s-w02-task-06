"""Tests for Email notification template renderer."""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from templateRenderer import TemplateRenderer
from placeholderResolver import PlaceholderResolver

class TestMain:
    def test_basic(self):
        obj = TemplateRenderer()
        assert obj.process({"key": "val"}) is not None
    def test_empty(self):
        obj = TemplateRenderer()
        assert obj.process(None) is None
    def test_stats(self):
        obj = TemplateRenderer()
        obj.process({"x": 1})
        assert obj.get_stats()["processed"] == 1

class TestSupport:
    def test_basic(self):
        obj = PlaceholderResolver()
        assert obj.process({"key": "val"}) is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

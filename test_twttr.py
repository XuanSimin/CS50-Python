from twttr import shorten

def test_shorten():
    assert shorten("apple") == "ppl"
    assert shorten("APPLE") == "PPL"
    assert shorten("pear") == "pr"
    assert shorten("ice") == "c"
    assert shorten("oat") == "t"
    assert shorten("us") == "s"

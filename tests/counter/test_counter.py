from src.counter import count_ocurrences


def test_counter():
    ocurrences_python = count_ocurrences("src/jobs.csv", "Python")
    ocurrences_javascript = count_ocurrences("src/jobs.csv", "Javascript")
    assert ocurrences_python == 1639
    assert ocurrences_javascript == 122

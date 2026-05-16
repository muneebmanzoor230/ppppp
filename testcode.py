from unittest.mock import patch
import runpy


def test_grade_b(capsys):
    with patch("builtins.input", side_effect=["Muneeb", "82"]):
        runpy.run_path("app.py")

    captured = capsys.readouterr()

    assert "Grade: B" in captured.out
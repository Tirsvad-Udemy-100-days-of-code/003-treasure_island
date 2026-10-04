import pytest

from treasure_island.game import choose, play


def run(answers):
    it = iter(answers)
    out = []
    won = play(ask=lambda _p: next(it), say=out.append)
    return won, "\n".join(out)


def test_winning_path():
    won, out = run(["left", "wait", "yellow"])
    assert won and "You Win" in out


@pytest.mark.parametrize(
    "answers, message",
    [
        (["right"], "hole"),
        (["left", "swim"], "trout"),
        (["left", "wait", "red"], "fire"),
        (["left", "wait", "blue"], "beasts"),
    ],
)
def test_losing_paths(answers, message):
    won, out = run(answers)
    assert not won and message in out and "Game Over" in out


def test_input_is_case_insensitive_and_reasked():
    won, _ = run(["LEFT", "huh", " Wait ", "Yellow"])
    assert won


def test_choose_rejects_invalid():
    answers = iter(["x", "b"])
    assert choose(lambda _p: next(answers), "?", ("a", "b")) == "b"

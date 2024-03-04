from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("hello world", 3) == "olleh_dlrow ol"
    assert encrypt_message("hello world!", 0) == "dlrow olleh"
    with pytest.raises(TypeError):
        encrypt_message(123, 2)
    with pytest.raises(TypeError):
        encrypt_message("hello world!", "invalid_key")

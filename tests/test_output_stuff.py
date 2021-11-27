import pytest
from src.output_stuff import output_with_error


def test_for_msg(capsys, caplog):
    # "pytest tests/* -s" to see the output

    # we are expecting an error, so:
    with pytest.raises(Exception) as err:
        output_with_error()  # call function
        # NOTE: MAKE SURE TO UNINDENT
        # Everything after function call is ignored. e.g:
        assert False  # THIS IS IGNORED!!!
        print("THIS IS IGNORED TOO!!!")

    stdout, stderr = capsys.readouterr()  # read the output
    log_msg = caplog.text  # read the log
    error_msg = str(err.value)  # read the error

    print("")
    print("_" * 10)
    print(f"->stdout: {stdout}")
    print(f"->stderr: {stderr}")
    print(f"->log_msg: {log_msg}")
    print(f"->error_msg: {error_msg}")
    print("_" * 10)

    # assertions here:
    assert "THE-MSG\n" in stdout
    assert "THE-MSG-2\n" in stdout
    assert "THE-LOG" in log_msg
    assert error_msg == "THE-ERROR"
    # assert False  # uncomment to make sure test runs this far

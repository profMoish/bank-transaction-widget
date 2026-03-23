from src.decorators import log


@log()
def div(a, b):
    return a / b

def test_log(capsys):

    r = div(10, 2)
    out, err = capsys.readouterr()
    assert err == ''
    out = out.split('\n')
    assert 'ok' in out[1]
    assert 'Result' in out[2]
    assert str(r) in out[2]
    assert 'Start' in out[3]
    assert 'End' in out[4]

def test_log_err(capsys):
    r = div(10, 0)
    out, err = capsys.readouterr()
    assert err == ''
    out = out.split('\n')
    assert 'error' in out[1]
    assert 'Inputs:' in out[2]
    assert 'Start' in out[3]
    assert 'End' in out[4]



def test_log_in_file():

    name_log = 'test_log.txt'

    @log(name_log)
    def division(a, b):
        return a / b

    division(10, 5)
    division(10, 0)

    with open(name_log, "r", encoding="utf-8") as file:
        lines = file.readlines()

        assert 'ok' in lines[-10]
        assert 'Result' in lines[-9]
        assert 'Start' in lines[-8]
        assert 'End' in lines[-7]

        assert 'error' in lines[-5]
        assert 'Inputs' in lines[-4]
        assert 'Start' in lines[-3]
        assert 'End' in lines[-2]

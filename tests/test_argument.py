from partition import argument


def test_get_parser(mocker):
    mocked_parser = mocker.patch("argparse.ArgumentParser")
    argument.get_parser()
    mocked_parser.assert_called()
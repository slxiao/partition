from partition import partition
import pytest

def test_partition_with_version(mocker):
    mocked_parser = mocker.patch("partition.argument.get_parser", mocker.Mock(return_value=mocker.Mock()))
    mocked_parser.return_value.parse_args.return_value = mocker.Mock(version="0.0.0")
    assert partition.partition() == "0.0.0"
    mocked_parser.assert_called()

def test_partition(mocker):
    mocked_parser = mocker.patch("partition.argument.get_parser", mocker.Mock(return_value=mocker.Mock()))
    mocked_parser.return_value.parse_args.return_value = mocker.Mock(version=None, numbers="1,2,3", grouplen=2, algorithm="greedy")
    mocked_greedy = mocker.patch("partition.greedy.greedy", mocker.Mock(return_value=[[1, 2], [3]]))
    assert partition.partition()[1] == 0
    mocked_parser.assert_called()
    mocked_greedy.assert_called_once_with([1,2,3],2)

def test_partition_nonexist_algorithm(mocker):
    mocked_parser = mocker.patch("partition.argument.get_parser", mocker.Mock(return_value=mocker.Mock()))
    mocked_parser.return_value.parse_args.return_value = mocker.Mock(version=None, numbers="1,2,3", algorithm="foo")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            partition.partition()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "unsupported partition algorithm: foo"
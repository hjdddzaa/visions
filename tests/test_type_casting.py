import pytest

from tenzing.core.model_implementations.types import *

from tests.series import get_series


def get_series_map():
    return [
        (tenzing_integer, tenzing_float, []),
        (tenzing_integer, tenzing_string, []),
        (tenzing_float, tenzing_string, []),
        (tenzing_datetime, tenzing_string, []),
        (tenzing_geometry, tenzing_string, []),
        (tenzing_bool, tenzing_string, []),
    ]


# TODO: check that all series are tested
# TODO: check that all relations are tested
# def all_series_included(series_list, series_map):
#     """Check that all names are indeed used"""
#     used_names = set([name for names in series_map.values() for name in names])
#     names = set([series.name for series in series_list])
#     if not names == used_names:
#         raise ValueError(f"Not all series are used {names ^ used_names}")


def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == "test_relations":
        _series_map = get_series_map()
        _test_suite = get_series()

        # all_series_included(_test_suite, _series_map)

        argsvalues = []
        for item in _test_suite:
            for source_type, relation_type, series_list in _series_map:
                args = {"id": f"{item.name} x {source_type} x {relation_type}"}
                # if item.name not in series_list:
                #     args["marks"] = pytest.mark.xfail()

                argsvalues.append(
                    pytest.param(source_type, relation_type, item, **args)
                )

        metafunc.parametrize(
            argnames=["source_type", "relation_type", "series"], argvalues=argsvalues
        )


def test_relations(source_type, relation_type, series):
    relation = source_type.get_relations()[relation_type]
    if series in relation_type and relation.is_relation(series):
        cast_series = relation.transform(series)
        assert (
            cast_series in source_type
        ), f"Relationship {relation} cast {series.values} to {cast_series.values} "
    else:
        pass
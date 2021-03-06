import pandas as pd
import pytest

from tests.series import get_series
from tests.utils import (
    contains,
    convert,
    get_contains_cases,
    get_convert_cases,
    get_inference_cases,
    infers,
)
from visions import StandardSet
from visions.types import (
    Boolean,
    Categorical,
    Complex,
    DateTime,
    Float,
    Generic,
    Integer,
    Object,
    String,
    TimeDelta,
)

series = get_series()

typeset = StandardSet()

contains_map = {
    Integer: {
        "int_series",
        "Int64_int_series",
        "int_range",
        "Int64_int_nan_series",
        "int_series_boolean",
        "np_uint32",
        "pd_uint32",
    },
    Float: {
        "float_series",
        "float_series2",
        "float_series3",
        "float_series4",
        "inf_series",
        "nan_series",
        "float_nan_series",
        "float_series5",
        "int_nan_series",
        "nan_series_2",
        "float_with_inf",
        "float_series6",
    },
    Categorical: {
        "categorical_int_series",
        "categorical_float_series",
        "categorical_string_series",
        "categorical_complex_series",
        "categorical_char",
        "ordinal",
    },
    Boolean: {"bool_series", "bool_series2", "bool_series3", "nullable_bool_series"},
    Complex: {
        "complex_series",
        "complex_series_py",
        "complex_series_nan",
        "complex_series_py_nan",
        "complex_series_nan_2",
        "complex_series_float",
    },
    DateTime: {
        "timestamp_series",
        "timestamp_aware_series",
        "datetime",
        "timestamp_series_nat",
        "date_series_nat",
    },
    TimeDelta: {"timedelta_series", "timedelta_series_nat", "timedelta_negative"},
    String: {
        "timestamp_string_series",
        "string_with_sep_num_nan",
        "string_series",
        "geometry_string_series",
        "string_unicode_series",
        "string_np_unicode_series",
        "path_series_linux_str",
        "path_series_windows_str",
        "int_str_range",
        "string_date",
        "textual_float",
        "textual_float_nan",
        "ip_str",
        "string_flt",
        "string_num",
        "str_url",
        "string_str_nan",
        "string_num_nan",
        "string_bool_nan",
        "string_flt_nan",
        "str_complex",
        "uuid_series_str",
        "str_int_leading_zeros",
        "email_address_str",
        "str_float_non_leading_zeros",
        "str_int_zeros",
    },
}

if int(pd.__version__[0]) >= 1:
    contains_map[String].add("string_dtype_series")

contains_map[Object] = {
    "path_series_linux",
    "path_series_linux_missing",
    "path_series_windows",
    "url_series",
    "url_nan_series",
    "url_none_series",
    "file_test_py",
    "file_mixed_ext",
    "file_test_py_missing",
    "image_png",
    "image_png_missing",
    "image_png",
    "image_png_missing",
    "email_address",
    "email_address_missing",
    "uuid_series",
    "uuid_series_missing",
    "ip",
    "ip_mixed_v4andv6",
    "ip_missing",
    "geometry_series",
    "geometry_series_missing",
    "mixed_list[str,int]",
    "mixed_dict",
    "callable",
    "module",
    "mixed_integer",
    "mixed_list",
    "mixed",
    "bool_nan_series",
    "date",
    "time",
}

# Empty series
contains_map[Generic] = {
    "empty",
    "empty_bool",
    "empty_float",
    "empty_int64",
    "empty_object",
}


@pytest.mark.parametrize(**get_contains_cases(series, contains_map, typeset))
def test_contains(series, type, member):
    """Test the generated combinations for "series in type"

    Args:
        series: the series to test
        type: the type to test against
        member: the result
    """
    result, message = contains(series, type, member)
    assert result, message


inference_map = {
    "int_series": Integer,
    "categorical_int_series": Categorical,
    "int_nan_series": Integer,
    "Int64_int_series": Integer,
    "Int64_int_nan_series": Integer,
    "np_uint32": Integer,
    "pd_uint32": Integer,
    "int_range": Integer,
    "float_series": Float,
    "float_nan_series": Float,
    "int_series_boolean": Integer,
    "float_series2": Integer,
    "float_series3": Float,
    "float_series4": Float,
    "float_series5": Float,
    "float_series6": Float,
    "complex_series_float": Integer,
    "categorical_float_series": Categorical,
    "float_with_inf": Float,
    "inf_series": Float,
    "nan_series": Float,
    "nan_series_2": Float,
    "string_series": String,
    "categorical_string_series": Categorical,
    "timestamp_string_series": DateTime,
    "string_with_sep_num_nan": String,  # TODO: Introduce thousands separator
    "string_unicode_series": String,
    "string_np_unicode_series": String,
    "string_num_nan": Integer,
    "string_num": Integer,
    "string_flt_nan": Float,
    "string_flt": Float,
    "string_str_nan": String,
    "string_bool_nan": Boolean,
    "int_str_range": Integer,
    "string_date": DateTime,
    "str_url": String,
    "bool_series": Boolean,
    "bool_nan_series": Boolean,
    "nullable_bool_series": Boolean,
    "bool_series2": Boolean,
    "bool_series3": Boolean,
    "complex_series": Complex,
    "complex_series_nan": Complex,
    "complex_series_nan_2": Complex,
    "complex_series_py_nan": Complex,
    "complex_series_py": Complex,
    "categorical_complex_series": Categorical,
    "timestamp_series": DateTime,
    "timestamp_series_nat": DateTime,
    "timestamp_aware_series": DateTime,
    "datetime": DateTime,
    "timedelta_series": TimeDelta,
    "timedelta_series_nat": TimeDelta,
    "timedelta_negative": TimeDelta,
    "geometry_string_series": String,
    "geometry_series_missing": Object,
    "geometry_series": Object,
    "path_series_linux": Object,
    "path_series_linux_missing": Object,
    "path_series_linux_str": String,
    "path_series_windows": Object,
    "path_series_windows_str": String,
    "url_series": Object,
    "url_nan_series": Object,
    "url_none_series": Object,
    "mixed_list[str,int]": Object,
    "mixed_dict": Object,
    "mixed_integer": Object,
    "mixed_list": Object,
    "mixed": Boolean,
    "callable": Object,
    "module": Object,
    "textual_float": Float,
    "textual_float_nan": Float,
    "empty": Generic,
    "empty_object": Generic,
    "empty_float": Generic,
    "empty_bool": Generic,
    "empty_int64": Generic,
    "ip": Object,
    "ip_str": String,
    "ip_missing": Object,
    "date_series_nat": DateTime,
    "date": Object,
    "time": Object,
    "categorical_char": Categorical,
    "ordinal": Categorical,
    "str_complex": Complex,
    "uuid_series": Object,
    "uuid_series_str": String,
    "uuid_series_missing": Object,
    "ip_mixed_v4andv6": Object,
    "file_test_py": Object,
    "file_test_py_missing": Object,
    "file_mixed_ext": Object,
    "image_png": Object,
    "image_png_missing": Object,
    "str_int_leading_zeros": String,
    "str_float_non_leading_zeros": Float,
    "str_int_zeros": Integer,
    "email_address": Object,
    "email_address_missing": Object,
    "email_address_str": String,
}
if int(pd.__version__[0]) >= 1:
    inference_map["string_dtype_series"] = String


@pytest.mark.parametrize(**get_inference_cases(series, inference_map, typeset))
def test_inference(series, type, typeset, difference):
    """Test the generated combinations for "inference(series) == type"

    Args:
        series: the series to test
        type: the type to test against
    """
    result, message = infers(series, type, typeset, difference)
    assert result, message


# Conversions in one single step
convert_map = [
    # Model type, Relation type
    (Integer, Float, {"int_nan_series", "float_series2"}),
    (Complex, String, {"str_complex"}),
    (
        Float,
        String,
        {
            "string_flt",
            "string_num_nan",
            "string_num",
            "string_flt_nan",
            "textual_float",
            "textual_float_nan",
            "int_str_range",
            "str_float_non_leading_zeros",
            "str_int_zeros",
            # "string_with_sep_num_nan",
        },
    ),
    (DateTime, String, {"timestamp_string_series", "string_date"}),
    (Boolean, String, {"string_bool_nan"}),
    (Float, Complex, {"complex_series_float"}),
    (Boolean, Object, {"bool_nan_series", "mixed"}),
]


@pytest.mark.parametrize(**get_convert_cases(series, convert_map, typeset))
def test_conversion(source_type, relation_type, series, member):
    """Test the generated combinations for "convert(series) == type" and "infer(series) = source_type"

    Args:
        series: the series to test
        type: the type to test against
    """
    result, message = convert(source_type, relation_type, series, member)
    assert result, message

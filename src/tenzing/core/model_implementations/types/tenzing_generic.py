import numpy as np

from tenzing.core import tenzing_model
from tenzing.core.reuse import base_summary


class tenzing_generic(tenzing_model):
    """**Generic** implementation of :class:`tenzing.core.models.tenzing_model`.

    >>> x = pd.Series(['a', 1, np.nan])
    >>> x in tenzing_generic
    True
    """

    @classmethod
    def contains_op(cls, series):
        return True

    @classmethod
    def cast_op(cls, series):
        return series

    @classmethod
    @base_summary
    def summarization_op(cls, series):
        summary = super().summarization_op(series)
        return summary

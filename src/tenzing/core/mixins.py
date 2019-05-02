from pandas import Series


class optionMixin:
    is_option = True

    def cast(self, series, operation=None):
        operation = operation if operation is not None else self.cast_op

        idx = series.isna()
        if idx.any():
            result = series.copy()
            result[~idx] = operation(series[~idx])
        else:
            result = operation(series)

        return result

    @staticmethod
    def get_series(series):
        return series[series.notna()]

    def __contains__(self, series):
        idx = series.isna()
        notna_series = series[~idx].infer_objects() if idx.any() else series
        return self.contains_op(notna_series)

    def summarize(self, series):
        idx = series.isna()
        summary = self.summarization_op(series[~idx])

        summary['na_count'] = idx.values.sum()
        summary['perc_na'] = summary['na_count'] / series.shape[0] if series.shape[0] > 0 else 0
        summary['n_records'] = series.shape[0]
        return summary

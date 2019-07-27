import math
from .select import select_internal


def kth_quantiles(numbers, k):
    quantiles = []

    size_of_each_quantile = math.ceil(len(numbers) / k)

    kth_quantiles_internal(
        numbers, 0, len(numbers) - 1, k, size_of_each_quantile, quantiles)

    return quantiles


def kth_quantiles_internal(numbers, p, r, k, size_of_each_quantile, quantiles):
    if k == 1:
        return
    else:
        median_of_k = math.ceil(k / 2)
        i = median_of_k * size_of_each_quantile

        index, quantile = select_internal(numbers, p, r, i)

        quantiles.append(quantile)

        kth_quantiles_internal(
            numbers, p, index, median_of_k, size_of_each_quantile, quantiles)
        kth_quantiles_internal(
            numbers, index + 1, r, k - median_of_k,
            size_of_each_quantile, quantiles)

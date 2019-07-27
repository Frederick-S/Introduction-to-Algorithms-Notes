def weighted_median(elements):
    elements.sort(key=lambda element: element.get('value'))

    weight_sum = 0.0
    epsilon = 0.001

    for element in elements:
        weight_sum += element.get('weight')

        if weight_sum + epsilon >= 0.5:
            return element.get('value')

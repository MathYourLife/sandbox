#!/usr/bin/env python

import numpy as np

# Generate some mocked up data
def generate_mock_data(factor_count, measurement_count):
    
    x = np.random.randn(measurement_count, factor_count)
    x = np.matrix(x)
    print x
    
    coeff = np.random.randn(factor_count)
    coeff = np.matrix(coeff)
    coeff.shape = (factor_count, 1)
    print coeff
    
    y = x * coeff
    # Add an offset
    offset = np.random.randn()
    beta = np.matrix((coeff, offset))
    print beta
    offset = np.ones(measurement_count) * offset
    offset.shape = (measurement_count, 1)

    y = y + offset
    #print y

    return x, y, beta

# Create some mock data to play with
generate_mock_data(factor_count=3, measurement_count=20)




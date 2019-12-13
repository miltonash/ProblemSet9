import numpy as np
import aggregates
import demographics


def test_get_L():
    '''
    Test of the aggregates.get_L() function
    '''
    E = 20
    S = 80
    T = int(round(4.0*S))
    min_year = 0
    max_year = 100
    curr_year = 0
    (omega_path_S, g_n_SS, omega_SS, living_rates_S, mort_rates_S, g_n_path,
        imm_rates_mat, omega_S_preTP) = \
        demographics.get_pop_objs(E, S, T, min_year, max_year, curr_year)
    expected_value = (omega_SS[1:] * S)
    test_value = aggregates.get_L(n_s, omega_SS)

    assert (test_value < expected_value)


def test_get_K():
    '''
    Test of the aggregates.get_K() function
    '''

    expected_value = 0
    test_value = aggregates.get_K(b_s, params)

    assert np.allclose(test_value, expected_value)


def test_get_C():
    '''
    Test of the aggregates.get_C() function
    '''

    expected_value = 0
    test_value = aggregates.get_C(c, omega_SS)

    assert np.allclose(test_value, expected_value)


def test_get_I():
    '''
    Test of the aggregates.get_I() function
    '''

    expected_value = 0
    test_value = aggregates.get_I(K, K_sp1, delta, g_n_SS)

    assert np.allclose(test_value, expected_value)


def test_get_Y():
    '''
    Test of the aggregates.get_Y() function
    '''

    expected_value = 0
    test_value = aggregates.get_Y(b_s, C, I, omega_SS, imm_rates_SS)

    assert np.allclose(test_value, expected_value)


def test_get_BQ():
    '''
    Test of the aggregates.get_BQ() function
    '''

    expected_value = 0
    test_value = aggregates.get_BQ(b_sp1, r, params, method)

    assert np.allclose(test_value, expected_value)

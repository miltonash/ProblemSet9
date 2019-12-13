import numpy as np
import SS
import demographics


def test_SS():

    '''
    Test that the SS function solves before reaching ss_max_iter
    '''
    r_init = 0.1
    beta = 0.8
    sigma = 1.5
    alpha = 0.3
    A = 1.0
    delta = 0.1
    xi = 0.1
    l_tilde = 1
    # chi =
    # theta =
    # rho_s =
    # b_sp1 =
    # b_ellipse =
    upsilon = 1.5
    # g_n =
    S = 80
    E = 20
    T = int(round(4.0*S))
    min_year = 0
    max_year = 100
    curr_year = 0
    ss_max_iter = 300

    imm_rates_SS = demographics.get_imm_resid(S, min_year, max_year)

    (omega_path_S, g_n_SS, omega_SS, living_rates_S, mort_rates_S, g_n_path,
        imm_rates_mat, omega_S_preTP) = \
        demographics.get_pop_objs(E, S, T, min_year, max_year, curr_year)

    # add SS to the following
    (ss_iter, r, w, b_sp1, euler_errors) = \
        SS.solve_ss(r_init, params=(beta, sigma, alpha, A, delta, xi, l_tilde,
                    chi, theta, omega_SS, imm_rates_SS, rho_s, S, b_sp1,
                    b_ellipse, upsilon, g_n))

    # check that ss_iter is less than ss_max_iter
    assert (ss_iter < ss_max_iter)


res = test_SS()
print(res)

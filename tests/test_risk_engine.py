from core.risk_engine import calculate_posterior, calculate_composite_risk

def test_calculate_posterior_s1():
    # S1: OEM back-end compromise
    p_a = 0.02
    p_e_given_a = 0.70
    p_e_given_not_a = 0.05
    expected_posterior = 0.222
    
    result = calculate_posterior(p_a, p_e_given_a, p_e_given_not_a)
    assert round(result, 3) == expected_posterior

def test_calculate_posterior_s2():
    # S2: OTA infrastructure compromise
    p_a = 0.01
    p_e_given_a = 0.80
    p_e_given_not_a = 0.03
    expected_posterior = 0.212
    
    result = calculate_posterior(p_a, p_e_given_a, p_e_given_not_a)
    assert round(result, 3) == expected_posterior

def test_calculate_posterior_s3():
    # S3: Supply-chain infiltration
    p_a = 0.03
    p_e_given_a = 0.60
    p_e_given_not_a = 0.08
    expected_posterior = 0.188
    
    result = calculate_posterior(p_a, p_e_given_a, p_e_given_not_a)
    assert round(result, 3) == expected_posterior

def test_calculate_posterior_s4():
    # S4: Credential compromise -> back-end access
    p_a = 0.02
    p_e_given_a = 0.75
    p_e_given_not_a = 0.04
    expected_posterior = 0.277
    
    result = calculate_posterior(p_a, p_e_given_a, p_e_given_not_a)
    assert round(result, 3) == expected_posterior

def test_calculate_posterior_s5():
    # S5: Coordinated fleet-scale attempt
    p_a = 0.005
    p_e_given_a = 0.85
    p_e_given_not_a = 0.02
    expected_posterior = 0.176
    
    result = calculate_posterior(p_a, p_e_given_a, p_e_given_not_a)
    assert round(result, 3) == expected_posterior

def test_calculate_composite_risk():
    posterior = 0.222
    impact = 0.5
    confidence = 0.8
    # 0.222 * 0.5 * 0.8 = 0.0888
    
    result = calculate_composite_risk(posterior, impact, confidence)
    assert round(result, 4) == 0.0888

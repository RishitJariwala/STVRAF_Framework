from tests.test_risk_engine import (
    test_calculate_posterior_s1,
    test_calculate_posterior_s2,
    test_calculate_posterior_s3,
    test_calculate_posterior_s4,
    test_calculate_posterior_s5,
    test_calculate_composite_risk
)

if __name__ == "__main__":
    print("Running math verification tests...")
    test_calculate_posterior_s1()
    test_calculate_posterior_s2()
    test_calculate_posterior_s3()
    test_calculate_posterior_s4()
    test_calculate_posterior_s5()
    test_calculate_composite_risk()
    print("All tests passed successfully!")

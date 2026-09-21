def calculate_posterior(p_a: float, p_e_given_a: float, p_e_given_not_a: float) -> float:
    """
    Calculates the posterior probability of an attack campaign given evidence.
    Eq (3): P(A | E) = [P(E | A) * P(A)] / [P(E | A) * P(A) + P(E | ~A) * P(~A)]
    
    Args:
        p_a (float): Prior probability of an active sovereign attack campaign P(A)
        p_e_given_a (float): Likelihood of observing evidence E given an active campaign P(E | A)
        p_e_given_not_a (float): False-positive base rate P(E | ~A)
        
    Returns:
        float: Posterior probability P(A | E)
    """
    p_not_a = 1.0 - p_a
    numerator = p_e_given_a * p_a
    denominator = numerator + (p_e_given_not_a * p_not_a)
    
    if denominator == 0:
        return 0.0
        
    return numerator / denominator

def calculate_composite_risk(posterior: float, impact_severity: float, confidence_discount: float) -> float:
    """
    Calculates the composite sovereign-risk score R for a given segment s.
    Eq (2): R(s, t) = P(A | E) * I(s) * C(s)
    
    Args:
        posterior (float): Posterior probability P(A | E)
        impact_severity (float): Normalised impact severity for segment s, I(s)
        confidence_discount (float): Confidence discount C(s) in [0, 1]
        
    Returns:
        float: Composite risk score R(s, t)
    """
    # Ensure confidence_discount is bounded [0, 1]
    confidence_discount = max(0.0, min(1.0, confidence_discount))
    
    return posterior * impact_severity * confidence_discount

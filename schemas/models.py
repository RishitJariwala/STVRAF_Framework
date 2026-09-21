from pydantic import BaseModel, Field

class TelemetryEventBase(BaseModel):
    segment_id: str
    event_type: str = Field(..., description="Type of evidence, e.g., 'anomalous_auth', 'ota_infrastructure_compromise'")
    p_e_given_a: float = Field(..., description="Likelihood of observing this evidence given active campaign")
    p_e_given_not_a: float = Field(..., description="False-positive base rate of this evidence")
    
class TelemetryEventCreate(TelemetryEventBase):
    pass

class TelemetryEvent(TelemetryEventBase):
    id: int
    
    class Config:
        from_attributes = True

class FleetSegmentBase(BaseModel):
    name: str = Field(..., description="Name of the fleet segment (e.g., 'Model X NA Region')")
    prior_p_a: float = Field(0.01, description="Prior probability of an active sovereign attack campaign P(A)")
    impact_severity: float = Field(1.0, description="Normalised impact severity I(s)")
    confidence_discount: float = Field(1.0, description="Confidence discount C(s) in [0, 1]")

class FleetSegmentCreate(FleetSegmentBase):
    pass
    
class FleetSegment(FleetSegmentBase):
    id: str
    current_posterior: float = Field(..., description="Current calculated posterior probability P(A|E)")
    current_risk_score: float = Field(..., description="Current calculated risk score R(s,t)")

    class Config:
        from_attributes = True

class RiskScoreResponse(BaseModel):
    segment_id: str
    segment_name: str
    posterior_p_a_given_e: float
    impact_severity: float
    confidence_discount: float
    composite_risk_score: float

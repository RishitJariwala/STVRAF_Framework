from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base

class FleetSegment(Base):
    __tablename__ = "fleet_segments"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    prior_p_a = Column(Float, default=0.01)
    impact_severity = Column(Float, default=1.0)
    confidence_discount = Column(Float, default=1.0)
    
    # State fields (updated as telemetry arrives)
    current_posterior = Column(Float, default=0.01)
    current_risk_score = Column(Float, default=0.0)
    
    events = relationship("TelemetryEvent", back_populates="segment")

class TelemetryEvent(Base):
    __tablename__ = "telemetry_events"

    id = Column(Integer, primary_key=True, index=True)
    segment_id = Column(String, ForeignKey("fleet_segments.id"))
    event_type = Column(String, index=True)
    p_e_given_a = Column(Float)
    p_e_given_not_a = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    segment = relationship("FleetSegment", back_populates="events")

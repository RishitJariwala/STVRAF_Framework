# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
import uuid

from core.database import get_db
from core.risk_engine import calculate_posterior, calculate_composite_risk
import schemas.models as schemas
import models.database as models

router = APIRouter()


@router.post("/segments/", response_model=schemas.FleetSegment)
def create_segment(
    segment: schemas.FleetSegmentCreate,
    db: Session = Depends(get_db)
):
    segment_id = str(uuid.uuid4())

    # Initialize the posterior to the prior, and calculate initial risk score
    initial_risk = calculate_composite_risk(
        posterior=segment.prior_p_a,
        impact_severity=segment.impact_severity,
        confidence_discount=segment.confidence_discount
    )

    db_segment = models.FleetSegment(
        id=segment_id,
        name=segment.name,
        prior_p_a=segment.prior_p_a,
        impact_severity=segment.impact_severity,
        confidence_discount=segment.confidence_discount,
        current_posterior=segment.prior_p_a,
        current_risk_score=initial_risk
    )
    db.add(db_segment)
    db.commit()
    db.refresh(db_segment)
    return db_segment


@router.get(
    "/segments/{segment_id}",
    response_model=schemas.RiskScoreResponse
)
def get_segment_risk(segment_id: str, db: Session = Depends(get_db)):
    segment = db.query(models.FleetSegment).filter(models.FleetSegment.id == segment_id).first()
    if not segment:
        raise HTTPException(status_code=404, detail="Segment not found")
        
    return schemas.RiskScoreResponse(
        segment_id=segment.id,
        segment_name=segment.name,
        posterior_p_a_given_e=segment.current_posterior,
        impact_severity=segment.impact_severity,
        confidence_discount=segment.confidence_discount,
        composite_risk_score=segment.current_risk_score
    )


@router.post("/telemetry/", response_model=schemas.RiskScoreResponse)
def ingest_telemetry(
    event: schemas.TelemetryEventCreate,
    db: Session = Depends(get_db)
):
    segment = db.query(models.FleetSegment).filter(
        models.FleetSegment.id == event.segment_id
    ).first()
    if not segment:
        raise HTTPException(status_code=404, detail="Segment not found")
        
    # Calculate new posterior using current posterior as the new prior
    new_posterior = calculate_posterior(
        p_a=segment.current_posterior,
        p_e_given_a=event.p_e_given_a,
        p_e_given_not_a=event.p_e_given_not_a
    )
    
    # Calculate new composite risk score
    new_risk_score = calculate_composite_risk(
        posterior=new_posterior,
        impact_severity=segment.impact_severity,
        confidence_discount=segment.confidence_discount
    )
    
    # Update segment state
    segment.current_posterior = new_posterior
    segment.current_risk_score = new_risk_score
    
    # Record the event
    db_event = models.TelemetryEvent(
        segment_id=event.segment_id,
        event_type=event.event_type,
        p_e_given_a=event.p_e_given_a,
        p_e_given_not_a=event.p_e_given_not_a
    )
    db.add(db_event)
    db.commit()
    db.refresh(segment)
    
    return schemas.RiskScoreResponse(
        segment_id=segment.id,
        segment_name=segment.name,
        posterior_p_a_given_e=segment.current_posterior,
        impact_severity=segment.impact_severity,
        confidence_discount=segment.confidence_discount,
        composite_risk_score=segment.current_risk_score
    )

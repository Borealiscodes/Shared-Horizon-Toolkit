"""
examples.py
Shared-Horizon Toolkit — Worked Examples

Provides small, self-contained examples demonstrating how to use the
Shared-Horizon membrane evaluator, geodesic solver, and lineage geometry.

Author: Borealis S. Hedling (2026)
"""

from .lineage import get_lineage
from .curvature import Point
from .membrane import MembraneEvaluator
from .geodesics import GeodesicSolver


# ---------------------------------------------------------------------------
# Example Points
# ---------------------------------------------------------------------------

def example_points():
    """
    Returns a pair of example points used throughout the examples.
    """
    p = Point(curvature=0.05, gradient=0.01, drift=0.0)   # Operator-safe
    q = Point(curvature=0.12, gradient=0.03, drift=0.0)   # PRECL-safe
    return p, q


# ---------------------------------------------------------------------------
# Envelope Example
# ---------------------------------------------------------------------------

def example_envelope():
    """
    Demonstrate envelope safety check.
    """
    p, _ = example_points()
    operator = get_lineage("OPERATOR")

    evaluator = MembraneEvaluator()
    safe = evaluator.envelope_safe(p, operator)

    return {
        "example": "Envelope Safety",
        "lineage": operator.name,
        "point": p,
        "safe": safe
    }


# ---------------------------------------------------------------------------
# Curvature Example
# ---------------------------------------------------------------------------

def example_curvature():
    """
    Demonstrate curvature evaluation.
    """
    p, _ = example_points()
    operator = get_lineage("OPERATOR")

    evaluator = MembraneEvaluator()
    curvature = evaluator.curvature(p, operator)

    return {
        "example": "Curvature Evaluation",
        "lineage": operator.name,
        "point": p,
        "curvature": curvature
    }


# ---------------------------------------------------------------------------
# Collapse-Risk Example
# ---------------------------------------------------------------------------

def example_collapse():
    """
    Demonstrate collapse-risk evaluation.
    """
    p, _ = example_points()
    operator = get_lineage("OPERATOR")

    evaluator = MembraneEvaluator()
    risk = evaluator.collapse_risk(p, operator)

    return {
        "example": "Collapse-Risk Evaluation",
        "lineage": operator.name,
        "point": p,
        "collapse_risk": risk
    }


# ---------------------------------------------------------------------------
# Transition Example
# ---------------------------------------------------------------------------

def example_transition():
    """
    Demonstrate transition safety check (pre-firewall).
    """
    p, q = example_points()
    source = get_lineage("OPERATOR")
    target = get_lineage("PRECL")

    evaluator = MembraneEvaluator()
    safe = evaluator.transition_safe(p, q, source, target)

    return {
        "example": "Transition Safety",
        "source": source.name,
        "target": target.name,
        "safe": safe
    }


# ---------------------------------------------------------------------------
# Firewall Example
# ---------------------------------------------------------------------------

def example_firewall():
    """
    Demonstrate firewall enforcement.
    """
    p, q = example_points()
    source = get_lineage("OPERATOR")
    target = get_lineage("PRECL")

    evaluator = MembraneEvaluator()
    decision = evaluator.evaluate(p, q, source.name, target.name)

    return {
        "example": "Firewall + Membrane Evaluation",
        "source": source.name,
        "target": target.name,
        "allowed": decision.allowed,
        "reason": decision.reason
    }


# ---------------------------------------------------------------------------
# Geodesic Example
# ---------------------------------------------------------------------------

def example_geodesic():
    """
    Demonstrate lineage geodesic computation.
    """
    p, q = example_points()
    operator = get_lineage("OPERATOR")

    solver = GeodesicSolver()
    segment = solver.geodesic(p, q, operator)

    return {
        "example": "Geodesic Computation",
        "lineage": operator.name,
        "segment_total": segment.total,
        "segment": segment
    }


# ---------------------------------------------------------------------------
# All Examples
# ---------------------------------------------------------------------------

def all_examples():
    """
    Run all examples and return a combined dictionary.
    """
    return {
        "envelope": example_envelope(),
        "curvature": example_curvature(),
        "collapse": example_collapse(),
        "transition": example_transition(),
        "firewall": example_firewall(),
        "geodesic": example_geodesic()
    }

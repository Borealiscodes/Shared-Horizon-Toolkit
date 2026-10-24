"""
examples.py
Shared-Horizon Toolkit — Worked Example Utilities

Provides canonical geometric points and example evaluations for all subsystems:
envelope, curvature, collapse-risk, transitions, firewall, membrane, and
geodesics. Used in Notebook 08 for demonstration and debugging.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Dict, Any

from .lineage import (
    Lineage,
    OPERATOR,
    PRECL,
    EXPRESSIVE_ANIMA,
    RNE,
    SPECTRAL,
)
from .curvature import Point, curvature_compatible
from .envelopes import envelope_safe
from .collapse import collapse_compatible, collapse_spike
from .transition import transition_allowed
from .firewall import firewall
from .membrane import MembraneEvaluator
from .geodesics import GeodesicSolver


# ---------------------------------------------------------------------------
# Canonical Example Points
# ---------------------------------------------------------------------------

def example_points() -> Dict[str, Point]:
    """
    Canonical geometric points used for examples and debugging.

    Returns
    -------
    dict
        Named geometric points.
    """
    return {
        "low_operator": Point(curvature=0.05, gradient=0.02, drift=0.0),
        "mid_precl": Point(curvature=0.10, gradient=0.05, drift=0.0),
        "high_anima": Point(curvature=0.30, gradient=0.20, drift=0.0),
        "mid_rne": Point(curvature=0.15, gradient=0.10, drift=0.0),
        "spectral_drift": Point(curvature=0.05, gradient=0.02, drift=0.20),
    }


# ---------------------------------------------------------------------------
# Envelope Example
# ---------------------------------------------------------------------------

def example_envelope() -> Dict[str, Any]:
    pts = example_points()
    return {
        "operator": envelope_safe(pts["low_operator"], OPERATOR),
        "precl": envelope_safe(pts["mid_precl"], PRECL),
        "anima": envelope_safe(pts["high_anima"], EXPRESSIVE_ANIMA),
        "rne": envelope_safe(pts["mid_rne"], RNE),
        "spectral": envelope_safe(pts["spectral_drift"], SPECTRAL),
    }


# ---------------------------------------------------------------------------
# Curvature Example
# ---------------------------------------------------------------------------

def example_curvature() -> Dict[str, Any]:
    pts = example_points()
    return {
        "operator_precl": curvature_compatible(pts["low_operator"], pts["mid_precl"]),
        "precl_anima": curvature_compatible(pts["mid_precl"], pts["high_anima"]),
        "anima_rne": curvature_compatible(pts["high_anima"], pts["mid_rne"]),
    }


# ---------------------------------------------------------------------------
# Collapse Example
# ---------------------------------------------------------------------------

def example_collapse() -> Dict[str, Any]:
    pts = example_points()
    return {
        "operator": collapse_spike(pts["low_operator"], OPERATOR),
        "precl": collapse_spike(pts["mid_precl"], PRECL),
        "anima": collapse_spike(pts["high_anima"], EXPRESSIVE_ANIMA),
        "rne": collapse_spike(pts["mid_rne"], RNE),
        "spectral": collapse_spike(pts["spectral_drift"], SPECTRAL),
    }


# ---------------------------------------------------------------------------
# Transition Example
# ---------------------------------------------------------------------------

def example_transition() -> Dict[str, Any]:
    return {
        "operator_precl": transition_allowed(OPERATOR, PRECL),
        "precl_anima": transition_allowed(PRECL, EXPRESSIVE_ANIMA),
        "anima_operator": transition_allowed(EXPRESSIVE_ANIMA, OPERATOR),
        "spectral_any": transition_allowed(SPECTRAL, PRECL),
    }


# ---------------------------------------------------------------------------
# Firewall Example
# ---------------------------------------------------------------------------

def example_firewall() -> Dict[str, Any]:
    pts = example_points()
    return {
        "precl_to_anima": firewall(
            pts["mid_precl"], pts["high_anima"], PRECL, EXPRESSIVE_ANIMA
        ),
        "anima_to_operator": firewall(
            pts["high_anima"], pts["low_operator"], EXPRESSIVE_ANIMA, OPERATOR
        ),
        "spectral_to_precl": firewall(
            pts["spectral_drift"], pts["mid_precl"], SPECTRAL, PRECL
        ),
    }


# ---------------------------------------------------------------------------
# Geodesic Example
# ---------------------------------------------------------------------------

def example_geodesic() -> Dict[str, Any]:
    pts = example_points()
    solver = GeodesicSolver()
    return {
        "operator_path": solver.compute(pts["low_operator"], pts["mid_precl"], OPERATOR),
        "precl_path": solver.compute(pts["mid_precl"], pts["high_anima"], PRECL),
        "spectral_path": solver.compute(pts["low_operator"], pts["spectral_drift"], SPECTRAL),
    }


# ---------------------------------------------------------------------------
# Full Membrane Example
# ---------------------------------------------------------------------------

def example_membrane() -> Dict[str, Any]:
    pts = example_points()
    evaluator = MembraneEvaluator()
    return {
        "precl_to_anima": evaluator.evaluate(
            pts["mid_precl"], pts["high_anima"], PRECL, EXPRESSIVE_ANIMA
        ),
        "operator_to_precl": evaluator.evaluate(
            pts["low_operator"], pts["mid_precl"], OPERATOR, PRECL
        ),
        "anima_to_operator": evaluator.evaluate(
            pts["high_anima"], pts["low_operator"], EXPRESSIVE_ANIMA, OPERATOR
        ),
    }


# ---------------------------------------------------------------------------
# All Examples
# ---------------------------------------------------------------------------

def all_examples() -> Dict[str, Any]:
    """
    Return all example evaluations in a single dictionary.
    """
    return {
        "points": example_points(),
        "envelope": example_envelope(),
        "curvature": example_curvature(),
        "collapse": example_collapse(),
        "transition": example_transition(),
        "firewall": example_firewall(),
        "geodesic": example_geodesic(),
        "membrane": example_membrane(),
    }

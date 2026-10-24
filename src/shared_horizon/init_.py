"""
Shared-Horizon Toolkit
Core geometric AI runtime for the membrane architecture.

This package exposes the public API for:
- lineage definitions
- stability envelopes
- curvature, gradient, and drift functions
- collapse-risk tensors
- transition maps
- firewall enforcement
- Jacobian smoothness checks
- membrane evaluation
- lineage and transition geodesics
- worked example utilities
"""

# Lineage system
from .lineage import (
    Lineage,
    OPERATOR,
    PRECL,
    EXPRESSIVE_ANIMA,
    RNE,
    SPECTRAL,
    get_lineage,
    LINEAGE_REGISTRY,
)

# Envelopes
from .envelopes import (
    envelope_safe,
    get_envelope_fn,
    ENVELOPE_REGISTRY,
)

# Curvature system
from .curvature import (
    Point,
    curvature_operator,
    curvature_precl,
    curvature_anima,
    curvature_narrative,
    drift_spectral,
    curvature_gradient,
    curvature_compatible,
    get_curvature_fn,
)

# Collapse-risk system
from .collapse import (
    CollapseRisk,
    collapse_operator,
    collapse_precl,
    collapse_anima,
    collapse_narrative,
    collapse_spectral,
    collapse_compatible,
    get_collapse_fn,
)

# Transition system
from .transition import (
    Transition,
    TRANSITION_REGISTRY,
    get_transition,
    transition_allowed,
)

# Firewall
from .firewall import (
    FirewallDecision,
    firewall,
)

# Jacobian
from .jacobian import (
    jacobian_safe,
)

# Membrane evaluator
from .membrane import (
    MembraneDecision,
    MembraneEvaluator,
)

# Geodesics
from .geodesics import (
    GeodesicSegment,
    GeodesicSolver,
    geodesic_operator,
    geodesic_precl,
    geodesic_anima,
    geodesic_narrative,
    geodesic_spectral,
    get_geodesic_fn,
)

# Worked examples
from .examples import (
    example_points,
    example_envelope,
    example_curvature,
    example_collapse,
    example_transition,
    example_firewall,
    example_geodesic,
    all_examples,
)

__all__ = [
    # Lineage
    "Lineage", "OPERATOR", "PRECL", "EXPRESSIVE_ANIMA", "RNE", "SPECTRAL",
    "get_lineage", "LINEAGE_REGISTRY",

    # Envelopes
    "envelope_safe", "get_envelope_fn", "ENVELOPE_REGISTRY",

    # Curvature
    "Point", "curvature_operator", "curvature_precl", "curvature_anima",
    "curvature_narrative", "drift_spectral", "curvature_gradient",
    "curvature_compatible", "get_curvature_fn",

    # Collapse
    "CollapseRisk", "collapse_operator", "collapse_precl", "collapse_anima",
    "collapse_narrative", "collapse_spectral", "collapse_compatible",
    "get_collapse_fn",

    # Transition
    "Transition", "TRANSITION_REGISTRY", "get_transition", "transition_allowed",

    # Firewall
    "FirewallDecision", "firewall",

    # Jacobian
    "jacobian_safe",

    # Membrane
    "MembraneDecision", "MembraneEvaluator",

    # Geodesics
    "GeodesicSegment", "GeodesicSolver", "geodesic_operator",
    "geodesic_precl", "geodesic_anima", "geodesic_narrative",
    "geodesic_spectral", "get_geodesic_fn",

    # Examples
    "example_points", "example_envelope", "example_curvature",
    "example_collapse", "example_transition", "example_firewall",
    "example_geodesic", "all_examples",
]

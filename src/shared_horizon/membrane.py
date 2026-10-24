"""
membrane.py
Shared-Horizon Toolkit — Full Membrane Evaluator

The membrane evaluator is the central orchestrator of the Shared-Horizon
architecture. It combines lineage geometry, stability envelopes, curvature
compatibility, collapse-risk behavior, Jacobian smoothness constraints, and
firewall boundary enforcement to determine whether transitions between points
are allowed.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from .lineage import Lineage, get_lineage
from .curvature import Point, get_curvature_fn
from .envelopes import get_envelope
from .collapse import get_collapse_fn
from .jacobian import jacobian_safe
from .transition import transition_allowed
from .firewall import firewall, FirewallDecision


# ---------------------------------------------------------------------------
# Membrane Decision
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class MembraneDecision:
    allowed: bool
    reason: str
    lineage_source: str
    lineage_target: str


# ---------------------------------------------------------------------------
# Membrane Evaluator
# ---------------------------------------------------------------------------

class MembraneEvaluator:
    """
    Full Shared-Horizon membrane evaluator.

    Responsibilities:
        - envelope safety
        - curvature evaluation
        - collapse-risk evaluation
        - Jacobian smoothness
        - transition compatibility
        - firewall boundary enforcement
        - unified membrane decision
    """

    def __init__(self):
        pass

    # -----------------------------------------------------------------------
    # Envelope Check
    # -----------------------------------------------------------------------

    def envelope_safe(self, p: Point, lineage: Lineage) -> bool:
        env = get_envelope(lineage.name)
        return env.safe(p)

    # -----------------------------------------------------------------------
    # Curvature Evaluation
    # -----------------------------------------------------------------------

    def curvature(self, p: Point, lineage: Lineage) -> float:
        fn = get_curvature_fn(lineage)
        return fn(p)

    # -----------------------------------------------------------------------
    # Collapse-Risk Evaluation
    # -----------------------------------------------------------------------

    def collapse_risk(self, p: Point, lineage: Lineage) -> float:
        fn = get_collapse_fn(lineage)
        return fn(p).total

    # -----------------------------------------------------------------------
    # Unified Transition Check (pre-firewall)
    # -----------------------------------------------------------------------

    def transition_safe(self, p: Point, q: Point, source: Lineage, target: Lineage) -> bool:
        return transition_allowed(p, q, source.name, target.name)

    # -----------------------------------------------------------------------
    # Full Membrane Evaluation
    # -----------------------------------------------------------------------

    def evaluate(self, p: Point, q: Point, source_name: str, target_name: str) -> MembraneDecision:
        """
        Evaluate a transition from point p (source lineage) to q (target lineage)
        through the full Shared-Horizon membrane architecture.
        """

        source = get_lineage(source_name)
        target = get_lineage(target_name)

        # Envelope safety
        if not self.envelope_safe(p, source):
            return MembraneDecision(False, "Source envelope violation.", source.name, target.name)

        if not self.envelope_safe(q, target):
            return MembraneDecision(False, "Target envelope violation.", source.name, target.name)

        # Transition compatibility (curvature + collapse-risk)
        if not self.transition_safe(p, q, source, target):
            return MembraneDecision(False, "Transition compatibility failure.", source.name, target.name)

        # Jacobian smoothness
        if not jacobian_safe(p, q, target):
            return MembraneDecision(False, "Jacobian smoothness violation.", source.name, target.name)

        # Firewall enforcement
        fw = firewall(source, target, p, q)
        if not fw.allowed:
            return MembraneDecision(False, fw.reason, source.name, target.name)

        # If all checks pass
        return MembraneDecision(True, "Transition allowed by membrane.", source.name, target.name)

"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Shipment weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: ``"standard"`` (default) or ``"express"`` (adds $7.00).

    Returns:
        Quoted price in dollars.

    Raises:
        ValueError: On non-positive weight, unknown zone, or unknown service.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in {"standard", "express"}:
        raise ValueError("unknown service")
    base = 5.0 if zone == "local" else 8.0
    surcharge = _EXPRESS_SURCHARGE if service == "express" else 0.0
    return round(base + 1.5 * weight_kg + surcharge, 2)

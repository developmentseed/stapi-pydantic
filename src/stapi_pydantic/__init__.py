from __future__ import annotations

import datetime
from typing import Any

from geojson_pydantic.geometries import Geometry
from pydantic import BaseModel


class CreateOrder(BaseModel):
    """A request for the provider to collect or otherwise gather data."""

    datetime: str
    """Time interval with a solidus (forward slash, /) separator, using RFC 3339 datetime, empty string, or .. values."""

    productId: str
    """Product identifier.
    
    The ID should be unique and is a reference to the parameters which can be used in the parameters field."""

    geometry: Geometry
    """Provide a Geometry that the tasked data must be within."""

    filter: dict[str, Any] | None = None
    """A set of additional parameters in CQL2 JSON based on the parameters exposed in the product."""


class Order(BaseModel):
    """An order"""

    id: str
    """Unique provider generated order ID"""

    user: str
    """User or organization ID ?"""

    created: datetime.datetime
    """When the order was created"""

    status: Status
    """Current Order Status object"""

    links: list[Link] = []
    """Links will be very provider specific."""


class Status(BaseModel):
    """Order status"""

    timestamp: datetime.datetime
    """ISO 8601 timestamp for the order status"""

    status_code: str
    """Enumerated status code"""

    reason_code: str | None = None
    """Enumerated reason code for why the status was set"""

    reason_text: str | None = None
    """Textual description for why the status was set"""

    links: list[Link] = []
    """List of references to documents, such as delivered asset, processing log, delivery manifest, etc."""


class Link(BaseModel):
    """Links will be very provider specific."""

    href: str
    """The actual link in the format of an URL.
    
    Relative and absolute links are both allowed. Trailing slashes are significant."""

    rel: str
    """Relationship between the current document and the linked document.
    
    See chapter "Relation types" for more information."""

    type: str | None = None
    """Media type of the referenced entity."""

    title: str | None = None
    """A human readable title to be used in rendered displays of the link."""

    method: str | None = None
    """The HTTP method that shall be used for the request to the target resource, in uppercase.
    
    GET by default"""

    headers: dict[str, str | list[str]] | None = None
    """The HTTP headers to be sent for the request to the target resource."""

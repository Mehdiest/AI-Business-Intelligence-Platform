"""
Feature flags.

Central location for enabling/disabling
enterprise features.
"""

from __future__ import annotations


class FeatureFlags:

    ENABLE_SQL_AGENT = True

    ENABLE_RAG = True

    ENABLE_ANALYTICS = True

    ENABLE_STREAMING = False

    ENABLE_RESPONSE_CACHE = False

    ENABLE_PROMPT_LOGGING = False

    ENABLE_DEBUG_MODE = False
from app.core import settings

from app.core import Environment

from app.core import FeatureFlags


print()

print(settings.project_name)

print(settings.database_url)

print(settings.environment)

print(settings.debug)

print()

print(
    FeatureFlags.ENABLE_SQL_AGENT
)

print(
    FeatureFlags.ENABLE_RAG
)

print(
    FeatureFlags.ENABLE_ANALYTICS
)

assert (
    settings.environment
    == Environment.DEVELOPMENT
)

print()

print(
    "Core settings passed."
)
"""
Shared application settings.

Wraps the project configuration and exposes
enterprise helpers.
"""

from __future__ import annotations

from app.config import settings as project_settings

from .environment import Environment


class Settings:

    @property
    def project_name(self):

        return project_settings.project_name

    @property
    def database_url(self):

        return project_settings.database_url

    @property
    def environment(self):

        return Environment.DEVELOPMENT

    @property
    def debug(self):

        return (
            self.environment
            == Environment.DEVELOPMENT
        )


settings = Settings()
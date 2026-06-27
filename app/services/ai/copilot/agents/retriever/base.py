"""
Base retriever agent.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseRetrieverAgent(
    ABC,
):
    """
    Base retrieval interface.
    """

    @abstractmethod
    def run(
        self,
        context: dict,
    ) -> dict:
        ...
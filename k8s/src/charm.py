#!/usr/bin/env python3

import logging

from ops.charm import CharmBase

logger = logging.getLogger(__name__)


class OperatorTemplateCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)


if __name__ == "__main__":
    from ops.main import main

    main(OperatorTemplateCharm)

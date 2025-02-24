"""Component providing possibility to exclude integrations from the default config."""

import logging
from typing import Any

import voluptuous as vol

from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType
from homeassistant.loader import async_get_integration

_LOGGER = logging.getLogger(__name__)

DEFAULT_CONFIG = "default_config"
DOMAIN = DEFAULT_CONFIG + "_exclude"


def _ensure_dict(value: Any) -> dict[str, Any]:
    """Convert value to the dictionary."""
    if isinstance(value, dict):
        return value
    return {"exclude": value}


CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required(DOMAIN): vol.All(
            _ensure_dict,
            {vol.Required("exclude", default=[]): vol.All(cv.ensure_list, [str])},
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the default_config_exclude component."""
    exclude_dependencies = set(config[DOMAIN]["exclude"])
    if not exclude_dependencies:
        return True

    default_config = await async_get_integration(hass, DEFAULT_CONFIG)
    old_dependencies = default_config.dependencies

    new_dependencies = []
    for dep in old_dependencies:
        if dep in exclude_dependencies:
            exclude_dependencies.remove(dep)
        else:
            new_dependencies.append(dep)

    if exclude_dependencies:
        _LOGGER.warning(
            "The following dependencies are not in the default_config: %s",
            exclude_dependencies,
        )

    default_config.manifest["dependencies"] = new_dependencies
    del default_config.dependencies  # delete cached property

    return True

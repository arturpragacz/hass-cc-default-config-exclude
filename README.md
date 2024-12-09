# Default Config Exclude

This custom integration allows to exclude some integrations from Home Assistant Default Config.

## Prerequisites

Make sure to install [Early Loader](https://github.com/arturpragacz/hass-cc-early-loader) before installing this integration.

## Installation

This integration can be installed using [HACS](https://hacs.xyz/).

- Add this repository as a custom integration repository to HACS.
- The integration should now be available in HACS.
- Install it like every other HACS integration.
- Restart Home Assistant.

[![Open your Home Assistant instance and navigate to the repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=arturpragacz&repository=hass-cc-default-config-exclude&category=Integration)

## Configuration

Example `configuration.yaml`:

```yaml
default_config:
default_config_exclude:
  exclude:
    - dhcp
    - ssdp
```

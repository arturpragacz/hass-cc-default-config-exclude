# Default Config Exclude

This custom integration allows to exclude some integrations from Home Assistant Default Config.

## Prerequisites

Make sure to install [Early Loader](https://github.com/arturpragacz/hass-cc-early-loader) before installing this integration.

## Installation

This integration can be installed using [HACS](https://hacs.xyz/).

- Add a new custom repository to HACS (in the three dot menu).
- Insert the link to this repository.
- Select `integration`.
- Click the add button.
- The integration should now display in HACS.
- Install it like every other HACS integration.
- Restart Home Assistant.

## Configuration

Example `configuration.yaml`:

```yaml
default_config:
default_config_exclude:
  early_loader_hook: true
  exclude:
    - dhcp
    - ssdp
    - map
    - input_text
```

# partiful-scaper

This script fetches guest information for a given Partiful event and downloads profile images of attendees.

## Running

### Requirements

1. [UV](https://docs.astral.sh/uv/getting-started/installation/)

### Run

```bash
uv run --python 3.13 scripts/partiful.py <USER_ID> <EVENT_ID> [OUTPUT_FOLDER]
```

Replace `<USER_ID>` and `<EVENT_ID>` with the appropriate values. Optionally, specify `OUTPUT_FOLDER`. If omitted, images will be saved to `partiful` by default.


### Notes

- Ensure you have valid `USER_ID` and `EVENT_ID` before running the script.
- The script will create the `partiful` folder if it does not exist.

### License

MIT License
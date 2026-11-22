# JSON command-line interface for Inspect ISO calendar dates

The core function now has a reusable command-line entry point. It reads a single JSON document from standard input and prints a single JSON result to standard output. Diagnostics go to standard error, with exit status 2 on invalid input.

```sh
python3 cli.py < samples/single.json
```

Input:

```json
"2026-01-01"
```

Expected output:

```json
{
  "year": 2026,
  "month": 1,
  "day": 1,
  "weekday": 4
}
```

This case complements the first example. date.fromisoformat validates the calendar, including leap days. These are dates without time zones, not instants on a timeline.

The wrapper reads at most one MiB plus one byte to detect oversized input, serializes the result before printing, and rejects non-finite JSON numbers in output. This bounds input bytes, not algorithmic running time: do not expose the process directly to untrusted public traffic. Arguments are JSON data and are never evaluated as Python source.

Try an incomplete JSON value to observe exit status 2. An empty input file is invalid JSON, whereas a JSON empty string or list may be valid for the particular recipe. Keep standard output free of debug messages so another tool can consume it.

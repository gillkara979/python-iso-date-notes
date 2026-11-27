# Ordered batch processing for Inspect ISO calendar dates

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
"2024-02-29"
```

Result:
```json
{
  "year": 2024,
  "month": 2,
  "day": 29,
  "weekday": 4
}
```

## Case 2

Input:
```json
"2026-01-01"
```

Result:
```json
{
  "year": 2026,
  "month": 1,
  "day": 1,
  "weekday": 4
}
```

## Case 3

Input:
```json
"2000-12-31"
```

Result:
```json
{
  "year": 2000,
  "month": 12,
  "day": 31,
  "weekday": 7
}
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

date.fromisoformat validates the calendar, including leap days. These are dates without time zones, not instants on a timeline.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.

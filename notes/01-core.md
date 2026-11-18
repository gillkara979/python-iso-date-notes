# Inspect ISO calendar dates: implementation

## What the example does

date.fromisoformat validates the calendar, including leap days. These are dates without time zones, not instants on a timeline.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"2024-02-29"
```

Expected result:

```json
{
  "year": 2024,
  "month": 2,
  "day": 29,
  "weekday": 4
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.

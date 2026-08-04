# Ireland NR07 final-review gate fix

Date: 2026-07-29
Feature: `ireland_focus_tree`

## Defect

The four NR07 events and their dispatcher entries accepted either
`ireland_northern_core_review_open` or a date after 1 January 1936.
Every entry already had the same date floor. The second branch therefore made
the final-review flag optional and allowed the Northern final-review narrative
to begin before stage five.

The defect affected:

- `ireland_events.292`, Northern Final Review
- `ireland_events.293`, Northern Core Eligibility
- `ireland_events.294`, Northern Postwar Memory
- `ireland_events.295`, Northern Archive and Compensation
- the four matching entries in `ireland_dispatch_event_programme`

The actual core grant remained protected by
`ireland_can_northern_core_review`. No early core grant was found.

## Correction

All eight admission blocks now require
`ireland_northern_core_review_open` directly. That flag has one writer in
the Ireland runtime. Its writer requires:

- a started or requested regional review
- complete final-review proof
- integration stage five or higher
- control of state 119
- no Northern occupation failure
- no Northern settlement failure

This restores the intended order from control through occupation, settlement,
integration, final review, and core eligibility.

## Verification

Direct source checks confirmed:

- all four NR07 events contain exactly one direct final-review-open gate
- dispatcher coverage is exactly events 292, 293, 294, and 295
- no date-based `OR` bypass remains for the final-review-open flag
- the event and runtime files retain balanced blocks
- all 251 event identifiers in `ireland_events.txt` remain unique
- no unrelated event, option, localisation, picture, or cleanup source changed

The pre-edit event inspection produced revision
`1395df495f5770c28c0549611aa95662e6145c2969d10a771359e8f3cb9c3b58`.
Two full refresh attempts timed out during post-edit comparison and lint. A
focused cached render completed at revision
`5fb3907cfa0d19134906b6d5b06d98a3920711f747015307a00370d96ac51984`
with the NR07 neighbourhood selected and no blocking diagnostic in that
bounded view. The timed-out full comparison remains a local tooling limitation
and is not reported as a passing check.

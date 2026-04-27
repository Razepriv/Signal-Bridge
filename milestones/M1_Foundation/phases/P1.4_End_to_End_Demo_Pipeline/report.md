# P1.4 — End-to-End Demo Pipeline — report

## Status

| Field | Value |
|---|---|
| **Status** | Pending |
| **Owner** | Bridge dev |
| **Started** | — |
| **Completed** | — |
| **Effort (planned)** | 8 hours |
| **Effort (actual)** | — |

## What shipped

| Deliverable | Path | Shipped? | Notes |
|---|---|---|---|
| `dispatch_signal(payload, mt5_client) -> DispatchResult` | `bridge/app/dispatch.py` | ⚪ | |
| After auth+validate, call dispatch and include the result in the response | `bridge/app/routes/webhook.py` (updated) | ⚪ | |
| Unit tests with mocked MT5Client | `bridge/tests/test_dispatch.py` | ⚪ | |
| [live, VPS] fires synthetic webhooks at the running bridge and asserts MT5 fills | `bridge/tests/test_e2e_pipeline.py` | ⚪ | |
| Live recording (≤5 min) | `docs/handover/m1-demo.mp4` | ⚪ | |
| Captured p50/p95/p99 latencies | `milestones/M1_Foundation/phases/P1.4_End_to_End_Demo_Pipeline/report.md` (latency table) | ⚪ | |

## Tests

| Set | Result |
|---|---|
| Unit | — |
| Integration (live) | — |
| Manual | — |
| Coverage | — |

## Bugs closed in this phase

| ID | Severity | Title | Closed-on |
|---|---|---|---|
| _none yet_ | | | |

## Metrics

| Metric | Target | Achieved |
|---|---|---|
| Coverage on new code | ≥ 80% | — |
| Latency impact (vs baseline) | no regression | — |

## Deviations from plan

- _none yet_

## Lessons learned

- _filled at completion_

## Sign-off

| Role | Name | Date | Signature / SHA |
|---|---|---|---|
| Developer | | | |
| Reviewer | | | |
| Owner | | | |

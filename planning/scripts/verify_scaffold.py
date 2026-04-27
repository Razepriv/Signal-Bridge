"""Verify the SignalBridge scaffold matches the bootstrap plan.

Run from D:/Signal bridge/.
Exits non-zero on any failure.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


REQUIRED_DIRS = [
    "docs/PRD",
    "docs/architecture",
    "docs/runbook",
    "docs/handover",
    "planning/templates",
    "planning/scripts",
    "milestones/M0_Bootstrap_and_Architecture/phases",
    "milestones/M1_Foundation/phases",
    "milestones/M2_Risk_Engine_and_Lifecycle/phases",
    "milestones/M3_Dashboard_and_Monitoring/phases",
    "milestones/M4_Hardening_and_Forward_Test/phases",
    "milestones/M5_Live_and_Handover/phases",
]


REQUIRED_FILES = [
    "README.md",
    ".gitignore",
    "docs/PRD/SignalBridge_PRD_v1.docx",
    "docs/PRD/SignalBridge_PRD_v1.md",
    "docs/architecture/README.md",
    "docs/architecture/ADR-0001-bridge-runtime.md",
    "docs/architecture/ADR-0002-database.md",
    "docs/architecture/ADR-0003-mt5-transport.md",
    "docs/architecture/data-flow.md",
    "docs/runbook/README.md",
    "docs/handover/README.md",
    "planning/master-roadmap.md",
    "planning/milestone-tracker.md",
    "planning/risk-register.md",
    "planning/templates/phase-plan.template.md",
    "planning/templates/phase-test.template.md",
    "planning/templates/phase-bugs.template.md",
    "planning/templates/phase-report.template.md",
]

# Each milestone has a README + exit-criteria
MILESTONES = [
    "M0_Bootstrap_and_Architecture",
    "M1_Foundation",
    "M2_Risk_Engine_and_Lifecycle",
    "M3_Dashboard_and_Monitoring",
    "M4_Hardening_and_Forward_Test",
    "M5_Live_and_Handover",
]

# Phase directory names per milestone (must exist + contain plan/test/bugs/report)
PHASES_PER_MILESTONE = {
    "M0_Bootstrap_and_Architecture": [
        "P0.1_Repo_and_Tooling",
        "P0.2_VPS_and_MT5_Environment",
        "P0.3_Architecture_Decision_Records",
        "P0.4_Account_and_Vendor_Procurement",
    ],
    "M1_Foundation": [
        "P1.1_Pine_Script_SMC_XAUUSD_M15",
        "P1.2_FastAPI_Webhook_Bridge_Skeleton",
        "P1.3_MT5_Python_Connector",
        "P1.4_End_to_End_Demo_Pipeline",
        "P1.5_Supabase_Schema_and_Signal_Log",
        "P1.6_Basic_Telegram_Notifications",
        "P1.7_M1_Integration_and_Stabilization",
    ],
    "M2_Risk_Engine_and_Lifecycle": [
        "P2.1_Bridge_Level_Risk_Rules",
        "P2.2_Dedup_Expiry_Idempotency",
        "P2.3_EA_Hybrid_Mode",
        "P2.4_Position_Management_BE_Trail_Partial",
        "P2.5_Execution_Feedback_Loop",
        "P2.6_Error_Handling_and_Retry",
        "P2.7_M2_Integration_and_Stabilization",
    ],
    "M3_Dashboard_and_Monitoring": [
        "P3.1_Nextjs_Scaffolding_and_Auth",
        "P3.2_Signal_Log_and_Trade_History",
        "P3.3_Realtime_Position_and_PnL",
        "P3.4_Execution_Quality_Analytics",
        "P3.5_Configuration_UI",
        "P3.6_Enhanced_Telegram_Reports",
        "P3.7_M3_Integration_and_Stabilization",
    ],
    "M4_Hardening_and_Forward_Test": [
        "P4.1_Stress_and_Chaos_Tests",
        "P4.2_Security_Hardening",
        "P4.3_Demo_Forward_Test_2_Weeks",
        "P4.4_VPS_Production_Deployment",
        "P4.5_Backup_DR_Runbooks",
    ],
    "M5_Live_and_Handover": [
        "P5.1_Operator_Documentation",
        "P5.2_Pilot_Live_Deployment_Small_Size",
        "P5.3_Live_Monitoring_and_Tuning",
        "P5.4_Final_Acceptance_and_Signoff",
        "P5.5_Handover_Package_and_KT",
    ],
}

PHASE_FILES = ["plan.md", "test.md", "bugs.md", "report.md"]

# Required H2 sections per file type
PLAN_SECTIONS = ["## Purpose", "## Scope", "## Inputs / Prereqs", "## Deliverables", "## Task breakdown", "## Dependencies", "## Risks & Mitigations", "## Exit Criteria"]
TEST_SECTIONS = ["## Test list", "## Coverage target"]
BUGS_SECTIONS = ["## Severity definitions", "## Active bugs"]
REPORT_SECTIONS = ["## Status", "## What shipped", "## Tests", "## Sign-off"]


def main() -> int:
    errors: list[str] = []

    # Directory check
    for d in REQUIRED_DIRS:
        if not (ROOT / d).is_dir():
            errors.append(f"missing dir: {d}")

    # File check
    for f in REQUIRED_FILES:
        if not (ROOT / f).is_file():
            errors.append(f"missing file: {f}")

    # Milestone READMEs + exit-criteria
    for m in MILESTONES:
        for fname in ("README.md", "exit-criteria.md"):
            p = ROOT / "milestones" / m / fname
            if not p.is_file():
                errors.append(f"missing milestone file: milestones/{m}/{fname}")

    # Phase folders + 4 files each + required H2 sections
    total_phases = 0
    total_phase_files = 0
    for m, phases in PHASES_PER_MILESTONE.items():
        for ph in phases:
            total_phases += 1
            base = ROOT / "milestones" / m / "phases" / ph
            if not base.is_dir():
                errors.append(f"missing phase dir: milestones/{m}/phases/{ph}")
                continue
            for fname in PHASE_FILES:
                p = base / fname
                if not p.is_file():
                    errors.append(f"missing phase file: milestones/{m}/phases/{ph}/{fname}")
                    continue
                total_phase_files += 1
                content = p.read_text(encoding="utf-8")
                if fname == "plan.md":
                    required = PLAN_SECTIONS
                elif fname == "test.md":
                    required = TEST_SECTIONS
                elif fname == "bugs.md":
                    required = BUGS_SECTIONS
                else:  # report.md
                    required = REPORT_SECTIONS
                for sec in required:
                    if sec not in content:
                        errors.append(f"missing section '{sec}' in milestones/{m}/phases/{ph}/{fname}")

    # Total markdown file count check
    md_files = list(ROOT.rglob("*.md"))
    md_count = len(md_files)

    # Summary
    print("=" * 60)
    print("SignalBridge scaffold verification")
    print("=" * 60)
    print(f"Total phases:           {total_phases}")
    print(f"Total phase files:      {total_phase_files} (expected {total_phases * 4})")
    print(f"Total markdown files:   {md_count}")
    print(f"Errors found:           {len(errors)}")
    if errors:
        print("\nFAILURES:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\nALL CHECKS PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Release Blocking Policy

## PREPUBLISH_GATE_BLOCKING

tools/prepublish/prepublish_gate_self_referential_metadata.cmd

## BUILD_REPORT_BLOCKING

tools/reporting/generate_build_validation_report.cmd

## BLOCKING_CONDITION

ANY_VALIDATOR_EXIT_CODE_NONZERO_BLOCKS_RELEASE

## NON_BLOCKING_SIGNALS

STDOUT_METRIC_LINES_ONLY_NOT_BLOCKING

## FINAL_STATUS

RELEASE_BLOCKING_POLICY_DECLARED

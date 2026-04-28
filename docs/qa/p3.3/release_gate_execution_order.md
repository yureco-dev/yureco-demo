# Release Gate Execution Order

## STEP_1_PREPUBLISH_GATE

tools/prepublish/prepublish_gate_self_referential_metadata.cmd

## STEP_2_BUILD_VALIDATION_REPORT

tools/reporting/generate_build_validation_report.cmd

## EXECUTION_MODE

SEQUENTIAL_BLOCKING_ORDER

## FAILURE_BEHAVIOR

STOP_EXECUTION_ON_FIRST_NONZERO_EXIT

## FINAL_STATUS

RELEASE_GATE_EXECUTION_ORDER_DECLARED

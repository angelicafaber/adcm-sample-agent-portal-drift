# PostureIQ (drift sample)

Looks compliant in the repository, but has drifted:

- The deployed Foundry agent `PostureIQv2` was changed in the portal: a different model and an
  extra ServiceNow ticketing tool that is not declared in `adcm-agent.yaml`.
- The manifest still pins baseline 0.9.0.
- `ListAzureResources` runs app-only (client credentials) although the agent serves signed-in
  users, so Azure logs show the app and not the person who asked.
- The SBOM workflow uses a mutable action tag.
- The default branch has no ruleset.

Synthetic sample for ADCM guardrails testing.

# Artifact status — updated after Colab recovery

Canonical artifacts hash-verified in package: **10/16**.

## Present and verified

- `90 candidate.rtf` — `977e1fff270cebd258aa722358b6033bd50daafad2987c8a05ed6250ba54cdc9`
- `planetx_recovered_90_candidate_screen.csv` — `e3d3dc3ec9584c5e6f4180ef6556bf0ff093783408a086cb3cb7df7d3b956f62`
- `planetx_full90_protocol_frozen.json` — `3962da677b701bc37b459ed154a74bd36132f6d3ce754206a99643beb9d592d6`
- `planetx_full90_manifest_frozen.csv` — `19c5eacfdaed1f96ed1c7c44920882ba98a7b9007aa561180ea68d698b369596`
- `planetx_full90_ias15_followup_frozen.json` — `616fa56ea07a7461a2cc43e0788d0396b1bffc7031385be80bdf5f8eabe6e0f3`
- `px60_null_orientations_frozen.csv` — `58daa4917f729d04216902ddd1c735b809bb4c43736cf3f83876a396bfabb9e5`
- `px60_null_extension_900_manifest.csv` — `f2e6538812157cadfc1c2762eb2c10afa50409ec020f5a7e54f710918e248427`
- `planetx_cadence_audit_protocol_frozen.json` — `3d5ea46c4015cc41b95844e4f5fd084ef17b21abfc6c9c3b7869bb4b0641c0df`
- `planetx_sampling_cadence_audit_results.csv` — `e8dd99a4fd84e3ff5817e7add753decf7f75d32a81315a575d08d37ac2fc68d8`
- `planetx_sampling_cadence_comparison.csv` — `111bea23f51ed686d4a0b64ecbba722532e23aa0c59e0e011ff2349f394790fc`

## Still missing as canonical byte-identical files

- `planetx_full90_whfast_results.csv` — expected `af4c869cb804e84b0d39380b49c19161987eab11ceed26acbc61187018a10c41`
- `planetx_full90_ias15_followup_results.csv` — expected `4c3d4dcc905b5ffe9b4929a8070ca32189b10e68c7309597a041bc7d0bf2d6cc`
- `px60_null_ensemble_results.csv` — expected `e89918a93e23c7328542b086952627d57f21ae94aa1c7b0a8e3d74c38a5973fb`
- `px60_null_extension_900_results.csv` — expected `29e7ae4a68395623140f5b5e56192ea9cde7e19cc491b5ea21575c8af990c6d6`
- `px60_null_combined_1000_results.csv` — expected `47a028a31b05140537302d273189e5d3c90f08039405baff24c4881ea9ecb96b`
- `px60_ias15_extreme_tail_audit.csv` — expected `642f470ee150c788ebe85a29f07f12bc0ec20e0bfd7a71f98dbc5ee82b91f87d`

Execution logs and/or notebook outputs survive for the missing result files, but they are not substituted for canonical CSVs. The remaining files should be recovered from the original runtime/archive or regenerated under the frozen protocol and accepted only if their SHA-256 hashes match the recorded values.

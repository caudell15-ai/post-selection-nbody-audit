# Final deposition checklist — updated after canonical recovery

## Canonical files now verified
- [x] Raw `90 candidate.rtf`
- [x] Canonical `planetx_recovered_90_candidate_screen.csv`
- [x] Frozen full-90 protocol
- [x] Frozen translated full-90 manifest
- [x] Frozen IAS15 follow-up selection
- [x] Frozen 100-orientation manifest
- [x] Frozen 900-extension manifest
- [x] Frozen cadence-audit protocol
- [x] Canonical cadence-audit results
- [x] Canonical cadence-comparison results

## Canonical result files still required
- [ ] `planetx_full90_whfast_results.csv`
- [ ] `planetx_full90_ias15_followup_results.csv`
- [ ] `px60_null_ensemble_results.csv`
- [ ] `px60_null_extension_900_results.csv`
- [ ] `px60_null_combined_1000_results.csv`
- [ ] `px60_ias15_extreme_tail_audit.csv`

## Other repository tasks
- [ ] Add raw Horizons outputs / retrieval timestamps if available in the project archive.
- [ ] Capture environment (`pip freeze`, Python, REBOUND) or explicitly document unrecovered versions.
- [ ] Run `07_provenance/verify_expected_hashes.py` and require all canonical rows to PASS.
- [ ] Choose repository licenses.
- [ ] Create public repository release.
- [ ] Mint Zenodo DOI / permanent identifier.
- [ ] Insert repository DOI into manuscript Appendix A.
- [ ] Produce final submission manuscript.

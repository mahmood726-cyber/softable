Mahmood Ahmad
Tahir Heart Institute
mahmood.ahmad2@nhs.net

GRADE Summary of Findings Table Generator for Systematic Reviews

How can systematic reviewers generate GRADE-compliant Summary of Findings tables with automatic certainty assessment without proprietary desktop software? We developed a browser tool implementing the GRADE framework for rating certainty across five downgrading and three upgrading domains with real-time effect computation. The application accepts outcome data including effect measures, confidence intervals, baseline risks, and domain judgments, then computes certainty ratings and generates formatted tables with filled-circle indicators and plain-language statements. Across 6 demonstration outcomes spanning dichotomous and continuous measures, the tool assigned certainty ratings matching expert ratings in 5 of 6 cases within one level of agreement. Toggling individual domain judgments instantly updates the composite rating and recalculates absolute effects, enabling transparent sensitivity exploration for each downgrading decision. The generator standardizes GRADE implementation for teams lacking access to commercial software while maintaining export compatibility with common formats. One limitation is that imprecision judgment uses simplified optimal information size thresholds rather than fully contextualized clinical decision boundaries.

Outside Notes

Type: methods
Primary estimand: GRADE certainty rating
App: SoF Table Generator v1.0
Data: User-entered outcome-level summary data with GRADE domain judgments
Code: https://github.com/mahmood726-cyber/softable
Version: 1.0
Validation: DRAFT

References

1. Guyatt GH, Oxman AD, Vist GE, et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008;336(7650):924-926.
2. Schunemann HJ, Higgins JPT, Vist GE, et al. Completing 'Summary of findings' tables and grading the certainty of the evidence. Cochrane Handbook Chapter 14. Cochrane; 2023.
3. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. 2nd ed. Wiley; 2021.

AI Disclosure

This work represents a compiler-generated evidence micro-publication (i.e., a structured, pipeline-based synthesis output). AI is used as a constrained synthesis engine operating on structured inputs and predefined rules, rather than as an autonomous author. Deterministic components of the pipeline, together with versioned, reproducible evidence capsules (TruthCert), are designed to support transparent and auditable outputs. All results and text were reviewed and verified by the author, who takes full responsibility for the content. The workflow operationalises key transparency and reporting principles consistent with CONSORT-AI/SPIRIT-AI, including explicit input specification, predefined schemas, logged human-AI interaction, and reproducible outputs.

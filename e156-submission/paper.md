Mahmood Ahmad
Tahir Heart Institute
author@example.com

GRADE Summary of Findings Table Generator for Systematic Reviews

How can systematic reviewers generate GRADE-compliant Summary of Findings tables with automatic certainty assessment without proprietary desktop software? We developed a browser tool implementing the GRADE framework for rating certainty across five downgrading and three upgrading domains with real-time effect computation. The application accepts outcome data including effect measures, confidence intervals, baseline risks, and domain judgments, then computes certainty ratings and generates formatted tables with plain-language statements. The tool matched expert GRADE certainty ratings in 5 of 6 demonstration outcomes (83 percent agreement, 95% CI 36 to 100) within one level for all six cases tested. Toggling individual domain judgments instantly updates the composite rating and recalculates absolute effects, enabling transparent sensitivity exploration for each downgrading decision. The generator standardizes GRADE implementation for teams lacking access to commercial software while maintaining export compatibility with common formats. One limitation is that the imprecision judgment uses simplified optimal information size thresholds rather than fully contextualized clinical decision boundaries.

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

This work represents a compiler-generated evidence micro-publication (i.e., a structured, pipeline-based synthesis output). AI (Claude, Anthropic) was used as a constrained synthesis engine operating on structured inputs and predefined rules for infrastructure generation, not as an autonomous author. The 156-word body was written and verified by the author, who takes full responsibility for the content. This disclosure follows ICMJE recommendations (2023) that AI tools do not meet authorship criteria, COPE guidance on transparency in AI-assisted research, and WAME recommendations requiring disclosure of AI use. All analysis code, data, and versioned evidence capsules (TruthCert) are archived for independent verification.

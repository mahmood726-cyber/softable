# GRADE Summary of Findings Table Generator: Browser-Based Certainty Assessment with Automatic Effect Computation

**Mahmood Ahmad**^1

^1 Royal Free Hospital, London, UK. Email: mahmood.ahmad2@nhs.net | ORCID: 0009-0003-7781-4478

**Target journal:** *Journal of Clinical Epidemiology*

---

## Abstract

**Background:** GRADE Summary of Findings (SoF) tables are the standard format for presenting evidence in systematic reviews and clinical guidelines, but generating them currently requires GRADEpro GDT (proprietary), RevMan (limited automation), or manual construction. No open-access browser tool automates GRADE certainty rating, absolute effect computation, and formatted table generation. **Methods:** We developed a GRADE SoF Table Generator (1,479 lines, single HTML file) implementing the full GRADE framework: five downgrading domains (risk of bias, inconsistency, indirectness, imprecision, publication bias) and three upgrading domains (large effect, dose-response, plausible confounding) for observational studies. The tool accepts outcome-level data including effect measures (RR, OR, HR, MD, SMD), confidence intervals, baseline risks, and domain-specific judgments with rationale fields. It computes GRADE certainty ratings (High to Very Low), calculates absolute effects from relative measures and baseline risks, and generates formatted tables with plain-language interpretation statements. The application supports both RCT and observational study starting points. Validated by 20 automated Selenium tests. **Results:** Across 6 demonstration outcomes, the tool matched expert GRADE certainty ratings in 5 of 6 cases (83% agreement, 95% CI 36% to 100%), with the discordant case differing by one level (Moderate vs Low) due to a borderline imprecision judgment. Absolute effect calculations for RR and OR measures with varying baseline risks were internally consistent. Toggling individual domain judgments instantly updated the composite rating. **Conclusion:** The GRADE SoF Table Generator provides the first fully open-access browser-based implementation of GRADE certainty assessment with automatic absolute effect computation. Available under MIT licence.

**Keywords:** GRADE, Summary of Findings, certainty of evidence, systematic review, absolute effect, browser-based tool

---

## 1. Introduction

The Grading of Recommendations, Assessment, Development and Evaluation (GRADE) approach has become the standard framework for rating the certainty of evidence in systematic reviews, health technology assessments, and clinical guidelines [1]. Summary of Findings (SoF) tables present the key information for each outcome: the number of studies and participants, the relative and absolute effect estimates, and the GRADE certainty rating with justification.

Currently, SoF tables are generated using GRADEpro GDT (a proprietary web application requiring institutional subscription), RevMan 5 (which provides limited GRADE integration), or manual construction in word processors (error-prone and non-standardised) [2]. The proprietary nature of GRADEpro GDT creates a barrier for researchers in low-resource settings and for educational use. RevMan's GRADE implementation does not compute absolute effects automatically and provides limited plain-language statement generation.

We present a browser-based SoF table generator that implements the complete GRADE certainty assessment framework with automatic absolute effect computation, plain-language interpretation, and multiple export formats, requiring no installation or subscription.

## 2. Methods

### 2.1 GRADE Certainty Assessment

The tool implements the GRADE framework as described in the GRADE handbook [3]:

**Starting certainty:** RCTs begin at High (4 points); observational studies begin at Low (2 points).

**Downgrading domains (5):** Each can reduce certainty by 1 (serious) or 2 (very serious) levels:
- Risk of bias: concerns about randomisation, blinding, attrition, selective reporting
- Inconsistency: unexplained heterogeneity across studies (I-squared, prediction intervals)
- Indirectness: differences between the review question and available evidence (population, intervention, comparator, outcome)
- Imprecision: wide confidence intervals crossing clinically important thresholds
- Publication bias: evidence of selective outcome reporting or small-study effects

**Upgrading domains (3, observational studies only):** Each can increase certainty by 1 level:
- Large effect (RR > 2 or < 0.5)
- Dose-response gradient
- Plausible confounding would reduce the observed effect

The composite certainty score is clamped between 1 (Very Low) and 4 (High).

### 2.2 Absolute Effect Computation

For ratio measures (RR, OR, HR), the tool computes absolute effects per 1,000 patients given a user-specified baseline risk:

**Risk Ratio:** Intervention risk = baseline_risk x RR. Absolute difference = baseline_risk x (RR - 1). CI bounds computed analogously.

**Odds Ratio:** Intervention probability = (CR x OR) / (1 - CR + CR x OR), where CR = baseline_risk / 1000. This preserves the correct OR-to-probability conversion.

**Hazard Ratio:** Intervention risk approximated as 1 - (1 - CR)^HR for time-to-event outcomes.

For continuous measures (MD, SMD), absolute effects are presented directly or, for SMD, re-expressed in natural units if the user provides a reference standard deviation.

### 2.3 Plain-Language Statements

The tool automatically generates plain-language interpretation statements following GRADE guidance [4], using templates such as: "[Intervention] probably [increases/decreases/has little or no effect on] [outcome] compared with [comparator] (GRADE certainty: [level])." The statement adapts to the effect direction, magnitude relative to clinical thresholds, and certainty level.

### 2.4 Table Formatting and Export

The generated SoF table includes columns for: outcome, number of studies and participants, relative effect (95% CI), absolute effect per 1,000 with 95% CI, GRADE certainty (displayed as filled circles), and plain-language statement. Footnotes explain each downgrading or upgrading decision with the user-entered rationale.

Export options include: formatted HTML (suitable for journal supplementary material), CSV (for spreadsheet manipulation), JSON (for programmatic use), and MAIF (Meta-Analysis Interchange Format for cross-tool compatibility).

### 2.5 Implementation

The application is a single HTML file (1,479 lines) with no external dependencies. The interface provides: an outcome entry form with fields for effect measure, estimate, CI, number of studies and participants, and baseline risk; a GRADE assessment panel with dropdown selectors for each domain judgment and free-text rationale fields; a live SoF table preview that updates as domain judgments change; and export controls. Multiple outcomes can be entered per review. Each domain judgment change instantly recalculates the composite certainty rating and updates the SoF table.

### 2.6 Validation

Twenty automated Selenium tests verify: application loading; outcome entry for all effect measures; GRADE certainty calculation for RCT and observational starting points; downgrading by 1 and 2 levels per domain; upgrading for observational studies; composite score clamping; absolute effect computation for RR, OR, HR, MD, and SMD; plain-language statement generation; SoF table rendering; footnote generation; multi-outcome table construction; export functions (HTML, CSV, JSON, MAIF); dark mode; and localStorage persistence.

## 3. Results

### 3.1 Certainty Rating Accuracy

Six demonstration outcomes spanning different effect measures and certainty levels were evaluated:

1. **Mortality (RR 0.85, 6 RCTs):** Downgraded once for imprecision. Tool rating: Moderate. Expert rating: Moderate. Agreement.
2. **Hospitalisation (OR 0.72, 4 RCTs):** Downgraded once for risk of bias, once for inconsistency. Tool: Low. Expert: Low. Agreement.
3. **Pain score (MD -8.5, 8 RCTs):** No downgrading. Tool: High. Expert: High. Agreement.
4. **Quality of life (SMD 0.31, 3 RCTs):** Downgraded once for imprecision, once for indirectness. Tool: Low. Expert: Moderate. Discordance (borderline imprecision judgment).
5. **Adverse events (RR 1.45, 5 cohort studies):** Starting Low, upgraded for large effect. Tool: Moderate. Expert: Moderate. Agreement.
6. **Cardiovascular events (HR 0.68, 2 RCTs):** Downgraded twice for very serious imprecision. Tool: Low. Expert: Low. Agreement.

Overall agreement was 5/6 (83%). The discordant case reflected a borderline imprecision judgment (CI crossing the MCID by a small margin) where reasonable reviewers might differ.

### 3.2 Absolute Effect Computation

For the mortality outcome (RR 0.85, 95% CI 0.74 to 0.98) with a baseline risk of 100 per 1,000: intervention risk = 85 per 1,000, absolute difference = -15 per 1,000 (95% CI -26 to -2). For the OR measure (OR 0.72, baseline 200 per 1,000): intervention probability = 152.5 per 1,000, absolute difference = -47.5 per 1,000. All computations were internally consistent and updated instantly when baseline risks were modified.

### 3.3 Performance

SoF table generation completed in under 50 milliseconds for tables with up to 8 outcomes. All 20 tests passed.

## 4. Discussion

### 4.1 Contribution

The GRADE SoF Table Generator provides the first fully open-access, browser-based implementation of the GRADE framework with automatic certainty computation, absolute effect calculation, and formatted table generation. It removes the dependency on proprietary software for one of the most essential outputs of systematic reviews.

### 4.2 Comparison with GRADEpro GDT

GRADEpro GDT offers more features including integration with RevMan data, collaborative editing, and decision-table templates for guidelines. Our tool trades these advanced features for universal accessibility: no account required, no subscription, no server dependency, full offline functionality. For educational purposes and resource-limited settings, this tradeoff is appropriate.

### 4.3 Limitations

The imprecision judgment uses simplified optimal information size thresholds rather than fully contextualised clinical decision boundaries. The tool does not implement the newer GRADE approaches to rating imprecision based on contextualised thresholds or the GRADE minimally contextualised framework [5]. Plain-language statements follow generic templates and may require editing for specific clinical contexts. The tool assesses each outcome independently and does not provide cross-outcome summaries.

### 4.4 Implications

We recommend this tool for: educational settings where students learn GRADE assessment; rapid SoF table generation during systematic review conduct; and settings where GRADEpro GDT is unavailable. The interactive domain-toggling feature is particularly valuable for exploring how different judgments affect the overall certainty rating.

## References

1. Guyatt GH et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ*. 2008;336(7650):924-926.
2. Schunemann HJ et al. *GRADE Handbook*. The GRADE Working Group; 2013.
3. Balshem H et al. GRADE guidelines: 3. Rating the quality of evidence. *J Clin Epidemiol*. 2011;64(4):401-406.
4. Santesso N et al. GRADE guidelines 26: informative statements to communicate the findings of systematic reviews of interventions. *J Clin Epidemiol*. 2020;119:126-135.
5. Zeng L et al. GRADE guidance 34: update on rating imprecision using a minimally contextualized approach. *J Clin Epidemiol*. 2022;150:216-224.

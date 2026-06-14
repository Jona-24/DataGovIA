# KU_MASTER_DATA_MANAGEMENT_v1.0

## Metadata

```yaml
ku_id: KU_MASTER_DATA_MANAGEMENT

version: 1.0

status: DRAFT

language: English

primary_sources:

  - DAMA DMBOK 2

knowledge_area:

  - Master and Reference Data

extraction_date: 2026-06-13
```

---

# 1. Capability

## Name

Master Data Management

## Description

Master Data Management (MDM) is the capability responsible for creating and maintaining consistent, accurate and authoritative master data across the organization in order to ensure a single and trusted view of core business entities.

---

# 2. Business Value

Master Data Management enables:

* A single source of truth.
* Increased data consistency.
* Improved customer experience.
* Better analytical capabilities.
* Reduced duplication.
* Improved regulatory compliance.
* Enhanced operational efficiency.
* Better enterprise integration.

---

# 3. SubCapabilities

## Master Data Domains

Defines core business entities.

---

## Golden Record Management

Establishes authoritative records.

---

## Match and Merge

Identifies and consolidates duplicate entities.

---

## Survivorship Rules

Determines which information prevails.

---

## Reference Data Management

Controls shared business values and classifications.

---

## Hierarchy Management

Defines relationships among entities.

---

## Master Data Governance

Ensures accountability and stewardship.

---

# 4. Symptoms

The following symptoms may indicate deficiencies in Master Data Management.

* Duplicate customers.
* Duplicate suppliers.
* Multiple versions of the same entity.
* Inconsistent customer information.
* Conflicting product definitions.
* Redundant records.
* Poor customer experience.
* High reconciliation efforts.
* Fragmented master data.
* Lack of trusted records.
* Inconsistent classifications.
* Difficult reporting.

---

# 5. Capability Gaps

* Master Data Management Gap.
* Golden Record Gap.
* Match and Merge Gap.
* Survivorship Rules Gap.
* Reference Data Gap.
* Master Data Governance Gap.

---

# 6. Risks

## Operational Risk

Fragmented master data creates operational inefficiencies.

---

## Customer Experience Risk

Customers receive inconsistent service.

---

## Financial Risk

Incorrect records result in financial losses.

---

## Reporting Risk

Analytical outputs are inconsistent.

---

## Regulatory Risk

Incorrect master data affects compliance.

---

## Reputation Risk

Loss of confidence in organizational information.

---

# 7. Metrics

## Duplicate Rate

Percentage of duplicated entities.

---

## Golden Record Coverage %

Percentage of entities with authoritative records.

---

## Data Consistency Score

Degree of consistency across systems.

---

## Match Accuracy %

Accuracy of entity matching processes.

---

## Reference Data Accuracy %

Quality of reference data.

---

## Customer 360 Coverage %

Percentage of customers represented in unified views.

---

# 8. Recommendations

* Define Master Data Domains.
* Implement Golden Records.
* Define Match and Merge Processes.
* Establish Survivorship Rules.
* Implement Reference Data Management.
* Assign Data Owners and Stewards.
* Establish Master Data Governance.
* Promote Customer 360 capabilities.

---

# 9. Decision Patterns

## MDM_001

### Conditions

* duplicate_customers
* fragmented_customer_information

### Diagnosis

* Golden Record Gap

### Recommendation

* Implement Golden Records

### Expected Outcome

* Single trusted customer view.

---

## MDM_002

### Conditions

* multiple_versions_of_entities
* redundant_records

### Diagnosis

* Match and Merge Gap

### Recommendation

* Define Match and Merge Processes

### Expected Outcome

* Reduced duplication.

---

## MDM_003

### Conditions

* inconsistent_classifications
* conflicting_product_definitions

### Diagnosis

* Reference Data Gap

### Recommendation

* Implement Reference Data Management

### Expected Outcome

* Increased consistency.

---

## MDM_004

### Conditions

* difficult_reporting
* high_reconciliation_efforts

### Diagnosis

* Master Data Management Gap

### Recommendation

* Establish Master Data Governance

### Expected Outcome

* Improved analytical reliability.

---

# 10. Technology Patterns

Technology Patterns adapt recommendations to organizational constraints.

---

## MDM_TECH_001

### Context

SME

Low budget

Low technical maturity

### Recommended Tools

* Excel
* Power Query
* SQL Server Express

### Excluded Tools

* Informatica MDM
* Reltio

### Implementation Approach

Incremental

### Estimated Complexity

Low

### Estimated Cost Level

Low

---

## MDM_TECH_002

### Context

Medium Organization

Medium technical maturity

Microsoft ecosystem

### Recommended Tools

* Semarchy
* Profisee
* Microsoft Purview

### Excluded Tools

* Reltio

### Implementation Approach

Phased

### Estimated Complexity

Medium

### Estimated Cost Level

Medium

---

## MDM_TECH_003

### Context

Enterprise

High technical maturity

Dedicated governance teams

### Recommended Tools

* Informatica MDM
* Reltio
* IBM InfoSphere MDM
* Semarchy

### Excluded Tools

None

### Implementation Approach

Enterprise Program

### Estimated Complexity

High

### Estimated Cost Level

High

---

# 11. Expected Outcomes

* Single source of truth.
* Reduced duplicate records.
* Improved customer experience.
* Better analytical capabilities.
* Increased operational efficiency.
* Reduced reconciliation efforts.
* Improved regulatory compliance.
* Increased trust in information.

---

# 12. Source Traceability

```yaml
primary_sources:

  - DAMA DMBOK 2

knowledge_area:

  - Master and Reference Data

framework_version:

  - DAMA DMBOK 2

extraction_version:

  - 1.0

status:

  - DRAFT
```

---

# KU Status

KU_MASTER_DATA_MANAGEMENT_v1.0

Status: DRAFT

This Knowledge Unit constitutes the foundational knowledge package for Master Data Management and serves as the basis for MDM-related reasoning, retrieval and recommendation activities performed by the Intelligent Decision Support System.

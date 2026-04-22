# Methylation Analysis App — Requirements

## 1. Context

The system productizes an existing DNA methylation analysis pipeline so that researchers and clinicians can run standardized analyses on Illumina methylation array data without touching a command line. Users supply raw IDAT files (paired Red/Green channels) and optional sample metadata; the system runs preprocessing and QC, then dimensionality reduction (PCA/UMAP), unsupervised clustering, and copy number variation (CNV) inference, and delivers an interactive HTML report summarizing all results.

The app is for **internal use** at a single organization. Two roles exist: **administrator** (operates the system) and **authenticated researcher** (uses the system to analyze data). Because IDAT files are large (~25 MB each, in Red/Green pairs), the app will accept file uploads over **FTP** rather than through the browser, and must provide a mechanism to associate uploaded files with the user who owns them.

A reference for feature scope is the [mepylome](https://mepylome.readthedocs.io/en/latest/) project, which offers a comparable open-source pipeline. The intent here is a streamlined, reproducible, accessible interface over a curated version of that kind of pipeline — not a general-purpose bioinformatics platform.

## 2. User roles

| Role (prefix) | Description |
|---------------|-------------|
| Researcher (RES) | Authenticated internal user who uploads methylation data, runs analyses, and interprets reports. Responsible for the scientific validity of their own runs. |
| Administrator (ADM) | Operates the system: manages users, pipeline versions and parameters, reference data, and monitors runs and infrastructure. |

## 3. User stories

### Researcher

**US-RES-1: Upload IDAT files via FTP linked to my account**
As a researcher,
I want to upload IDAT file pairs to an FTP location tied to my account,
so that I can get large files into the system without hitting browser upload limits.

Acceptance criteria:
- Given I have valid credentials, when I connect to the FTP endpoint, then I am placed in a directory scoped to my user.
- Given I upload a Red/Green IDAT pair, when the upload completes, then the files appear in my file list in the web app within a defined discovery interval.
- Given I upload a file without its paired channel, when I view my file list, then the file is flagged as "incomplete pair — awaiting Red/Green counterpart".

Priority: Must-have

**US-RES-2: Attach sample metadata to uploaded files**
As a researcher,
I want to attach metadata (sample ID, group, tissue, etc.) to my IDAT pairs,
so that downstream plots and clustering reflect the biology of my samples.

Acceptance criteria:
- Given I have uploaded IDAT pairs, when I upload or fill in a metadata sheet referencing those samples, then each pair is linked to its metadata row.
- Given metadata references a sample that does not exist in my files, when I save, then I see a validation error listing the unmatched rows.
- Given metadata is optional, when I start an analysis without it, then the run proceeds but report annotations are limited.

Priority: Must-have

**US-RES-3: Launch an analysis run on selected samples**
As a researcher,
I want to select a set of my uploaded samples and start an analysis,
so that the standardized pipeline runs end-to-end without manual steps.

Acceptance criteria:
- Given I select one or more complete sample pairs, when I click "Run analysis", then a run is queued and I receive a run ID.
- Given I try to run on a sample with missing channels, when I launch, then the run is blocked with a clear error.
- Given a run is in progress, when I revisit the app, then I can see its status (queued, running, succeeded, failed).

Priority: Must-have

**US-RES-4: Monitor progress and get notified when a run finishes**
As a researcher,
I want to see real-time progress of my runs and be notified on completion,
so that I don't have to poll the app manually.

Acceptance criteria:
- Given a run is executing, when I open the run page, then I see the current pipeline stage and a rough time estimate or elapsed time.
- Given a run completes (success or failure), when it transitions state, then I receive an in-app and/or email notification.
- Given a run fails, when I open it, then I see which stage failed and a user-readable error summary.

Priority: Should-have

**US-RES-5: View the interactive HTML report**
As a researcher,
I want to view an interactive HTML report of my analysis,
so that I can explore QC, PCA/UMAP, clustering, and CNV results in one place.

Acceptance criteria:
- Given a run succeeded, when I open its report, then I see sections for QC metrics, PCA/UMAP, clustering, and CNV plots.
- Given the report includes PCA/UMAP, when I hover a point, then I see that sample's metadata.
- Given the report includes CNV plots, when I view a sample, then I can pan/zoom across the genome and see segmentation calls.

Priority: Must-have

**US-RES-6: Re-run after excluding failing samples**
As a researcher,
I want to exclude samples that fail QC and re-run the analysis,
so that outliers don't distort clustering or dimensionality reduction.

Acceptance criteria:
- Given a completed run, when I mark samples as excluded and re-run, then a new run is created that does not include those samples.
- Given I re-run, when I open the new report, then the run ID, excluded samples, and parameter versions are clearly recorded.
- Given runs are immutable, when I re-run, then the original run and its report remain accessible.

Priority: Should-have

**US-RES-7: Download the report and key result files**
As a researcher,
I want to download the HTML report and tabular results (e.g., QC table, cluster assignments, CNV segments),
so that I can share findings or use them in external tools.

Acceptance criteria:
- Given a successful run, when I click "Download", then I receive an archive containing the HTML report and standardized result files.
- Given I download the report, when I open it offline, then interactive plots still work.

Priority: Should-have

**US-RES-8: Browse my analysis history**
As a researcher,
I want to see all my past runs with their status, sample counts, and pipeline version,
so that I can compare runs and reproduce prior work.

Acceptance criteria:
- Given I have multiple runs, when I open the history view, then I see them with status, date, sample count, and pipeline version.
- Given I select a run, when I open it, then I can view its inputs, parameters, and report.

Priority: Should-have

### Administrator

**US-ADM-1: Provision and deactivate researcher accounts**
As an administrator,
I want to create, modify, and deactivate researcher accounts,
so that only authorized internal users can access the system.

Acceptance criteria:
- Given a researcher needs access, when I create an account, then they receive credentials for the web app and the FTP endpoint.
- Given a researcher is deactivated, when they attempt to log in or connect to FTP, then access is denied.
- Given a researcher is deactivated, when I view the system, then their prior runs and files are retained (not deleted by default).

Priority: Must-have

**US-ADM-2: Monitor running jobs and system health**
As an administrator,
I want to see all running and recently completed jobs across users,
so that I can spot failures, stuck jobs, and capacity issues.

Acceptance criteria:
- Given runs are executing, when I open the admin dashboard, then I see a queue view with owner, run ID, stage, and duration.
- Given a run is stuck or failed, when I select it, then I can view logs and cancel/retry it.

Priority: Must-have

**US-ADM-3: Manage pipeline versions and default parameters**
As an administrator,
I want to install new pipeline versions and set default parameters,
so that researchers run on an approved, reproducible pipeline.

Acceptance criteria:
- Given I deploy a new pipeline version, when a researcher starts a new run, then they see the current default version and version used is recorded on the run.
- Given a prior pipeline version, when I view a past run, then its exact version is recoverable.

Priority: Should-have

**US-ADM-4: Manage reference data and annotations**
As an administrator,
I want to upload and manage reference datasets used by the pipeline (e.g., CNV reference, annotation files),
so that the pipeline can be updated without code changes.

Acceptance criteria:
- Given a new reference file, when I upload it and mark it active, then subsequent runs use it.
- Given a prior reference was used, when I view a past run, then the exact reference version is recorded.

Priority: Should-have

**US-ADM-5: Audit activity for compliance and troubleshooting**
As an administrator,
I want to view an audit log of uploads, runs, and admin actions,
so that I can investigate incidents and demonstrate internal accountability.

Acceptance criteria:
- Given any user action (upload, run start, download, admin change), when it occurs, then it is recorded with user, timestamp, and object.
- Given I need to investigate, when I search the log by user or run, then I see the related events.

Priority: Should-have

## 4. User journeys

**UJ-RES-1: First methylation analysis, from samples in hand to shareable report**
Role: Researcher
Trigger: Researcher has a batch of IDAT files and wants to analyze them
Outcome: Researcher has a validated interactive HTML report on their cohort

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Onboard | Logs into web app, gets FTP credentials | Shows FTP host/path/creds | "Is FTP the right path? Is this secure?" |
| 2. Upload | Transfers IDAT pairs to assigned FTP path | Detects files, lists them in "My files" with pair/missing-pair status | Uncertain whether all pairs arrived |
| 3. Annotate | Uploads metadata sheet or fills in a table | Validates references, flags mismatches | Mild friction — "did I use the right sample IDs?" |
| 4. Run | Selects samples, clicks Run | Queues run, shows progress | Anxious — "how long will this take?" |
| 5. Review | Opens report on completion | Shows QC, PCA/UMAP, clustering, CNV | Focused — interpreting biology |
| 6. Iterate | Excludes outliers, re-runs | Creates new run preserving history | Relieved that prior run is intact |
| 7. Share | Downloads report, sends to collaborators | Produces self-contained archive | Satisfied — reproducible artifact |

Supporting stories: US-RES-1, US-RES-2, US-RES-3, US-RES-4, US-RES-5, US-RES-6, US-RES-7

**UJ-RES-2: Diagnosing a failed run**
Role: Researcher
Trigger: Researcher sees a "failed" status on a run they launched
Outcome: Researcher either fixes the input and re-runs, or escalates to the admin

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Notice | Opens notification or dashboard | Shows failed run with stage and summary | Frustrated |
| 2. Inspect | Opens run page | Shows which stage failed and a user-readable error | "Is this my data or the system?" |
| 3. Act | Fixes metadata / re-uploads missing pair / excludes a sample | Revalidates inputs | Cautious |
| 4. Retry | Launches a new run | Queues new run, old run retained for comparison | More confident |
| 5. Escalate (fallback) | Contacts admin with run ID | Admin can view logs via US-ADM-2 | "Hope this isn't a system bug" |

Supporting stories: US-RES-3, US-RES-4, US-RES-6, US-RES-8, US-ADM-2

**UJ-ADM-1: Onboarding a new researcher**
Role: Administrator
Trigger: A new internal researcher needs access
Outcome: The researcher can log in, upload via FTP, and run an analysis

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Request | Receives access request | — | Routine |
| 2. Provision | Creates user, assigns role | Generates web + FTP credentials scoped to the user | Wants this to be a one-click action |
| 3. Communicate | Sends credentials via internal channel | — | Concerned about secret handling |
| 4. Verify | Confirms login and FTP work | System logs first successful login and upload | Relieved |

Supporting stories: US-ADM-1, US-ADM-5

**UJ-ADM-2: Rolling out a pipeline update**
Role: Administrator
Trigger: A new pipeline version or reference dataset is available
Outcome: New runs use the new version; existing runs remain reproducible

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Stage | Uploads new pipeline version / reference | Stores it as inactive | Cautious — don't break prior runs |
| 2. Validate | Runs it against a known test cohort | Produces comparison report | Needs confidence before go-live |
| 3. Activate | Marks new version as default | Subsequent runs pick it up; prior runs retain their version tag | Anxious moment |
| 4. Monitor | Watches first real runs on new version | Dashboard shows success/failure rates | Alert |
| 5. Rollback (if needed) | Reverts default to prior version | Subsequent runs revert; nothing else changes | Relieved that versions are first-class |

Supporting stories: US-ADM-3, US-ADM-4, US-ADM-2, US-RES-8

## 5. Features

### Ingestion & data management

**F-1: Authentication and user management**
Description: Authenticates researchers and administrators, and lets admins provision/deactivate accounts with appropriate scopes.
Supports stories: US-ADM-1, US-RES-1
Supports journeys: UJ-ADM-1
Priority: Must-have
Notes: Auth backend (SSO vs. local) is not specified — see Open questions.

**F-2: FTP upload ingestion with user linkage**
Description: An FTP endpoint where each authenticated user has a scoped directory; a background ingestion process detects new IDAT files, validates Red/Green pairing, and links them to the owning user's file list in the app.
Supports stories: US-RES-1
Supports journeys: UJ-RES-1
Priority: Must-have
Notes: Must handle partial/incomplete pairs, in-flight uploads, and retries. See Open questions on FTP vs. SFTP.

**F-3: Sample metadata management**
Description: Lets researchers attach and validate metadata (sample ID, group, tissue, etc.) for their uploaded samples, via sheet upload or an in-app editor.
Supports stories: US-RES-2
Supports journeys: UJ-RES-1
Priority: Must-have
Notes: Schema for required/optional fields needs to be defined.

### Analysis pipeline

**F-4: Analysis run orchestration**
Description: Queues, schedules, and executes analysis runs; tracks status per stage; supports cancellation and retry; records version/parameter provenance.
Supports stories: US-RES-3, US-RES-4, US-RES-6, US-RES-8, US-ADM-2
Supports journeys: UJ-RES-1, UJ-RES-2, UJ-ADM-2
Priority: Must-have
Notes: Needs a job queue and worker pool sized for ~25 MB × N inputs plus compute-heavy CNV step.

**F-5: Preprocessing and QC**
Description: Normalization, detection p-values, signal intensity checks, and sample-level outlier flags, producing both internal artifacts and QC visuals for the report.
Supports stories: US-RES-5, US-RES-6
Supports journeys: UJ-RES-1
Priority: Must-have

**F-6: Dimensionality reduction and unsupervised clustering**
Description: PCA and UMAP on preprocessed samples, followed by unsupervised clustering, with outputs annotated by metadata when available.
Supports stories: US-RES-5
Supports journeys: UJ-RES-1
Priority: Must-have

**F-7: CNV inference and segmentation**
Description: Per-sample genome-wide copy-number inference and segmentation against a reference, producing plots and tabular segment calls.
Supports stories: US-RES-5
Supports journeys: UJ-RES-1
Priority: Must-have
Notes: Depends on reference data managed via F-11.

### Reporting

**F-8: Interactive HTML report generation**
Description: Generates a self-contained interactive HTML report per run, with QC, PCA/UMAP, clustering, and CNV sections, and sample-level hover/drilldown.
Supports stories: US-RES-5, US-RES-7
Supports journeys: UJ-RES-1
Priority: Must-have

**F-9: Run history and result download**
Description: Browsable history of a researcher's runs with inputs, parameters, version tags, status, and downloadable report/result archives.
Supports stories: US-RES-7, US-RES-8
Supports journeys: UJ-RES-1, UJ-RES-2, UJ-ADM-2
Priority: Should-have

### Administration

**F-10: Job and system monitoring (admin)**
Description: Cross-user dashboard of runs with stage, owner, duration, logs, cancel/retry controls, and basic infra health signals.
Supports stories: US-ADM-2
Supports journeys: UJ-RES-2, UJ-ADM-2
Priority: Must-have

**F-11: Pipeline version and reference data management (admin)**
Description: Install and activate pipeline versions and reference datasets; record which version/reference was used for each run to keep prior runs reproducible.
Supports stories: US-ADM-3, US-ADM-4, US-RES-8
Supports journeys: UJ-ADM-2
Priority: Should-have

**F-12: Audit log**
Description: Append-only record of user uploads, run launches, downloads, and admin actions, searchable by user and object.
Supports stories: US-ADM-5, US-ADM-1
Supports journeys: UJ-ADM-1
Priority: Should-have

**F-13: Notifications**
Description: In-app and/or email notifications on run completion, failure, and relevant admin events.
Supports stories: US-RES-4
Supports journeys: UJ-RES-1, UJ-RES-2
Priority: Should-have

## 6. Traceability matrix

| Story | Feature(s) | Journey(s) |
|-------|------------|------------|
| US-RES-1 | F-1, F-2 | UJ-RES-1 |
| US-RES-2 | F-3 | UJ-RES-1 |
| US-RES-3 | F-4 | UJ-RES-1, UJ-RES-2 |
| US-RES-4 | F-4, F-13 | UJ-RES-1, UJ-RES-2 |
| US-RES-5 | F-5, F-6, F-7, F-8 | UJ-RES-1 |
| US-RES-6 | F-4, F-5 | UJ-RES-1, UJ-RES-2 |
| US-RES-7 | F-8, F-9 | UJ-RES-1 |
| US-RES-8 | F-9, F-11 | UJ-RES-2, UJ-ADM-2 |
| US-ADM-1 | F-1, F-12 | UJ-ADM-1 |
| US-ADM-2 | F-4, F-10 | UJ-RES-2, UJ-ADM-2 |
| US-ADM-3 | F-11 | UJ-ADM-2 |
| US-ADM-4 | F-11 | UJ-ADM-2 |
| US-ADM-5 | F-12 | UJ-ADM-1 |

Every story maps to at least one feature and one journey. Every feature supports at least one story.

## 7. Open questions

1. **FTP vs. SFTP.** The spec says "FTP" but for internal research data, SFTP (or FTPS) is typically required for credential and data protection. Is plain FTP actually acceptable, or should this be SFTP?
2. **File-to-user linkage mechanism.** Is it sufficient to give each user their own FTP home directory, or do we also need a manifest file / claim-upload step in the web app? This affects both F-2 and US-RES-1.
3. **Supported array platforms.** Illumina methylation arrays include 450K, EPIC v1, and EPIC v2. Which platforms must the pipeline support at launch? This drives preprocessing, reference data, and QC thresholds in F-5 and F-7.
4. **Single-sample vs. cohort analyses.** Clustering and PCA/UMAP require ≥2 samples; CNV inference typically needs a reference panel. What are the minimum and maximum sample counts for a run, and is there a notion of "cohort"/"project" that groups samples across runs? Currently assumed to be a flat per-run selection.
5. **Collaboration and visibility.** Can researchers share a run or its report with another researcher inside the org, or are all runs private to their owner? The spec says "internal researchers" but does not address sharing.
6. **Authentication backend.** Is there a required SSO (e.g., SAML, OIDC via the org's IdP) or is local auth acceptable? Affects F-1 scope significantly.
7. **Data retention.** IDAT files are large; is there an automatic retention/cleanup policy, or must all uploads be kept indefinitely? Affects storage sizing and F-12 audit requirements.
8. **Clinical use.** The goal mentions "clinicians." Does this imply regulatory/compliance requirements (HIPAA, IVD, GxP) or is "clinician" just a second research-like user? This materially changes audit, validation, and reporting requirements.
9. **Notification channels.** The spec doesn't specify notifications; F-13 assumes in-app + email. Should we also consider chat integration (Slack/Teams)?
10. **Pipeline runtime expectations.** No performance targets are given (e.g., "N samples in under M minutes"). A rough SLO would let us size workers and set user expectations in US-RES-4.

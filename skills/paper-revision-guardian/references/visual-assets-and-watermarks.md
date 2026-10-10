# Visual Asset Consistency, Data Integrity, and Watermark Audit

## Purpose and scope

Apply this reference whenever a manuscript revision includes algorithm illustrations,
system/workflow diagrams, model architecture figures, experimental comparisons,
statistical plots, ablations, qualitative visualizations, or new/revised figures.
A polished appearance is not evidence that a figure is technically correct.

Priorities: research integrity and faithful data representation; correspondence with
methods and narrative; consistency with the paper's visual language; legibility and
journal requirements; publication-ready watermark-free material.

## 1. Establish the manuscript's visual baseline

Inspect several **existing, representative figures** before changing any figure.
Document the following where they are observable:

- palette (colors, saturation, contrast) and consistent meanings of colors;
- fonts, font sizes, mathematical notation, capitalization and units;
- stroke/arrow weights, markers, line styles, box corners and borders;
- relative margins, whitespace, grids, alignment, panel layout and visual density;
- axis/legend placement, tick conventions, subfigure labels and caption style;
- raster/vector format and effective readability at final publication size.

Follow the *dominant* existing style, not an arbitrary attractive external style.
When the existing manuscript is inconsistent, explain the conflict and propose a
coherent reference style before broad changes. Do not sacrifice scientific clarity,
color differentiation or accessibility merely to copy an existing defect. Do not
invent missing colors, measurements or semantic meanings.

## 2. Verify meaning for technical diagrams

For system, architecture, algorithm and workflow diagrams, check:

- component/module names and correspondence to manuscript terminology;
- data-flow and control-flow direction, inputs, outputs, dependencies and grouping;
- conditional branches, iteration order, feedback paths and stopping conditions;
- correspondence with equations, pseudocode, algorithm descriptions and code when available;
- absence of decorative arrows, implied mechanisms or modules not present in the research.

Preserve necessary details for interpretability and reproducibility. If a conceptual
simplification is proposed, record which elements are intentionally omitted.

## 3. Verify plotted data and statistical results

For experimental and statistical figures, whenever sources are available:

1. Trace each visualized series/panel to a dataset, table, analysis output or
   plotting script. Record source file, sheet/column or variable and relevant settings.
2. Compare numerical values, labels, units, axes, baselines, limits, scales,
   normalization, legends, seeds, methods, dataset splits and conditions.
3. Recalculate reported deltas and rankings and confirm metric direction.
4. Validate aggregation method, sample size, dispersion, error bars, confidence
   intervals, statistical tests, p-values, significance markers and multiple-
   comparison corrections **when such quantities are shown or claimed**.
5. Compare the figure with textual interpretation and associated tables. Identify
   unsupported generalization or visually misleading truncation, rescaling or omitted series.
6. If code/data are available and execution is authorized, reproduce plots in a
   separate output directory and compare numerical results. Preserve original data.

Never create plausible-looking numerical plots using invented values. Never silently
change source data, test results, statistical choices or axes to make a finding appear
stronger. If the figure is only available as an image or PDF, visually audit it but
mark underlying numeric/statistical correctness **not independently verified**.

## 4. Watermark-free publication gate

Publication-facing figures must be free of **unrelated** visible watermarks,
stock-preview stamps, screenshot UI residue, unauthorized logos, trial-software
marks and unintentional branding overlays.

- Inspect the full-resolution image, including borders, faint overlays, insets,
  backgrounds, legends and each subfigure; inspect source files and metadata where
  accessible and relevant.
- Distinguish legitimate scientific labels, intentionally cited logos and required
  attribution from removable decorative marks. Preserve required copyright notices
  and licensing obligations.
- If a third-party asset bears a watermark or restrictive attribution, **do not
  erase/crop/obscure ownership marks as a substitute for permission**. Request a
  licensed clean original, replace it with an authorized asset, or redraw the
  scientific content from sources the author is entitled to use.
- Regenerate original plots from owned data and scripts without tool or platform
  branding when possible.
- Withhold publication-ready approval if a visible or detectable watermark remains.

This is an **acceptance requirement**, not a claim of omniscience: checking pixels
cannot prove that no imperceptible forensic watermark or hidden provenance signal
exists. Report which checks were actually conducted; do not promise impossible
100% detection.

## 5. Caption, placement and visual integrity

Ensure captions identify what is plotted or diagrammed, necessary conditions,
subfigures, units and abbreviations without repeating paragraphs of results.
Check the figure's first substantive citation and narrative placement, subject to
the journal's float and page-layout rules. Export to appropriate resolution or
vector format where available; do not introduce distortion, clipped labels,
misaligned elements or decorative gradients inconsistent with the manuscript.

## 6. Required verification log

For each figure in scope, record a concise table or equivalent log containing:

- figure ID and source asset;
- baseline style reference (other figures/pages);
- technical/semantic consistency: **verified / issues found / not checked**;
- numerical integrity: **source-data verified / table checked / visual only / unavailable**;
- statistics: **recomputed / source-output checked / not applicable / unverified**;
- watermark status: **inspected and no visible marks found / issue found / not inspectable**;
- changes made, evidence used, remaining issues and the original figure retained.

Do not state "data verified" based on visual inspection alone. Do not state "no
watermarks anywhere" when only a rendered image was inspected. Preserve all source
files and maintain a reversible revision history.

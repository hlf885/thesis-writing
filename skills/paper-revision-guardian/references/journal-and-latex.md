# Journal Requirements and LaTeX Source Safety

For Advanced Robotics, prefer its current Instructions for Authors over publisher-wide guidelines, which take precedence over examples from published papers. Never present preferences from Nature/IEEE/NeurIPS as mandatory Advanced Robotics rules.

Preserve manuscript-specific `\\label`, `\\ref`, `\\cite`, `\\textbf`, math delimiters, theorem and algorithm environments, bibliography and local macros. Do not add unrelated formatting or expand established abbreviations mechanically. Check consistency of figure, table, equation and section references after any rewrite. Use valid LaTeX escaping for new prose without corrupting commands or math. Do not claim a successful compile unless it was run.

The optional read-only checker scans static references; macro-generated references and conditional graphics may produce false positives.
